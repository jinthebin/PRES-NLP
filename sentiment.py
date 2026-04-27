from spacytextblob.spacytextblob import SpacyTextBlob
import spacy

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
'''
Author: Abhinav Jindal


This program performs sentiment analysis on a dataframe and returns the 
dataframe with new columns for sentiment score, sentiment label

It uses spacytextblob instead of asent - which was dropped due to 
complexity of doc structure

currently using the smaller en_core_web_sm embedding model

'''

def sentiment_analysis(df, text_col):
    sentiment_score = []
    sentiment_label = []

    for index, row in df.iterrows():
        doc = nlp(row[text_col])
        sentiment = doc._.blob.polarity
        sentiment = round(sentiment,2)

        if sentiment > 0:
            sent_label = "Positive"
        elif sentiment == 0:
            sent_label = "Neutral"
        else:
            sent_label = "Negative"


        sentiment_label.append(sent_label)
        sentiment_score.append(sentiment)
    df["Sentiment Score"] = sentiment_score
    df["Sentiment Label"] = sentiment_label
    return df