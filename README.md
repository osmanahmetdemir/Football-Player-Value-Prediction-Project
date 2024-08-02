# Football Player Value Prediction Project
![logo](https://github.com/user-attachments/assets/3c1bdc32-e76b-47af-b1c4-40ef4eb8e34b)

### 1) Data Mining and Machine Learning

## ![Overview](https://img.shields.io/badge/Overview-green)
This project analyzes the transfer market for women and men football, using machine learning models to predict player market values. As the popularity of women football grows, the transfer market has become more complex, with increasing transfer fees and data analytics playing a crucial role in decision-making.

## ![Literature Review](https://img.shields.io/badge/Literature_Review-red)

### ![Growth in Transfers and Expenditures](https://img.shields.io/badge/Growth_in_Transfers_and_Expenditures-orange)
- Significant rise in both transfer numbers and fees.
- Example: Transfer fees reached $3 million in summer 2022, marking a 140.8% increase.

### ![Importance of Data Analytics](https://img.shields.io/badge/Importance_of_Data_Analytics-purple)
Data-driven decision-making can enhance transfer success compared to intuition-based approaches.

### ![Use of Alternative Data Sources](https://img.shields.io/badge/Use_of_Alternative_Data_Sources-brown)
Alternative data, like video games (e.g., FIFA), are utilized to predict player performance due to limited access to comprehensive player data.

## ![Project Goal](https://img.shields.io/badge/Project_Goal-teal)
To evaluate machine learning models for predicting the value of women footballers, providing stakeholders with actionable insights for strategic decisions in the transfer market.

## ![Methodology](https://img.shields.io/badge/Methodology-darkcyan)

### ![Data Acquisition](https://img.shields.io/badge/Data_Acquisition-darkorange)
- Source: Data collected from sofifa.com.
- Process: Python script used to scrape data, including player ratings, positions, skills, etc.
- Output: Data stored in womendataset.csv.

### ![Data Processing](https://img.shields.io/badge/Data_Processing-darkred)
- Data Split:
  - Training: 67.4%
  - Testing: 15%
  - Validation: 17.6%
- Preprocessing: Filling missing values and applying Min-Max normalization.

### ![Model Training](https://img.shields.io/badge/Model_Training-darkgreen)
- Models: Gradient Boosting, Random Forest, K-Nearest Neighbors (KNN), Decision Tree, AdaBoost, Linear Regression(It is not regression model, we wanted to show that).
- Optimization: Bayesian Optimization and Grid Search for hyperparameter tuning.

### ![Libraries Used](https://img.shields.io/badge/Libraries_Used-darkblue)
The following Python libraries were utilized in this project:

- sklearn: For machine learning algorithms and model evaluation. It includes a range of supervised and unsupervised learning algorithms, as well as tools for model evaluation and selection.
- seaborn: For creating attractive and informative statistical graphics. It simplifies data visualization and exploration.
- matplotlib.pyplot: For plotting graphs and visualizing data. It is a versatile library used for creating a wide range of static, animated, and interactive plots.
- pandas: For data manipulation and analysis. It provides data structures and functions needed to work on structured data seamlessly.
- numpy: For numerical computations and array operations. It supports large, multi-dimensional arrays and matrices, along with a large collection of mathematical functions to operate on these arrays.

## ![Findings](https://img.shields.io/badge/Findings-darkblue)
- Best Model: Gradient Boosting achieved the highest accuracy.
- Fastest Model: KNN was the fastest in training.

## ![Discussion](https://img.shields.io/badge/Discussion-darkmagenta)
Machine learning models, especially Gradient Boosting, effectively predict the market values of female football players. This provides clubs and agents with valuable insights for making informed transfer decisions.

## ![Conclusion](https://img.shields.io/badge/Conclusion-darkviolet)
The study highlights the effectiveness of machine learning models in predicting football player market values. Further research is necessary to explore the broader applications of these findings in the football transfer market.

### 2) SEO Player Value UI

In the first part of our project, we wanted to present the results from our ML model to users more clearly through the UI, displaying predicted values of women football players. We tried to design an interface as user-friendly as possible.
![image](https://github.com/user-attachments/assets/dba5b94e-894e-43c3-9e14-59f358fb3c30)

The functionality of the search button in our project interface is demonstrated.

![image](https://github.com/user-attachments/assets/9db7d309-ba07-4d04-ae76-8f8aa44ac86e) ![image](https://github.com/user-attachments/assets/a677aced-7b89-42f8-844b-a510fce5c958) ![image](https://github.com/user-attachments/assets/0274bb66-43fc-4874-ac56-a09ab5b46260)

In our project, we can sort features such as Position, Age, Club, Nationality, and Value. Here, sorting the Age feature is demonstrated.

![image](https://github.com/user-attachments/assets/39d1a7f3-6d9a-4995-9a03-4741066230c2) ![image](https://github.com/user-attachments/assets/a5a0c06b-f30b-424f-bfd1-8fce7afd7b17) ![image](https://github.com/user-attachments/assets/0fa0c372-453f-4f3f-b703-527722ebea55)

To view player statistics in our project, we can click the "View Stats" button. Player statistics in our project are displayed.

![image](https://github.com/user-attachments/assets/e8d3f947-bbaf-40d4-8861-40568e2974fc) ![image](https://github.com/user-attachments/assets/48f54e2d-547b-414c-ba02-108c6cdb665c)


To view men football players' statistics and predicted values, we can click the "Men" button. 

![image](https://github.com/user-attachments/assets/68d12414-6e37-4521-bc06-5f4f3b15f009) ![image](https://github.com/user-attachments/assets/31c51384-919a-46cc-9951-01cdb2da1fb0)

Searching and filtering is valid for this tab too. 

![image](https://github.com/user-attachments/assets/6028f0dc-967c-4530-92fc-a36ab17d89b7)


You can send an e-mail at any time to get more detailed information about Data Mining, Machine Learning and User Interface in the project and to ask your questions: =)
