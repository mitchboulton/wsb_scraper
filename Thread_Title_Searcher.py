import praw

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

thread_limit = 1000
phrase = 'What Are Your Moves Tomorrow'
thread_counter = 0

subreddit = reddit.subreddit('wallstreetbets')
for submission in subreddit.hot(limit=thread_limit):
    print(BMP(submission.title))
 
    if phrase in submission.title:
        thread_counter = thread_counter + 1

    print(thread_counter)
