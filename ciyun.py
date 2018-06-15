from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

text = open(path.join(d, 'cipin.txt')).read()

img_mask = np.array(Image.open(path.join(d, "img.png")))

stopwords = set(STOPWORDS)
stopwords.add("一夜")

wc = WordCloud(width=1000, background_color="white", max_words=2000, mask=img_mask, stopwords=stopwords, font_path='ziti.ttf', random_state=42)
wc.generate(text)

image_colors = ImageColorGenerator(img_mask)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()

wc.to_file(path.join(d, "ciyun.png"))