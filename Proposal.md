# Proposal 
## 1. Data set: https://www.kaggle.com/rakeshrau/social-network-ads 
We have chosen a data set which shows whether a product was purchased as a result of adds shown to members of a social networking community. What is important to note about the data is that the product that the advertisement is for is unknown. This means that the goal of working with the data set is to see whether the features Sex, Age and Income have any effect on whether the product was purchased. Therefore if these features have effects on purchasing, we can extrapolate and infer that they likely would have an effect of purchases for other products. 

## 2. Identify a research question:
Does gender, salary and/or age influence purchases based on social network adds? 
- Sub question: which predictor has the greatest impact on purchases made from social network adds?##

## 3. How will we address the problem and analyze the data? 
We will perform classification with a decision tree. If we can generate a model with acceptable train and test accuracies based on these features, we will be able to conclude that these features are good predictors and influence purchases based on social network adds. Furthermore, we can then address our predictive sub question for which feature has the greatest influence. 

## 4. Discuss at least one exploratory data analysis table and one exploratory data analysis figure you will create that makes sense for your research question, the data that you have, and the analysis you plan to do.
- **Table:** In our EDA .ipynb file we created a summary table of the features, in addition to two other tables separated by positive and negative target values.  to find the averages of the features associated with positive and negative results (purchased and not purchased)
- **Figure:** Create histograms of each feature with positive and negative target values separated. 

## 5. Suggest how you would share the results of your analysis as one or more tables and/or figures
- **Table:** By creating a general summary table, as well as two tables filtered for ‘purchased’ and ‘not purchased’ we will be able to find the average of all the features on social network sites, as well as the average of the features that correspond to purchases and not purchased. Since we observed differences between these values, we are able infer that these features likely have an effect on whether items are purchased based on social network adds. 
- **Figure:** By creating histograms for each feature separated for ‘purchased’ and ‘not purchased’ we will be able to view the distribution of all the values of a given feature, as well as if there are any clear division based on ‘purchased’ or ‘not purchased’ for each feature. 
- We will share the results as tables and figures displayed in our EDA.ipynb file. 
