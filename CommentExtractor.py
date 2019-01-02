import praw, re, csv

# Removes emojis from IDLE output
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

# Pulls Reddit credentials from locally stored file
print('Logging into Reddit...') # To be deleted.
raw_credentials = open('Reddit_Creds.txt')
listed_credentials = []
for string in raw_credentials:
    listed_credentials.append(string.rstrip())

# Credentials to access Reddit API
reddit = praw.Reddit(client_id=listed_credentials[0],
                     client_secret=listed_credentials[1],
                     user_agent=listed_credentials[2])

# Selects the reddit thread - this is a short one as a test
submission = reddit.submission(id='ablzh6')
print('Done') # To be deleted.

# Ticker dictionary - creates a ticker dictionary to be counted, pulling from a CSV file.
print('Selecting tickers from dictionary...') # To be deleted.
raw_tickers = open('tickers.csv')
tickers_reader = csv.reader(raw_tickers)
tickers = list(tickers_reader)

# Ticker counter - creates a list to store the count for each of the items in the ticker dictionary
# Stores the value of zero in each item of the list.
number_of_tickers = len(tickers)
tickerCount = []
j = 0
while j < len(tickers):
    tickerCount.append(0)
    j = j +1 
print('Done') # To be deleted.

# Extracts all the comments out of the thread using Reddit API
print('Extracting comments from thread...') # To be deleted.
submission.comments.replace_more(limit=None)

# Starts a loop to extract each comment one by one from the Reddit API
for comment in submission.comments.list():

    i = 0 # Resets i to zero at the start of every comment read
    # print(BMP(comment.body)) # For testing, to be deleted
    
    # Starts a loop through each item in the ticker dictionary
    while i < number_of_tickers: 
        if tickers[i][0] in comment.body:
            tickerCount[i] = tickerCount[i] + 1
        i = i + 1

    # print(tickerCount) # To be deleted
print('Done') # To be deleted.

# Writes both lists to a CSV file.
print('Writing to CSV file...') # To be deleted.
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerows(zip(tickers,tickerCount)) # Need to figure out how to remove quotes
outputFile.close()
print('Done') # To be deleted.
print('------------END--------------') # To be deleted.
