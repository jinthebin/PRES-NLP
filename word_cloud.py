from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64

# Define a function to update the word cloud image
def update_word_cloud(df, text_col):
    text = ' '.join(df[text_col])
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('word_cloud.png', bbox_inches='tight')
    with open('word_cloud.png', 'rb') as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return 'data:image/png;base64,{}'.format(encoded_image)


