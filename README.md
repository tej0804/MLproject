# 1. Problem Statement
The goal is to predict whether a student will pass or fail based on features such as:

Gender

Race/Ethnicity

Parental Level of Education

Lunch type

Test Preparation Course

Reading Score

Writing Score

# 2. Data Source
Data was either synthetically created or sourced from the Student Performance dataset (common reference).

Features are both categorical and numerical, requiring preprocessing.

# 3. Feature Engineering
Extracted features:

Gender (categorical)

Race/Ethnicity (categorical)

Parental Level of Education (categorical)

Lunch (categorical)

Test Preparation Course (categorical)

Reading Score (numerical)

Writing Score (numerical)

A derived feature: Average Score = (Reading + Writing) / 2

# 4. Preprocessing
Used OneHotEncoding / LabelEncoding for categorical variables.

Used StandardScaler for numerical features.

Preprocessing pipeline was saved as preprocessor.pkl.

# 5. Model Building
Trained a classification model to predict Pass/Fail.

You mentioned RandomForestClassifier was used (or similar tree-based model).

Saved trained model as model.pkl.

# 6. Pipeline Architecture
Created two custom classes:

CustomData → Converts raw form data into a Pandas DataFrame

PredictPipeline → Loads preprocessor & model, transforms input, and performs prediction

# 7. Flask Integration
Built a web UI using Flask with two routes:

/ → Renders form to enter data (index.html)

/predictdata → Handles form input, predicts result, and renders home.html with output

# 8. HTML Pages
index.html → Input form for student data

home.html → Displays prediction result (e.g., "Pass" or "Fail")

# 9. Model Performance 
After evaluating model:

Accuracy: 88.04% 

Best Model: Random Forest Classifier

Metrics: Precision, Recall, F1-score

Visualizations (Confusion Matrix, ROC Curve)

