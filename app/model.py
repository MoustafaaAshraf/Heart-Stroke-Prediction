def model(df):

    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.pipeline import Pipeline
    from feature_engine.outliers import Winsorizer
    from sklearn.metrics import accuracy_score, classification_report

    # Splitting the dataframe into target and features
    X = df.drop('stroke', axis=1)
    y = df['stroke']

    # Splitting the dataframe into training set and testing set
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.3,
                                                        random_state=1)

    # Creating a pipeline for ease of modelling
    pipe = Pipeline([
        # 1. Capping outliers based on fold of three, on both sides
        # 2. Training a model of Gradient Boosting
        ('outlier',
         Winsorizer(capping_method='gaussian',
                    tail='both',
                    fold=3,
                    variables=['age', 'bmi',
                               'avg_glucose_level'])),
        ('gbr', GradientBoostingClassifier(random_state=1))])

    # Training the model
    pipe.fit(X_train, y_train)

    # Making Predictions
    y_pred = pipe.predict(X_test)

    # Printing the classification metrics
    print('Accuracy score is: ', accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))