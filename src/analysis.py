# authors: DSCI 522 Group 305 
# date: 2020-01-22

"""
This script read in the data processed by pre-process.py and apply decision tree algorithm

Usage: src/analysis.py --train_data=<train_data> --test_data=<test_data> --local_path=<local_path>

Options:
--train_data=<train_data>  Local path to the training data csv file (include file name)
--test_data=<test_data>  Local path to the training data csv file (include file name)
--local_path=<local_path>  Local path to folder you want the analysis files to be written to 
"""

import pandas as pd
from docopt import docopt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

opt = docopt(__doc__)

def main(train_data, test_data, local_path):
    # in console type: python src/analysis.py --train_data=./data/processed/train_data.csv --test_data=./data/processed/test_data.csv --local_path=./results
    
    #convert to pandas data frame
    train_df = pd.read_csv(train_data)
    test_df = pd.read_csv(test_data)
    X_train = train_df.drop(columns='Class')
    y_train = train_df[['Class']]
    X_test = test_df.drop(columns='Class')
    y_test = test_df[['Class']]

    #fit and predict using decision tree classifer
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    model_test_score = pd.DataFrame(cross_val_score(model, X_test, y_test, cv=10))
    

    #write to csv
    model_test_score.to_csv("%s/analysis_result.csv" % local_path)
    
  
if __name__ == "__main__":
    main(opt["--train_data"], opt["--test_data"],opt["--local_path"])