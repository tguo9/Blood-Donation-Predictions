# authors: DSCI 522 Group 305 
# date: 2020-01-22

"""
This script pre-processes the data from the following data: 
Writes the training and test data to 2 separate csv files 

Usage: src/pre_process_data.py --raw_data=<raw_data> --local_path=<local_path>

Options:
--raw_data=<raw_data>      Local path to the raw data csv file (include file name)
--local_path=<local_path>  Local path to folder you want the csv files to be written to 
"""

import pandas as pd
from docopt import docopt
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(raw_data, local_path):
    # in console type: python src/pre_process_data.py --raw_data=./data/raw/raw_data.csv --local_path=./data/processed
    
    #convert to pandas data frame
    blood_df = pd.read_csv(raw_data, index_col=0)
    X = blood_df.iloc[:,0:-1]
    y = blood_df.iloc[:,-1]

    #test that X has same number of columns as there are features (4)
    assert len(X.columns) == 4
    #test that y is a series (1 column only)
    assert isinstance(y, pd.Series)

    # split training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 123)

    blood_df_train = X_train
    blood_df_train = pd.merge(blood_df_train, y_train, left_index=True, right_index=True)

    blood_df_test = X_test
    blood_df_test = pd.merge(blood_df_test, y_test, left_index=True, right_index=True)

    #test that Class (target) values are only 1 or 2
    assert blood_df_train['Class'].isin([1, 2]).all()
    assert blood_df_test['Class'].isin([1, 2]).all()

    # rename columns 
    blood_df_train = blood_df_train.rename(columns={"V1": "since_last_don", "V2": "total_dons", "V3": "total_blood", "V4": "since_first_don"})
    blood_df_test = blood_df_test.rename(columns={"V1": "since_last_don", "V2": "total_dons", "V3": "total_blood", "V4": "since_first_don"})

    #write to csv
    blood_df_train.to_csv("%s/train_data.csv" % local_path)
    blood_df_test.to_csv("%s/test_data.csv" % local_path)


if __name__ == "__main__":
    main(opt["--raw_data"], opt["--local_path"])