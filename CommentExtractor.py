import praw, re
from collections import Counter

# Removes emojis from IDLE output
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

# Pulls Reddit credentials from locally stored file
raw_credentials = open('Reddit_Creds.txt')
listed_credentials = []
for string in raw_credentials:
    listed_credentials.append(string.rstrip())

# Credentials to access Reddit API
reddit = praw.Reddit(client_id=listed_credentials[0],
                     client_secret=listed_credentials[1],
                     user_agent=listed_credentials[2])

# Testing whether access is read only - not used currently
# print(reddit.read_only)

# Selects the reddit thread - this is a short one as a test
submission = reddit.submission(id='ablzh6')

# Prints number of comments in thread (reference for now - to be deleted_
print(submission.num_comments) 

# Prints all top level comments in thread - not used currently
# submission.comments.replace_more(limit=None) 
# for top_level_comment in submission.comments:
#    print(BMP(top_level_comment.body))

# Ticker dictionary - creates a ticker dictionary to be counted, pulling from a txt file.
raw_tickers = open('tickers.txt')
tickers = []
for string in raw_tickers:
    tickers.append(string.rstrip())

# Ticker counter - creates a list to store the count for each of the items in the ticker dictionary
# Stores the value of zero in each item of the list.
number_of_tickers = len(tickers)
tickerCount = []
j = 0
while j < len(tickers):
    tickerCount.append(0)
    j = j +1 

# Extracts all the comments out of the thread using Reddit API
submission.comments.replace_more(limit=None)

# Starts a loop to extract each comment one by one from the Reddit API
for comment in submission.comments.list():

    i = 0 # Resets i to zero at the start of every comment read
    print(BMP(comment.body)) # For testing, to be deleted

    while i < number_of_tickers: # Loop through each item in the ticker dictionary
        if tickers[i] in comment.body:
            tickerCount[i] = tickerCount[i] + 1
        i = i + 1

    print(tickerCount) # To be deleted


