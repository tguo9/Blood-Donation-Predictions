# mds522_305: Social Network Add Purchases Predictor
* Contributors: 
  - Evelyn Moorhouse
  - Tao Guo
  - Lise Braaten 
  - Xinwen Wang
  
## Introduction

The goal of this project is to see whether the features Sex, Age and Income have any effect on whether the product was purchased. This is important information for companies interested in advertising through social networking websites. 

We have chosen a data set which shows whether a product was purchased as a result of adds shown to members of a social networking community. The dataset is sourced from an online course Machine Learning A-Z by Kirill Eremenko and Hadelin de Ponteves, https://www.superdatascience.com/pages/machine-learning. What is important to note about the data is that the product that the advertisement is for is unknown. This means that the goal of working with the data set is to see whether the features Sex, Age and Income have any effect on whether the product was purchased. Therefore if these features have effects on purchasing, we can extrapolate and infer that they likely would have an effect of purchases for other products.

We will perform classification with a decision tree. If we can generate a model with acceptable train and test accuracies based on these features, we will be able to conclude that these features are good predictors and influence purchases based on social network adds. Furthermore, we can then address our predictive sub question for which feature has the greatest influence.

## Dependencies

Python 3.7.3 and Python packages: </br>
        skleanr==0.22.1 </br>
        pandas==0.24.2 </br>
        altair==3.2.0 </br>
        
## References

Kirill Eremenko and Hadelin de Ponteves, https://www.superdatascience.com/pages/machine-learning
