# Docker file for the group 305 project
# Group 305, Jan, 2020

# use continuumio/anaconda3 as the base image and
FROM continuumio/anaconda3

# Install R
RUN apt-get update
RUN apt-get install libcurl4-openssl-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install r-base r-base-dev -y

# Install the python packages
RUN conda install pandas
RUN conda install scikit-learn
RUN conda install numpy
RUN pip install datapackage
RUN conda install requests
RUN conda install docopt

# Install R Packages
RUN Rscript -e "install.packages('tidyverse')"
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('reticulate')"
RUN Rscript -e "install.packages('kableExtra')"

# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"

CMD ["/bin/bash"]