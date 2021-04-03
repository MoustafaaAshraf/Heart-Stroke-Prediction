## Heart Stroke EDA & Prediction

A stroke is a medical condition in which poor blood flow to the brain causes cell death. There are two main types of stroke: ischemic, due to lack of blood flow, and hemorrhagic, due to bleeding. Both cause parts of the brain to stop functioning properly. Signs and symptoms of a stroke may include an inability to move or feel on one side of the body, problems understanding or speaking, dizziness, or loss of vision to one side. Signs and symptoms often appear soon after the stroke has occurred. If symptoms last less than one or two hours, the stroke is a transient ischemic attack (TIA), also called a mini-stroke. A hemorrhagic stroke may also be associated with a severe headache. The symptoms of a stroke can be permanent. Long-term complications may include pneumonia and loss of bladder control.

## Objective

- Exploring the data and relations between features and Creating an online Dashboard
- Training a model to predict if the person would suffer a stroke based on the studied features

## Used Libraries

- Pandas
- Numpy
- Scipy
- Matplotlib
- Seaborn
- Scikit-Learn
- feature-engine
- Flask

## Variable Description

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.

- id: unique identifier
- gender: "Male", "Female" or "Other"
- age: age of the patient
- hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
- heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
- ever_married: "No" or "Yes"
- work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
- Residence_type: "Rural" or "Urban"
- avg_glucose_level: average glucose level in blood
- bmi: body mass index
- smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
- stroke: 1 if the patient had a stroke or 0 if not

Note: "Unknown" in smoking_status means that the information is unavailable for this patient

## Workflow BreakDown
### 1. ETL
    - Dataset is read through pandas function .read_csv().
    - Dropping Un-needed columns (id).
    - Imputing bmi missing values (Missing-at-random) based on existing complete features ['age', 'gender', 'avg_glucose_level'] using RandomForestRegressor.
    - Changing categorical data in several columns into numerical ordinal values, as integers.  
    - Returning two dataframes df and df_model. One for Data analytics purpose and one of Predictive Modelling
### 2. Feature Diagnosis 
    - In order to perform regression model some diagnostic tests has to be performed checking:
    - Distribution of values and Outliers, in order to adjust preprocessing to acheive the best fit during training.
### 3. Questions and Data Analytics
    - Two questions are asked and answered through visualizations:
    - Is average Glucose Level and Bmi are determinant of Having a Stroke?
    - Is Gender a determinant factor for experiencing a Stroke?
### 4. Preprocessing and Model building Pipeline
    - According to the Diagnistic process, several features within the dataframe are prone to Outliers.
    - The preprocessing pipeline is restricted to capping the outliers to the maximum and minimum values in each columns.
    - The statistical model used for predicting is GradientBoostingClassifier
### 5. Model Performance Verification
    - After the model is trained, the performance is evaluated using accuracy and classification report.