Blood Donation Predictors Report
================
Group 305
2020-02-08

``` r
library(reticulate)
os <- import("os")
library(kableExtra)
```

## Introduction

Blood donations are a vital component of saving lives, and there is an
ever-growing need for healthy and clean volunteer donors (Gillespie &
Hillyer, 2002). Finding donors that will be a repeated donor is a hard
task for many transfusion centers (Armitage & Conner, 2001). This leads
to a need for understanding what motivates individuals to donate blood,
and whether there are certain factors that effect if someone chooses to
donate blood or not, specifically if they have previously been a donor.
To try and address this question we explore a dataset provided by
I-Cheng et al. (2008), which indicates whether an individual donated
blood or not. Each donor has four characteristics associated with them,
(1) the time in months since their last donation (Recency), (2) the
total number of times they have donated (Frequency), (3) the total
amount of blood they have donated in centilitres (Monetary), and (4) the
time since their first donation in months (Time). We are using this
dataset to observe if these features influence whether an individual
donated blood.

## Preliminary EDA

Before creating any models or statistical tests we conducted a
preliminary exploratory data analysis to provide insights into how our
model would perform. Prior to the EDA we split our data into train and
test sets, and then used the train set to derive information. As shown
in Table 1, we determined that there were 598 observation in our train
dataset. We separated our data into two additional tables based on the
target class, Table 2 for only those that did not donate, and Table 3
for only donors. Based on this separation we saw our data was
imbalanced. Class 1 representing those candidates who did not donate,
had 460 observations, versus class 2 with 138 individuals who did
donate. We also noted from Table 1 that almost all features had a high
variance, which indicated to us that these may not be exceptionally
predictive.

``` python
import pandas as pd
blood_df_train = pd.read_csv('../data/processed/train_data.csv').drop('Unnamed: 0', axis = 1)
table_1 = blood_df_train.describe()
table_2 = blood_df_train[blood_df_train['Class']==1].describe()
table_3 = blood_df_train[blood_df_train['Class']==2].describe()
```

``` r
print('Table 1:')
```

    ## [1] "Table 1:"

``` r
py$table_1 %>%
  kable() %>%
  kable_styling()
```

<table class="table" style="margin-left: auto; margin-right: auto;">

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:right;">

since\_last\_don

</th>

<th style="text-align:right;">

total\_dons

</th>

<th style="text-align:right;">

total\_blood

</th>

<th style="text-align:right;">

since\_first\_don

</th>

<th style="text-align:right;">

Class

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

count

</td>

<td style="text-align:right;">

598.000000

</td>

<td style="text-align:right;">

598.000000

</td>

<td style="text-align:right;">

598.000

</td>

<td style="text-align:right;">

598.00000

</td>

<td style="text-align:right;">

598.0000000

</td>

</tr>

<tr>

<td style="text-align:left;">

mean

</td>

<td style="text-align:right;">

9.951505

</td>

<td style="text-align:right;">

5.653846

</td>

<td style="text-align:right;">

1413.462

</td>

<td style="text-align:right;">

35.03010

</td>

<td style="text-align:right;">

1.2307692

</td>

</tr>

<tr>

<td style="text-align:left;">

std

</td>

<td style="text-align:right;">

8.399130

</td>

<td style="text-align:right;">

5.939018

</td>

<td style="text-align:right;">

1484.755

</td>

<td style="text-align:right;">

24.34569

</td>

<td style="text-align:right;">

0.4216778

</td>

</tr>

<tr>

<td style="text-align:left;">

min

</td>

<td style="text-align:right;">

0.000000

</td>

<td style="text-align:right;">

1.000000

</td>

<td style="text-align:right;">

250.000

</td>

<td style="text-align:right;">

2.00000

</td>

<td style="text-align:right;">

1.0000000

</td>

</tr>

<tr>

<td style="text-align:left;">

25%

</td>

<td style="text-align:right;">

4.000000

</td>

<td style="text-align:right;">

2.000000

</td>

<td style="text-align:right;">

500.000

</td>

<td style="text-align:right;">

16.00000

</td>

<td style="text-align:right;">

1.0000000

</td>

</tr>

<tr>

<td style="text-align:left;">

50%

</td>

<td style="text-align:right;">

9.000000

</td>

<td style="text-align:right;">

4.000000

</td>

<td style="text-align:right;">

1000.000

</td>

<td style="text-align:right;">

28.00000

</td>

<td style="text-align:right;">

1.0000000

</td>

</tr>

<tr>

<td style="text-align:left;">

75%

</td>

<td style="text-align:right;">

14.750000

</td>

<td style="text-align:right;">

7.000000

</td>

<td style="text-align:right;">

1750.000

</td>

<td style="text-align:right;">

50.75000

</td>

<td style="text-align:right;">

1.0000000

</td>

</tr>

<tr>

<td style="text-align:left;">

max

</td>

<td style="text-align:right;">

74.000000

</td>

<td style="text-align:right;">

50.000000

</td>

<td style="text-align:right;">

12500.000

</td>

<td style="text-align:right;">

98.00000

</td>

<td style="text-align:right;">

2.0000000

</td>

</tr>

</tbody>

</table>

``` r
print('Table 2:')
```

    ## [1] "Table 2:"

``` r
py$table_2 %>%
  kable() %>%
  kable_styling()
```

<table class="table" style="margin-left: auto; margin-right: auto;">

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:right;">

since\_last\_don

</th>

<th style="text-align:right;">

total\_dons

</th>

<th style="text-align:right;">

total\_blood

</th>

<th style="text-align:right;">

since\_first\_don

</th>

<th style="text-align:right;">

Class

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

count

</td>

<td style="text-align:right;">

460.000000

</td>

<td style="text-align:right;">

460.000000

</td>

<td style="text-align:right;">

460.000

</td>

<td style="text-align:right;">

460.00000

</td>

<td style="text-align:right;">

460

</td>

</tr>

<tr>

<td style="text-align:left;">

mean

</td>

<td style="text-align:right;">

11.315217

</td>

<td style="text-align:right;">

4.969565

</td>

<td style="text-align:right;">

1242.391

</td>

<td style="text-align:right;">

36.12174

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:left;">

std

</td>

<td style="text-align:right;">

8.699697

</td>

<td style="text-align:right;">

4.908215

</td>

<td style="text-align:right;">

1227.054

</td>

<td style="text-align:right;">

24.56627

</td>

<td style="text-align:right;">

0

</td>

</tr>

<tr>

<td style="text-align:left;">

min

</td>

<td style="text-align:right;">

0.000000

</td>

<td style="text-align:right;">

1.000000

</td>

<td style="text-align:right;">

250.000

</td>

<td style="text-align:right;">

2.00000

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:left;">

25%

</td>

<td style="text-align:right;">

4.000000

</td>

<td style="text-align:right;">

2.000000

</td>

<td style="text-align:right;">

500.000

</td>

<td style="text-align:right;">

16.00000

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:left;">

50%

</td>

<td style="text-align:right;">

11.000000

</td>

<td style="text-align:right;">

3.000000

</td>

<td style="text-align:right;">

750.000

</td>

<td style="text-align:right;">

28.00000

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:left;">

75%

</td>

<td style="text-align:right;">

16.000000

</td>

<td style="text-align:right;">

7.000000

</td>

<td style="text-align:right;">

1750.000

</td>

<td style="text-align:right;">

52.00000

</td>

<td style="text-align:right;">

1

</td>

</tr>

<tr>

<td style="text-align:left;">

max

</td>

<td style="text-align:right;">

74.000000

</td>

<td style="text-align:right;">

44.000000

</td>

<td style="text-align:right;">

11000.000

</td>

<td style="text-align:right;">

98.00000

</td>

<td style="text-align:right;">

1

</td>

</tr>

</tbody>

</table>

``` r
print('Table 3:')
```

    ## [1] "Table 3:"

``` r
py$table_3 %>%
  kable() %>%
  kable_styling()
```

<table class="table" style="margin-left: auto; margin-right: auto;">

<thead>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:right;">

since\_last\_don

</th>

<th style="text-align:right;">

total\_dons

</th>

<th style="text-align:right;">

total\_blood

</th>

<th style="text-align:right;">

since\_first\_don

</th>

<th style="text-align:right;">

Class

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

count

</td>

<td style="text-align:right;">

138.000000

</td>

<td style="text-align:right;">

138.000000

</td>

<td style="text-align:right;">

138.000

</td>

<td style="text-align:right;">

138.00000

</td>

<td style="text-align:right;">

138

</td>

</tr>

<tr>

<td style="text-align:left;">

mean

</td>

<td style="text-align:right;">

5.405797

</td>

<td style="text-align:right;">

7.934783

</td>

<td style="text-align:right;">

1983.696

</td>

<td style="text-align:right;">

31.39130

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:left;">

std

</td>

<td style="text-align:right;">

5.175232

</td>

<td style="text-align:right;">

8.134998

</td>

<td style="text-align:right;">

2033.750

</td>

<td style="text-align:right;">

23.31424

</td>

<td style="text-align:right;">

0

</td>

</tr>

<tr>

<td style="text-align:left;">

min

</td>

<td style="text-align:right;">

0.000000

</td>

<td style="text-align:right;">

1.000000

</td>

<td style="text-align:right;">

250.000

</td>

<td style="text-align:right;">

2.00000

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:left;">

25%

</td>

<td style="text-align:right;">

2.000000

</td>

<td style="text-align:right;">

3.000000

</td>

<td style="text-align:right;">

750.000

</td>

<td style="text-align:right;">

15.00000

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:left;">

50%

</td>

<td style="text-align:right;">

4.000000

</td>

<td style="text-align:right;">

6.000000

</td>

<td style="text-align:right;">

1500.000

</td>

<td style="text-align:right;">

28.00000

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:left;">

75%

</td>

<td style="text-align:right;">

4.000000

</td>

<td style="text-align:right;">

10.000000

</td>

<td style="text-align:right;">

2500.000

</td>

<td style="text-align:right;">

41.75000

</td>

<td style="text-align:right;">

2

</td>

</tr>

<tr>

<td style="text-align:left;">

max

</td>

<td style="text-align:right;">

26.000000

</td>

<td style="text-align:right;">

50.000000

</td>

<td style="text-align:right;">

12500.000

</td>

<td style="text-align:right;">

98.00000

</td>

<td style="text-align:right;">

2

</td>

</tr>

</tbody>

</table>

In addition to the tables we also created visualizations to help us
understand the distribution of the data. Though not included in this
report, in the EDA.ipynb file we looked at all observations together,
regardless of whether the observation indicated donated or not donated.
Through our plots we observed that almost all features had an
exponential distribution. In figures 1, 2, and 3 seen below where we
chose to separate features based on class and instead of a bar based
histograms from our initial EDA, we plotted density. The only feature we
did not create a figure for was total donations. This is because total
blood donations and total amount of blood donated had almost identical
results graphically. Figure 1 shows that the density of the time since
the first blood donation for both individuals that donated and did not
donate was very similar. Based on this observation it is likley that
time since first donation wouldn’t be a strong differentiating feature.
In constrast, figure 2 showed that the time since the last donation
could be a decent predictor, since the number of individuals who ended
up donating had often donated quite recently, indicating they are
probably a frequent donor. Figure 3 indicated that there is likley a
small predictive power for total blood donation, since those individuals
that had not donated recently had actually donated more blood in
general.

|              Figure 1               |              Figure 2              | Figure 3                        |
| :---------------------------------: | :--------------------------------: | :------------------------------ |
| ![](../results/since_first_don.png) | ![](../results/since_last_don.png) | ![](../results/total_blood.png) |

## Methods

To address our research question of whether our features could be used
as predictors for blood donation we decided to create and test three
models that are all designed to perform well in binary classification
problems. The three models were a Random Forest classifier, a Decision
Tree and a Logistic Regression Classifier. Prior to implementing the
models, we cleaned and processed the data to ensure there were no
missing or erroneous values. We then selected a random subset of the
class 1 portion of the training data to address the training imbalance,
so our model was trained on a dataset that had a 50% split of classes.
Once this was completed, we created mutliple models and performed a
GridCV search to tune for the best hyperparameters of each model with
10-fold cross validation to fit and train the
model.

## Results

``` python
results = pd.read_csv('../results/analysis_result.csv', names=["Info", "Scores"])
rndm_frst = results.loc[5,'Scores']
lgst_rgrsn = results.loc[16,'Scores']
```

``` r
print('Table 4:')
```

    ## [1] "Table 4:"

``` r
py$results %>%
  kable() %>%
  kable_styling()
```

<table class="table" style="margin-left: auto; margin-right: auto;">

<thead>

<tr>

<th style="text-align:left;">

Info

</th>

<th style="text-align:left;">

Scores

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

method

</td>

<td style="text-align:left;">

Random Forest

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_max\_depth

</td>

<td style="text-align:left;">

\[4\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_min\_samples\_split

</td>

<td style="text-align:left;">

\[2\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_CV\_Score

</td>

<td style="text-align:left;">

\[0.6954545454545454\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Training\_Error

</td>

<td style="text-align:left;">

\[0.2090909090909091\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Validation\_Error

</td>

<td style="text-align:left;">

\[0.3035714285714286\]

</td>

</tr>

<tr>

<td style="text-align:left;">

method

</td>

<td style="text-align:left;">

Decision Tree

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_max\_depth

</td>

<td style="text-align:left;">

\[7\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Bestmin\_samples\_split

</td>

<td style="text-align:left;">

\[4\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_CV\_Score

</td>

<td style="text-align:left;">

\[0.6590909090909091\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Training\_Error

</td>

<td style="text-align:left;">

\[0.15000000000000002\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Validation\_Error

</td>

<td style="text-align:left;">

\[0.3571428571428571\]

</td>

</tr>

<tr>

<td style="text-align:left;">

method

</td>

<td style="text-align:left;">

Logistic regression

</td>

</tr>

<tr>

<td style="text-align:left;">

C

</td>

<td style="text-align:left;">

\[1\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Best\_CV\_Score

</td>

<td style="text-align:left;">

\[0.7090909090909091\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Training\_Error

</td>

<td style="text-align:left;">

\[0.2727272727272727\]

</td>

</tr>

<tr>

<td style="text-align:left;">

Validation\_Error

</td>

<td style="text-align:left;">

\[0.3214285714285714\]

</td>

</tr>

</tbody>

</table>

In table 4 we show the results for all three models, including the best
hyperparameters and the train and validation errors. With our random
seed, the Random Forest model at \[0.3035714285714286\] had a better
validation error than the Logistic Regression model at
\[0.3214285714285714\]. However, the Logistic Regression model was
significantly less overfit than the Random Forest model, since the
difference between train and validation error was much smaller than the
difference in the Random Forest model.

## Discussion

Based on our results we infer that the features of 1) time since last
donation, 2) total number of donations, 3) total blood donated, and 4)
the time since the first donation, all combined have some predictive
power for whether a patient will donate blood. However, even with
training three models and optimizing their respective hyperparameters,
the best train and test accuracy scores were low. With an accuracy score
of 0.5 being equivalent to random, the best score of the Random Forest
model at \[0.3035714285714286\] isn’t much better than random in terms
of strength of predictive power. If a model was to be used to predict
blood donation based on these features we would recommend a Logistic
Regression classifier, even though it had a higher validation error than
the Random Forest. This is because the difference between train and
validation error is much less than the Random Forest model, and
therefore it would be a better model for generalization. However, since
the predictive power for these features is so low, regarless of the
model, we wouldn’t recommend using these features for predicting blood
donation. We would suggest that more reasearch needs to be conducted to
identify other features that may provide better predictions for whether
blood is donated by a past donor.

## Conclusion

Based on our results we infer that the features of 1) time since last
donation, 2) total number of donations, 3) total blood donated, and 4)
the time since the first donation, all combined have some predictive
power for whether a patient will donate blood. However, since our
accuracy and cross validation scores were low, the combined predictive
power of these features is quite low. Since the predictive power is so
low, we suggest that these features don’t have a strong influence on
whether a patient donates blood or not. We would suggest that other
factors may provide better predictions as to whether blood is donated by
a past donor.

## References

Armitage, C. J., & Conner, M. (2001). Social cognitive determinants of
blood donation. Journal of applied social psychology, 31(7), 1431-1457.
</br></br> de Jonge, Edwin. 2018. Docopt: Command-Line Interface
Specification Language. <https://CRAN.R-project.org/package=docopt>.
</br></br> Gillespie, T. W., & Hillyer, C. D. (2002). Blood donors and
factors impacting the blood donation decision. Transfusion Medicine
Reviews, 16(2), 115-130. </br></br> Keleshev, Vladimir. 2014. Docopt:
Command-Line Interface Description Language.
<https://github.com/docopt/docopt>. </br></br> R Core Team. 2019. R: A
Language and Environment for Statistical Computing. Vienna, Austria: R
Foundation for Statistical Computing. <https://www.R-project.org/>.
</br></br> Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V.,
Thirion, B., Grisel, O., … & Vanderplas, J. (2011). Scikit-learn:
Machine learning in Python. Journal of machine learning research,
12(Oct), 2825-2830 </br></br> VanderPlas et al. Altair: Interactive
Statistical Visualizations for Python. Journal of Open Source Software
(2018) </br></br> Van Rossum, Guido, and Fred L. Drake. 2009. Python 3
Reference Manual. Scotts Valley, CA: CreateSpace. </br></br> Wes
McKinney. Data Structures for Statistical Computing in Python,
Proceedings of the 9th Python in Science Conference, 51-56 (2010)
(publisher link) </br></br> Wickham, H. (2016). ggplot2: elegant
graphics for data analysis. Springer. </br></br> Wickham, Hadley. 2017.
Tidyverse: Easily Install and Load the ’Tidyverse’.
<https://CRAN.R-project.org/package=tidyverse>. </br></br> Xie, Yihui.
2014. “Knitr: A Comprehensive Tool for Reproducible Research in R.” In
Implementing Reproducible Computational Research, edited by Victoria
Stodden, Friedrich Leisch, and Roger D. Peng. Chapman; Hall/CRC.
<http://www.crcpress.com/product/isbn/9781466561595>. </br></br> Yeh, I.
C., Yang, K. J., & Ting, T. M. (2009). Knowledge discovery on RFM model
using Bernoulli sequence. Expert Systems with Applications, 36(3),
5866-5871 </br></br>
