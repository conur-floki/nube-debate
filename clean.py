import re
from unidecode import unidecode

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

text = re.sub(r'[¿!¡;,:\.\?#@()+-="]',
        "",
        text)

with open('cleanText.txt', 'w') as text_file:
    text_file.write(text)