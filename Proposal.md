# Proposal 
## 1. Data set: https://www.superdatascience.com/pages/machine-learning
We have chosen a data set which shows whether a person donated blood on specific date as a result of their past donation history. The goal of working with the data set is to see whether the features Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on that date. Therefore if these features have effects on donation, we can extrapolate and infer that they likely would have an effect on future donation.

## 2. Identify a research question:
Do Recency(last donation month), Frequency(total number of donation) and Monetary(total blood donated) have any effect on whether the blood was donated on a specific date? 
- Sub question: which predictor has the greatest impact on donation ?##

## 3. How will we address the problem and analyze the data? 
We will perform classification with a decision tree. If we can generate a model with acceptable train and test accuracies based on these features, we will be able to conclude that these features are good predictors and influence donation based on donation history. Furthermore, we can then address our predictive sub question for which feature has the greatest influence. 

## 4. Discuss at least one exploratory data analysis table and one exploratory data analysis figure you will create that makes sense for your research question, the data that you have, and the analysis you plan to do.
- **Table:** In our EDA .ipynb file we created a summary table of the features, in addition to two other tables separated by positive and negative target values.  to find the averages of the features associated with positive and negative results (donated and not donated)
- **Figure:** Create histograms of each feature with positive and negative target values separated. 

## 5. Suggest how you would share the results of your analysis as one or more tables and/or figures
- **Table:** By creating a general summary table, as well as two tables filtered for ‘donated’ and ‘not donated’ we will be able to find the average of all the features on donation history, as well as the average of the features that correspond to donated and not donated. Since we observed differences between these values, we are able infer that these features likely have an effect on whether blood will be donated based on donation history. 
- **Figure:** By creating histograms for each feature separated for ‘donated’ and ‘not donated’ we will be able to view the distribution of all the values of a given feature, as well as if there are any clear division based on ‘donated’ or ‘not donated’ for each feature. 
- We will share the results as tables and figures displayed in our EDA.ipynb file. 
