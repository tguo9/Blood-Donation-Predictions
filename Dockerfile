FROM continuumio/anaconda3

# Install R
RUN apt-get update
RUN apt-get install r-base r-base-dev -y

RUN conda install pandas
RUN conda install warnings
RUN conda install scikit-learn
RUN conda install numpy
RUN conda install datapackage
RUN conda install requests

RUN /opt/conda/bin/conda install -y -c anaconda docopt

# Install R Packages
RUN Rscript -e "install.packages('tidyverse')"
RUN Rscript -e "install.packages('knitr')"
RUN Rscript -e "install.packages('docopt')"
RUN Rscript -e "install.packages('ggplot2')"

# Put Anaconda Python in PATH
ENV PATH="/opt/conda/bin:${PATH}"

CMD ["/bin/bash"]