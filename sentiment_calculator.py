import csv, os

def initialise_blank_matrix(columns,rows):
    # Creates matrix filled with zeros
    comment_sentiment = [[0 for x in range(columns)]
                         for y in range(rows)]
    return comment_sentiment

def import_from_CSV(filename):
   import_list = open(filename, encoding="utf8")
   import_reader = csv.reader(import_list, delimiter="\t")
   import_list = list(import_reader)
   import_list = [row[0] for row in import_list]
   return import_list

def write_to_CSV(matrix,output_file):
    outputFile = open(output_file, 'w', newline='', encoding='utf-8')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerows(matrix) 
    outputFile.close()

# Imports comments from csv file into list
comments = import_from_CSV('comment_input.csv')
number_of_comments = len(comments)

# Imports bearish and bullish keywords from csv file into list
keywords_bullish = import_from_CSV('keywords_bullish.csv')
number_of_keywords_bullish = len(keywords_bullish)
keywords_bearish = import_from_CSV('keywords_bearish.csv')
number_of_keywords_bearish = len(keywords_bearish)

# Initialises blank matrix to hold comment sentiment
comment_sentiment = initialise_blank_matrix(2,number_of_comments)

# Changes left column of the matrix (inserts comment)
# This is for presentatio purposes - so i can review output / accuracy of sentiment
i = 0
while i < number_of_comments:
    comment_sentiment[i][0] = comments[i]
    i = i + 1

overall_sentiment = 0

j = 0
while j < number_of_comments:
    print("Checking comment...")
    
    # Bullish indicator loop
    i = 0
    while i < number_of_keywords_bullish: # Loops through the keywords
        if keywords_bullish[i] in comments[j]:
            print('Found the keyword "',keywords_bullish[i],'" in comment: ',comments[j])
            comment_sentiment[j][1] = comment_sentiment[j][1] + 1
            overall_sentiment = overall_sentiment + 1
        i = i + 1

    # Bearish indicator loop
    i = 0
    while i < number_of_keywords_bearish: # Loops through the keywords
        if keywords_bearish[i] in comments[j]:
            print('Found the keyword "',keywords_bearish[i],'" in comment: ',comments[j])
            comment_sentiment[j][1] = comment_sentiment[j][1] - 1
            overall_sentiment = overall_sentiment - 1
        i = i + 1

    j = j + 1

print('Overall sentiment: ',overall_sentiment)

write_to_CSV(comment_sentiment,'comment_output.csv')
os.startfile("comment_output.csv")
