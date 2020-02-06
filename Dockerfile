FROM continuumio/anaconda3

# Install R
RUN apt-get update
RUN apt-get install libcurl4-openssl-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install r-base r-base-dev -y

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

# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"

CMD ["/bin/bash"]