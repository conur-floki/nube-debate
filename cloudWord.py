import os
from wordcloud import WordCloud, ImageColorGenerator
from unidecode import unidecode
from PIL import Image
import numpy as np

def custom_filter(word):
    return any(caracter.isdigit() for caracter in word) or len(word) < 4

with open('texto.txt', 'r') as text_file:
    text = text_file.read()

with open('filterDict.txt', 'r') as text_file:
    wordsToFilter = [linea.strip() for linea in text_file]

words = text.split()

filteredWords = [word for word in words if word.lower().strip()
                not in [w.lower().strip() for w in wordsToFilter]
                and not custom_filter(word)]

text = ' '.join(filteredWords)

text = unidecode(text).lower()

mapArg = np.array(Image.open("arg.jpg"))

mapMask = mapArg.copy()

mapMask[mapMask.sum(axis=2) == 0] = 255

wc = WordCloud(width=1200, height=1200, max_words=3000, mask=mapMask, max_font_size=40, random_state=42, relative_scaling=0.3, collocations=False, margin=2)

wc.generate(text)
image_colors = ImageColorGenerator(mapArg)
wc.recolor(color_func=image_colors)
wc.to_file("wordCloud.png")