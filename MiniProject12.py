import pandas as pd 
import snscrape.modules.twitter as twit 

query = '(from:elonmusk) until:2023-07-20 since:2023-03-20'
tweets = []
limit = 100

for tweet in twit.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) ==  limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username,tweet.content])
df = pd.DataFrame(tweets, columns=['Date','User','Tweet'])
print(df)