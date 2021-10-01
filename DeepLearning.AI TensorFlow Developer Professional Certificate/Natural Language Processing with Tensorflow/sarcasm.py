import ast

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