# -Health-Data-Insights-Predicting-Diabetes-with-Machine-Learning

This project utilizes machine learning techniques to predict diabetes status based on health and behavioral data from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS) survey. By analyzing factors such as physical activity and BMI, the model aims to identify individuals at risk for diabetes, providing insights that could aid in early detection and intervention. Key evaluation metrics, including recall and f1-score, are prioritized to ensure a balanced assessment of model performance.

The initial_notebook.ipynb file includes the following steps:
* Loading the initial dataset
* Selecting desired columns
* Filtering rows based on specified criteria for each selected column
* Performing a basic exploratory analysis of the predictor and target variables


**November 25, 2024 Update**

The notebook titled 'first model building process.ipynb' documents the initial fitting of three models: Logistic Regression, Random Forest Classifier, and Histogram Gradient Boosting Classifier. The highest f1-score achieved so far is 0.48, obtained with the Histogram Gradient Boosting Classifier. While this is below the desired performance, it represents a good starting point. There's significant opportunity for improvement, and I plan to explore further refinements and optimizations to enhance the model's performance.


**November 26, 2024 Update**

The notebook titled 'a_second_attempt.ipynb' documents the new preprocessing steps applied to the training and testing predictors (one-hot encoding of discrete variables), along with stratification of the target variable. The objective was to fit multiple models, including Logistic Regression, Random Forest Classifier, Balanced Random Forest Classifier, Histogram Gradient Boosting Classifier, and XGB Classifier, to achieve a higher F1 score for diabetic instances. However, the best F1 score remained at 0.48, achieved by both the Histogram Gradient Boosting Classifier and the XGB Classifier.


**November 28, 2024 Update**

The notebook titled 'analyzing the scoring.ipynb' documents the exploration of recall, precision, and F1 score for the Histogram Gradient Boosting (HistGradientBoost) and XGBoost (XGB) classifier models predicting whether an individual is diabetic. Attempts were made to adjust the threshold used by each model to determine whether the predicted probability warranted a diabetic or non-diabetic classification. Additionally, oversampling of the minority class (SMOTE) and a combination of oversampling the minority class with undersampling the majority class (SMOTE combined) were applied to the training data. The issue with the threshold adjustments was that the F1 score only reached a maximum of 0.48 for both the HistGradientBoost and XGBoost classifiers. If the focus were instead on maximizing recall or precision, it would have been easy to adjust the threshold to achieve a suitable score. For the SMOTE models, the model with the oversampled minority class failed to generalize to the testing data, as the training data had approximately balanced classes, but the testing data was heavily imbalanced. For the combined-SMOTE model, there were no noticeable improvements at all.


**December 3, 2024 Update**

Unfortunately, I have decided to conclude this project without any future updates. While it's disappointing, I had envisioned eventually creating an interactive interface where individuals could answer questions and the model would predict whether they are diabetic. However, I wanted the model to be decent, focusing primarily on the F1-score for the positive (diabetic) class. The severe class imbalance in the dataset, where the negative class vastly outnumbered the positive class, made this goal challenging. Although the dataset doesn't represent the entire world, this imbalance reflects the real-world scenario where more people are non-diabetic than diabetic. This project has been a valuable learning experience, despite the challenges in achieving my desired outcomes.
