Football Player Value Prediction
Women's Football Transfer Analysis
Introduction
The rising popularity of women's football has led to a more complex transfer market, with increasing transfer fees replacing traditional loan agreements. The number of women's football transfers has seen a steady increase, reaching 829 in the summer of 2023, with 66 transfers involving fees. This growth signifies a notable increase in the economic value of women's football.

Literature Review
Growth in Transfers and Expenditures
There has been a significant rise in both the number of transfers and the transfer fees involved. For instance, transfer fees reached $3 million in the summer of 2022, reflecting a 140.8% increase.

Importance of Data Analytics
The use of data analytics in football transfers can improve decision-making, traditionally based on intuition. Data-driven approaches can help clubs achieve more economical and successful transfers.

Use of Alternative Data Sources
Due to limited access to comprehensive player data, alternative sources like video games (e.g., FIFA) have been utilized to predict player performance and value. This approach helps overcome data scarcity and enhances analysis in football analytics.

Project Goal
This project aims to evaluate machine learning models to predict the value of women footballers, providing stakeholders with valuable insights for making strategic decisions in the transfer market.

Methodology
Data Acquisition
We extracted FIFA statistics of female football players from sofifa.com using a Python script. Data included overall ratings, positions, skills, and more, collected into a CSV file named "womendataset.csv".

Data Processing
The dataset was split into training (67.4%), testing (15%), and validation (17.6%) sets. Missing values were filled, and Min-Max normalization was applied.

Model Training
We trained and evaluated six different regression models, including Gradient Boosting, Random Forest, and K-Nearest Neighbors (KNN), among others. Bayesian Optimization was used to fine-tune the models.

Findings
Best Model: Gradient Boosting achieved the highest accuracy for predicting player market values.
Fastest Model: KNN was identified as the fastest in training.
Discussion
Machine learning models, particularly Gradient Boosting, proved effective in predicting the market values of female football players, offering valuable insights for clubs and agents. The use of data analytics in this context helps clubs make more informed transfer decisions.

Conclusion
The study demonstrates the effectiveness of machine learning models, especially Gradient Boosting, in predicting football player market values. The analysis highlights the strengths and limitations of different models, emphasizing the importance of data analytics in the football transfer market. Further research is needed to explore broader applications of these findings.

