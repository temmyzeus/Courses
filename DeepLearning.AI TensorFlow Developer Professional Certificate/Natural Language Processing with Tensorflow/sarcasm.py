import os
import ast
from pprint import pprint

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

os.chdir('DeepLearning.AI TensorFlow Developer Professional Certificate/Natural Language Processing with Tensorflow')
with open('./Sarcasm_Headlines_Dataset.json', mode='r') as f:
    data = f.readlines()

article_links: list = []
is_sarcastic: list = []
headlines: list = []

for line in data:
    line = ast.literal_eval(line)
    article_links.append(line['article_link'])
    is_sarcastic.append(line['is_sarcastic'])
    headlines.append(line['headline'])

tokenizer = Tokenizer(
    num_words=None,
    oov_token='<UNK>'
)
tokenizer.fit_on_texts(headlines)

# Print Ordered Dict of Word Counts or Frequency
print(tokenizer.word_counts, end='\n\n')

# Number of docs tokens appeared in
print(tokenizer.word_counts, end='\n\n')

# Word Indeces, index is used to represent the word
print(tokenizer.word_index, end='\n\n')

pprint(headlines[:3])
enc_tokens = tokenizer.texts_to_sequences(headlines[:3])
pprint(enc_tokens)
