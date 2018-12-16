# wsb_scraper
Scraping tool for WSB

Tool aims to have the following functionality.

1. Initial stage (scraping)

  - Open the daily WSB discussion thread
  - Search for and count the number of mentions for stock tickers
  - Search for and count the option place for each stock ticket (if one is mentioned alongside the stock)
  - Search for and count mentions of "buy" and "sell" for stock tickers and option types (if one is mentioned alongside the stock)
  - Conduct analysis to determine an overall "sentiment" for that day
  
2. Testing stage (testing of sentiment)

  - Extract the daily stock price movement for each of the relevant stock tickers for that day, including other relevant metrics (such as volatility, etc)
  - Produce a dataset over which regression analysis can be applied, comparing daily stock price movement to overall sentiment
  - Running of testing over the historical period
  
3. Automation stage (giving the progam power to make investment decisions)

  - Development of a decision making process, so that the program, once scraping and testing is complete, can make a go/no-go decision
  - Connecting to interactive brokers (paper money first)
  - Automation of trading process based on WSB sentiment
