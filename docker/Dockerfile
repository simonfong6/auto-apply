FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get upgrade -y

# Install git for development.
RUN apt-get install -y git

# Install vim for debugging.
RUN apt-get install -y vim

# Install wget to download the driver.
RUN apt-get install -y wget

# Install unzip to uncompress the driver.
RUN apt-get install -y unzip

# Install Python 3 and Pip.
RUN apt-get install -y python3.5 \
                       python3-pip

# Install selenium.
RUN pip3 install selenium

# Install chrome webdriver dependencies.
# Some information from https://stackoverflow.com/questions/33382998/chromedriver-various-lib-dependencies-are-missing-on-ubuntu-14-04-64-bit?rq=1
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libnss3
RUN apt-get install -y libx11-6

# Download the chrome web driver and place it in PATH.
RUN wget https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN rm chromedriver_linux64.zip
RUN mv chromedriver /usr/bin

# Install Chrome Browser
# Instructions from https://askubuntu.com/questions/510056/how-to-install-google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable