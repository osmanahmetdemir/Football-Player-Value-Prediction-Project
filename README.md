# Football Player Value Prediction Project
### 1) Data Mining and Machine Learning

## ![Overview](https://img.shields.io/badge/Overview-green)
This project analyzes the transfer market for women's football, using machine learning models to predict player market values. As the popularity of women's football grows, the transfer market has become more complex, with increasing transfer fees and data analytics playing a crucial role in decision-making.

## ![Literature Review](https://img.shields.io/badge/Literature_Review-red)

### ![Growth in Transfers and Expenditures](https://img.shields.io/badge/Growth_in_Transfers_and_Expenditures-orange)
- **Significant rise in both transfer numbers and fees.**
- **Example:** Transfer fees reached $3 million in summer 2022, marking a 140.8% increase.

### ![Importance of Data Analytics](https://img.shields.io/badge/Importance_of_Data_Analytics-purple)
Data-driven decision-making can enhance transfer success compared to intuition-based approaches.

### ![Use of Alternative Data Sources](https://img.shields.io/badge/Use_of_Alternative_Data_Sources-brown)
Alternative data, like video games (e.g., FIFA), are utilized to predict player performance due to limited access to comprehensive player data.

## ![Project Goal](https://img.shields.io/badge/Project_Goal-teal)
To evaluate machine learning models for predicting the value of women footballers, providing stakeholders with actionable insights for strategic decisions in the transfer market.

## ![Methodology](https://img.shields.io/badge/Methodology-darkcyan)

### ![Data Acquisition](https://img.shields.io/badge/Data_Acquisition-darkorange)
- **Source:** Data collected from sofifa.com.
- **Process:** Python script used to scrape data, including player ratings, positions, skills, etc.
- **Output:** Data stored in `womendataset.csv`.

### ![Data Processing](https://img.shields.io/badge/Data_Processing-darkred)
- **Data Split:**
  - Training: 67.4%
  - Testing: 15%
  - Validation: 17.6%
- **Preprocessing:** Filling missing values and applying Min-Max normalization.

### ![Model Training](https://img.shields.io/badge/Model_Training-darkgreen)
- **Models:** Gradient Boosting, Random Forest, K-Nearest Neighbors (KNN), etc.
- **Optimization:** Bayesian Optimization for hyperparameter tuning.

## ![Findings](https://img.shields.io/badge/Findings-darkblue)
- **Best Model:** Gradient Boosting achieved the highest accuracy.
- **Fastest Model:** KNN was the fastest in training.

## ![Discussion](https://img.shields.io/badge/Discussion-darkmagenta)
Machine learning models, especially Gradient Boosting, effectively predict the market values of female football players. This provides clubs and agents with valuable insights for making informed transfer decisions.

## ![Conclusion](https://img.shields.io/badge/Conclusion-darkviolet)
The study highlights the effectiveness of machine learning models in predicting football player market values. Further research is necessary to explore the broader applications of these findings in the football transfer market.

### 2) SEO Player Value UI

In the first part of our project, we wanted to present the results from our ML model to users more clearly through the UI, displaying statistics and predicted values.

The general project interface and the data we collected are displayed.

The functionality of the search button in our project interface is demonstrated.

To view player statistics in our project, we can click the "View Stats" button. Player statistics in our project are displayed.

In our project, we can sort features such as Position, Age, Club, Nationality, and Value. Here, sorting the Age feature is demonstrated.
