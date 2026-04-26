import spacy
import asent

#converted to work on dataframe using pipe function -- AJ 

# load spacy pipeline
nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

# add the rule-based sentiment model
nlp.add_pipe('asent_en_v1')

all_visualizations = []
# print polarity of document, scaled to be between -1, and 1
def sentiment_analysis(text):
    for doc in nlp.pipe(text):
        # print(doc._.polarity)
        viz_html = asent.visualize(doc, style='prediction')
        all_visualizations.append(viz_html)