import pandas as pd


raw_data = pd.read_csv(r'C:\Users\busaji\CODERepository\NLP-app\PRES-NLP\raw_data.csv')
raw_data['Text'] = raw_data['Text'].fillna('N/A')
raw_data['Text'] = raw_data['Text'].astype(str)

test_data = raw_data.sample(100)
test_data['Text'] = test_data['Text'].fillna('N/A')
test_data['Text'] = test_data['Text'].astype(str)

sentiment_data = pd.read_csv(r"C:\Users\busaji\CODERepository\NLP-app\.dat\sentiment_data.csv")