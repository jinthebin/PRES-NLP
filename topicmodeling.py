

# Import external libraries: spaCy for tokenization, lemmatization and stopwords
import spacy
from spacy.lang.en import English                 # For other languages, refer to the SpaCy website: https://spacy.io/usage/models
from spacy.lang.en.stop_words import STOP_WORDS   # Also need to update stopwords for other languages (e.g. spacy.lang.uk.stop_words for Ukrainian)

# Import external libraries: gensim to create models and do some additional preprocessing
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Import external libraries: pyLDA for vis
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis



# Print the initial set of stopwords from SpaCy
# Also available at: https://github.com/explosion/spaCy/blob/master/spacy/lang/en/stop_words.py
# print(STOP_WORDS)

# Add a word to remove or add from the list
# STOP_WORDS.add('word') 
# STOP_WORDS.remove('word')

# Lemmatize tokens
def lemmatization(texts, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]):   # Doing part of speech (PoS) tagging helps with lemmatization
    # Load the nlp pipeline, omitting the parser and ner steps of the workflow to conserve computer memory
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"]) # For other languages, use models from step 2
    texts_out = []
    for text in texts: # Run each of the documents through the nlp pipeline
        doc = nlp(text)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    return (texts_out)


# Preprocess texts
def gen_words(texts):
    final = [] # Create an empty list to hold tokens
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc = True) 
        # If working with languages that employ accents, you can set deacc to False
        final.append(new)
    return (final)


def topic_modeling_pipeline(text, num_topics):
    lemmatized_texts = lemmatization(text)
    data_words = gen_words(lemmatized_texts)

    # N-grams
    bigram_phrases = gensim.models.Phrases(data_words, min_count=3, threshold=50)
    trigram_phrases = gensim.models.Phrases(bigram_phrases[data_words], threshold=50)

    bigram = gensim.models.phrases.Phraser(bigram_phrases)
    trigram = gensim.models.phrases.Phraser(trigram_phrases)

    def make_bigrams(texts):
        return [bigram[doc] for doc in texts]

    def make_trigrams(texts):
        return [trigram[bigram[doc]] for doc in texts]

    data_bigrams = make_bigrams(data_words)
    data_bigrams_trigrams = make_trigrams(data_bigrams)

    # Create dictionary of all words in texts
    id2word = corpora.Dictionary(data_bigrams_trigrams)

    # Represent dictionary words as tuples (index, frequency)
    corpus = []
    for text in data_bigrams_trigrams:
        new = id2word.doc2bow(text)
        corpus.append(new)

    # Create LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=num_topics,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,     
                                                # Change chunksize to increase or decrease the length of segments
                                                passes=50,         
                                                # Can do more passes but will increase the time it takes the block to run
                                                alpha="auto")

    # Output visualization
    vis_data = gensimvis.prepare(lda_model, corpus, id2word, R=15, mds='mmds')
    # vis_data
    # pyLDAvis.display(vis_data)
    # pyLDAvis.save_html(vis_data, './topicVis' + str(num_topics) + '.html')
    return vis_data
