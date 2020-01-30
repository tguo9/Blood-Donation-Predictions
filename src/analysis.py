# authors: DSCI 522 Group 305 
# date: 2020-01-22

"""
This script read in the data processed by pre-process.py and apply decision tree algorithm

Usage: src/analysis.py --train_data=<train_data>  --local_path=<local_path>

Options:
--train_data=<train_data>  Local path to the training data csv file (include file name)
--local_path=<local_path>  Local path to folder you want the analysis files to be written to 
"""

import pandas as pd
from docopt import docopt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.model_selection import GridSearchCV

opt = docopt(__doc__)

def main(train_data, local_path):
    # in console type: python src/analysis.py --train_data=./data/processed/train_data.csv  --local_path=./results
    
    #convert to pandas data frame
    train_df = pd.read_csv(train_data)

    #resample due to unbalanced data set more people not donate
    donate = train_df[train_df.Class == 2]
    not_donate = train_df[train_df.Class == 1]
    not_resample = resample(not_donate, replace = False, n_samples=len(donate), random_state= 100)
    train_df = pd.concat([donate,not_resample])
    X = train_df.drop(columns='Class')
    y = train_df[['Class']]
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state = 123)
    

    #fit and predict using decision tree classifer and gridCV to find best max_depth hyperparameter
    model = DecisionTreeClassifier()
    param_grid = {'max_depth': list(range(2,15))}
    CV = GridSearchCV(model, param_grid, cv = 10, refit=True)          
    CV.fit(X_train, y_train)
    d = {'Best_max_depth':[CV.best_params_['max_depth']], 
         'Best_CV_Score':[CV.best_score_], 
         'Training_Error':[1 - CV.score(X_train, y_train)], 
         'Validation_Error':[1 - CV.score(X_valid, y_valid)]}
    model_score = pd.DataFrame(d)

    #write to csv
    model_score.to_csv("%s/analysis_result.csv" % local_path)
    
  
if __name__ == "__main__":
    main(opt["--train_data"],opt["--local_path"])