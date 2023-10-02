import os
import random
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(203, 60%%, %d%%)" % random.randint(60, 100)

with open('cleantext.txt', 'r') as text_file:
    text = text_file.read()

mapArg = np.array(Image.open("arg.jpg"))

mapMask = mapArg.copy()

mapMask[mapMask.sum(axis=2) == 0] = 255

wc = WordCloud(width=1200, height=1200, max_words=3000, 
    mask=mapMask, max_font_size=20, random_state=42, 
    relative_scaling=0.3, collocations=False, margin=2).generate(text)

image_colors = ImageColorGenerator(mapArg)
wc.recolor(color_func=grey_color_func, random_state=3)
wc.to_file("wordCloud.png")