def ETL():

    '''
    Function in a csv, turn it into a pandas dataframe.
    @return:
    1. df: a dataframe suitable for data analysis dashboards and EDA
    2. df_model: a dataframe ready for predictive models
    '''

    # Imports
    import numpy as np
    import pandas as pd
    from sklearn.pipeline import Pipeline
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler

    # Reading DataFrame
    df = pd.read_csv('healthcare-dataset-stroke-data.csv')
    df.drop('id', axis=1, inplace=True)

    # Pipeline for imputing missing values in bmi features
    imputing_pipe = Pipeline([('scaler', StandardScaler()),
                              ('rf', RandomForestRegressor(random_state=1))])

    # Creating a temp dataframes based on the most related features to the features with missing values
    X = df[['age', 'gender', 'avg_glucose_level', 'bmi']].copy()

    # Changing the string values for grnder into numerical for ease of handleing
    X['gender'] = X['gender'].map({
        'Male': 0,
        'Female': 1,
        'Other': -1
    }).astype(np.uint8)

    # to save the index of missing values to help refilling
    missing = X[X['bmi'].isna()]

    # Creating a dataframe with no null values for training
    X = X[~X['bmi'].isna()]

    # creating a series with bmi with no missing values as target for training
    Y = X.pop('bmi')

    # training the imputing model
    imputing_pipe.fit(X, Y)

    # Predicting the missing values and assigning their index as in the original model
    predicted_bmi = pd.Series(imputing_pipe.predict(
        missing[['age', 'gender', 'avg_glucose_level']]),
        index=missing.index)

    # Filling the missing values through indexing
    df.loc[missing.index, 'bmi'] = predicted_bmi

    # Dropping the only instance of gender 'Other'
    df = df[df['gender'] != 'Other']

    df_model = df.copy()

    # Mapping gender into numerical values with mean of 0
    df_model['gender'] = df['gender'].replace({
        'Male': 0,
        'Female': 1,
        'Other': -1
    }).astype(int)

    # Mapping into numerical
    df_model['Residence_type'] = df['Residence_type'].replace({
        'Rural': 0,
        'Urban': 1
    }).astype(int)

    # Mapping into numerical with mean of 0
    df_model['work_type'] = df['work_type'].replace({
        'Private': 0,
        'Self-employed': 1,
        'Govt_job': 2,
        'children': -1,
        'Never_worked': -2
    }).astype(int)

    # Mapping into numerical
    df_model['smoking_status'] = df['smoking_status'].replace({
        'never smoked': -1,
        'formerly smoked': 0,
        'smokes': 1,
        'Unknown': 2
    }).astype(int)

    # Mapping into numerical
    df_model['ever_married'] = df['ever_married'].replace({
        'Yes': 1,
        'No': 0
    }).astype(int)

    return df, df_model