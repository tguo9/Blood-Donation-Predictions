# blood donation data pipe
# author: Group 305
# date: 2020-01-30

all: results/since_last_don.png results/total_blood.png results/total_dons.png results/analysis_result.csv results/analysis_confusion.csv doc/report.md doc/report.html

# download data
data/raw/raw_data.csv: src/load_blood_donor_data.py
	python src/load_blood_donor_data.py --data_url='https://datahub.io/machine-learning/blood-transfusion-service-center/datapackage.json' --local_path=data/raw/raw_data.csv

# pre-process data (e.g., scale and split into train & test)
data/processed/train_data.csv data/processed/test_data.csv: src/pre_process_data.py data/raw/raw_data.csv
	python src/pre_process_data.py --raw_data=data/raw/raw_data.csv --local_path=data/processed

# exploratory data analysis - graphs
results/since_last_don.png results/total_blood.png results/total_dons.png: src/plot.R data/processed/train_data.csv
	Rscript src/plot.R --file_path=data/processed/train_data.csv --out_dir=results/

# get model results
results/analysis_result.csv results/analysis_confusion.csv: src/analysis.py data/processed/train_data.csv
	python src/analysis.py --train_data=data/processed/train_data.csv --local_path=results

# generate report
doc/report.md doc/report.html: doc/report.Rmd
	Rscript -e "rmarkdown::render('doc/report.Rmd')"

# clean the result
clean: 
	rm -rf data/raw/*
	rm -rf data/processed/*
	rm -rf results/*
	rm -rf doc/report.md
	rm -rf doc/report.html