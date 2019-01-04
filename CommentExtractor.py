import praw, re, csv, os
from operator import add

# Removes emojis from IDLE output
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

# Acesses reddit API
def reddit_creds():
    print('Logging into Reddit...') # To be deleted.
    raw_credentials = open('Reddit_Creds.txt')
    listed_credentials = []
    for string in raw_credentials:
        listed_credentials.append(string.rstrip())
        
    # Credentials to access Reddit API
    reddit = praw.Reddit(client_id=listed_credentials[0],
                         client_secret=listed_credentials[1],
                         user_agent=listed_credentials[2])
    print('Logged in')
    return reddit

def write_to_CSV(matrix):
    outputFile = open('output.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerows(matrix) 
    outputFile.close()

# Searches through WSB threads, finds WAYMT threads, returns submission ids
def search_threads():
    thread_limit = 300
    phrase = 'What Are Your Moves Tomorrow'
    thread_counter = 0
    thread_ids,thread_date = [],[]

    subreddit = reddit.subreddit('wallstreetbets')
    for submission in subreddit.hot(limit=thread_limit):
         
        if phrase in submission.title:
            thread_ids.append(submission.id)
            thread_date.append(submission.created_utc)
            thread_counter = thread_counter + 1
            print(thread_counter," thread(s) found") # To be deleted
            print(BMP(submission.title)) # To be deleted
    
    return(thread_ids)

def initialise_matrix(number_of_threads,
                      number_of_tickers,
                      row_buffer,
                      column_buffer):

    # Initialisation of blank matrix (filled with zeros)
    
    matrix = [[0 for x in range(number_of_threads+column_buffer)]
              for y in range(number_of_tickers+row_buffer)]

    matrix[0][0] = ""

    # Changes the top row of the matrix
    i = 0 
    while i < number_of_threads:
        matrix[0][i+column_buffer] = "ID " + str(i+1)
        i = i + 1

    # Changes left column of the matrix
    i = 0
    while i < number_of_tickers:
        matrix[i+row_buffer][0] = tickers[i]
        i = i + 1
    
    return matrix
    return number_of_tickers
    return number_of_threads

# ------------------- START MAIN --------------------------------

row_buffer,column_buffer = 1,1 # Need to put this somewhere

# Pulls reddit credentials from local folder and accesses API
reddit = reddit_creds()

# Selects the reddit thread - this is a short one as a test
thread_id = search_threads()
number_of_threads = len(thread_id) # Calculates number of threads
print('Number of threads identified: ',number_of_threads)

# Ticker dictionary - creates a ticker dictionary to be counted, pulling from a CSV file.
raw_tickers = open('tickers.csv')
tickers_reader = csv.reader(raw_tickers, delimiter="\t")
tickers = list(tickers_reader)
tickers = [row[0] for row in tickers] # Compresses the CSV input file into one list (instead of a list of lists)
number_of_tickers = len(tickers)

matrix = initialise_matrix(number_of_threads,number_of_tickers,row_buffer,column_buffer)
print('Number of tickers: ',number_of_tickers)
print('Number of threads: ',number_of_threads)

# START OF THEAD LOOP

thread_counter = 1

while thread_counter < number_of_threads + 1:
    submission = reddit.submission(id=thread_id[thread_counter - 1])
    print('Extracting comments from thread number ',thread_counter) # To be deleted.
    submission.comments.replace_more(limit=None)

    comment_loop_counter = 0 # To be deleted

    # Extracts title date and places at top of column
    title = submission.title
    title_date = title.split(', ')[1]
    matrix[0][thread_counter] = title_date

    for comment in submission.comments.list():
        i = 0
        while i < number_of_tickers: # Loops through the tickers
            if tickers[i] in comment.body:
                matrix[i+row_buffer][0+thread_counter] = matrix[i+row_buffer][0+thread_counter] + 1
            i = i + 1

        comment_loop_counter = comment_loop_counter + 1 # To be deleted
        print('Analying comment number ',comment_loop_counter,' in thread number ',thread_counter) # To be deleted

    thread_counter = thread_counter + 1

print(matrix)

# END OF THREAD LOOP

# Writes the two lists to a CSV file
write_to_CSV(matrix)
os.startfile("output.csv")
