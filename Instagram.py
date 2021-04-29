# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


text = open('most.csv').read()
wordcloud = WordCloud().generate(text)
# Generate plot
plt.imshow(wordcloud)
plt.axis("off")
plt.show()