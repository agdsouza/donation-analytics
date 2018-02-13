# Introduction

My submission for the Insight Data Engineering Coding Challenge

# Implementation

For this challenge, I created 3 classes to process incoming data.

`DataInitializer` receives raw data from the Federal Election Commission in the form of a text file, itcont.txt, and a percentile in a text file, percentile.txt, where it filters out any data with empty required fields such as NAME, ZIP_CODE, etc. It also finds all non-repeat donors, puts them in a set, and
iterates through the data set, removing those non-repeats.

`DataCalculator` receives the cleaned and filtered data and iterates through each entry in order, calculating the sum of all transactions, percentiles, and number of repeats for a specific candidate, zip code, and donation year, returning a list of dictionaries of each repeat entry representing these calculations, where it will be ready for output.

`DataOutputer` receives a list of dictionaries, each representing the data that will be printed on each line of the output file. The dictionary key-value pairs are delimited with a "|" character, and finally placed in an output txt file, repeat_donors.txt.

`donation-analytics.py` runs a Python script that implements each of the above classes, forming the names of the input and output files to be used within those classes.

# Source Files and Required Dependencies

## Source files:

* donation-analytics.py
* data_initializer.py
* data_calculator.py
* data_outputer.py

## Dependencies

No development dependencies were used for this project; it can be run without installing prior libraries on Python 3.

# Run Instructions

From the `donation-analytics` directory, run `run.sh` on any Linux machine. Note that the project will only run on Python 3, and the script itself does not use the arguments within the shell to find the files; all files are located within the `donation-analytics.py` file itself.

The file must be run from the above directory in order to work, otherwise a "no such file or directory" error will occur.