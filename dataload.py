import pandas as pd


raw_data = pd.read_csv(r'yelp_sentiment_master_dataset.csv')
raw_data['Text'] = raw_data['Text'].fillna('N/A')
raw_data['Text'] = raw_data['Text'].astype(str)

test_data = raw_data.sample(100)
test_data['Text'] = test_data['Text'].fillna('N/A')
test_data['Text'] = test_data['Text'].astype(str)

'''
sentiment_data = pd.read_csv(r"C:\Users\busaji\CODERepository\NLP-app\.dat\sentiment_data.csv")

 site_data = pd.read_csv(r"C:\Users\busaji\CODERepository\NLP-app\.dat\site_data.csv")

sentiment_temp = pd.merge(left=sentiment_data,
                                 right=site_data,
                                 left_on="Site ID",
                                 right_on="SiteCode", how='left')

sentiment_data_merged = pd.merge(left=sentiment_temp,
                                 right=site_data,
                                 left_on="Site ID",
                                 right_on="Name", how='left')
'''