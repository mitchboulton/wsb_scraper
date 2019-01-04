import csv, os
from operator import add

row_buffer,column_buffer = 1,1

# Initialisation of blank matrix (filled with zeros)
no_of_threads, no_of_tickers = 9, 8;
matrix = [[0 for x in range(no_of_threads+column_buffer)]
          for y in range(no_of_tickers+row_buffer)]

# Placeholder for tickers, will need to connect to actual list
tickers =['SPY','VIX','AAPP','SQ',"VXX","SPX","GOOG","MYR"]

matrix[0][0] = ""

# Changes the top row of the matrix
i = 0 
while i < no_of_threads:
    matrix[0][i+column_buffer] = "ID " + str(i+1)
    i = i + 1

# Changes left column of the matrix
i = 0
while i < no_of_tickers:
    matrix[i+row_buffer][0] = tickers[i]
    i = i + 1

print(matrix)

outputFile = open('testy.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerows(matrix) 
outputFile.close()

os.startfile("testy.csv")

