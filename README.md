# Spacy Movie Recommender
This python script uses the spaCy library to analyse a movie description against a list of movie descriptions and based on the 
similarity in descriptions will recommend the next movie to watch.

## Requirements
* Python 3.x
* spaCy 3.x

## Getting Started 
To get started with this project, follow these steps:

* Clone this repository
* Build the Docker image: docker build -t myproject .
* Run the Docker container: docker run -it --rm myproject
* Run the script by typing python garden.py and pressing enter in the console

## Installation
* Run the requirements.txt file 
OR 
* Install Python 3.x from the official website
* Install spaCy by running pip install spacy on your terminal or command prompt
* Download the en_core_web_md model for spaCy by running python -m spacy download en_core_web_md

## Usage
* Clone or download the code from this repository
* Open a terminal or command prompt and navigate to the directory where the code is located
* Run the script by typing python watch_next.py and pressing enter
* The script will print the recommended movie title