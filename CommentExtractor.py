import praw, re
from collections import Counter

# Removes emojis from IDLE output
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

# Finds whole word - not used currently, will need to be deleted later if not used
# def findWholeWord(w):
#    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

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
submission = reddit.submission(id='ab5h45')

# Prints number of comments in thread (reference for now - to be deleted_
print(submission.num_comments) 

# Prints all top level comments in thread - not used currently
# submission.comments.replace_more(limit=None) 
# for top_level_comment in submission.comments:
#    print(BMP(top_level_comment.body))

# Creates a dictionary for tickers - will need to be developed further
tickers = ['SPX','VIX']
tickerCount = [0,0]
number_of_tickers = len(tickers)

# Until the dictionary is completed and integrated, using hardcoded SPX to test.
SPX = 0
word = 'SPX'

# Prints all comments in thread
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    i = 0 # Resets i to zero at the start of every comment read
    print(BMP(comment.body)) # For testing, to be deleted
    # Searches for SPX in the comment body, needs to be hooked into a dictionary. Next step to be completed.
    print('Number of tickers: ',number_of_tickers)
    while i < number_of_tickers:
        if tickers[i] in comment.body:
            tickerCount[i] = tickerCount[i] + 1
            print('----------------------------------------------')
        i = i + 1
        print('Current value of i: ',i)
    print('Current value of i: ',i)
    print(tickerCount)


