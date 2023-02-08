# RPA_Challenge_NY
This project scraps the new york times website which is https://nytimes.com to get data of the news, apply filters to search specific news.
## Requirements
- python version 3.10.5
## First steps
> python -m venv venv

### For Linux
> source ./venv/bin/activate

### For Windows
> .\venv\Scripts\activate

### Then
> pip install --upgrade pip

> pip install -r requirements.txt

## Configuration
In the **main.py** file you have three variables.

**words** phrase that will be use to search

**categories** is a list of the sections to filter, the available options are: *Any, Arts, Books, Magazine, Movies, New York, Opinion, Theater, U.S., World*

**number_of_months** the number of months to search the news. 0 - 1 is for news of the current month, 2 for news since the last month and so on and so forth.

## Run

To execute the script
> python main.py

To run tests
> python -m unittest ./tests/test_dollar_pattern.py