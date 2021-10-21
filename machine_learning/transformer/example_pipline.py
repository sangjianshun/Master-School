from transformers import pipeline
import torch

# 1. sentiment-analysis
# Allocate a pipeline for sentiment-analysis
# classifier = pipeline('sentiment-analysis')
# print(classifier('我不喜欢'))
# [{'label': 'POSITIVE', 'score': 0.9996980428695679}]

# # 1.1 上面等价于下面：
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# # 1.2 question-answering
# # Allocate a pipeline for question-answering
# question_answerer = pipeline('question-answering')
# res = question_answerer({
# 'question': 'What is the name of the repository ?',
# 'context': 'Pipeline has been included in the huggingface/transformers repository'
# })
# print(res)
# print(1)


# 2. mask机制展示
# from pprint import pprint
# unmasker = pipeline("fill-mask")
# pprint(unmasker(f"HuggingFace is creating a {unmasker.tokenizer.mask_token} that the community uses to solve NLP tasks."))


# # 3. 载入bert模型
# from transformers import BertTokenizer
# bt = BertTokenizer.from_pretrained('bert-base-uncased')
# a = bt('I like natural language progressing!')


# 4. 自动识别模型
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
model = AutoModel.from_pretrained('bert-base-chinese')

# 5. 展示encode模型
b = tokenizer("春眠不觉晓")
input_ids_b = b["input_ids"]
input_ids = tokenizer.encode('春眠不觉晓', return_tensors='pt')

# 5.1 tokenizer
## 一个示例
# 参数, padding, max_length 截断长度
pt_batch = tokenizer(
    ["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."],
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt"
)

# 6. 正向传播
logits = model.forward(input_ids, output_hidden_states = True)
# last_hidden_state = logits.last_hidden_state  # shape (1, 7, 768)
# hidden_state = logits.hidden_state  # list shape [(1, 7, 768) * 13]
# v = torch.mean(last_hidden_state, dim=1)


# 7. 展示文本相似度的计算
import numpy as np

def sentence_embedding(sentence):
    input_ids = tokenizer.encode(sentence, return_tensors='pt')
    logits = model.forward(input_ids) # shape (1, 7, 768)
    last_hidden_state = logits.last_hidden_state
    v = torch.mean(last_hidden_state, dim=1)
    return v

sentences = ['春眠不觉晓','大梦谁先觉','浓睡不消残酒','东临碣石以观沧海']

# vs = [sentence_embedding(sentence).numpy() for sentence in sentences]
vs = [sentence_embedding(sentence).detach().numpy() for sentence in sentences]
nvs = [v / np.linalg.norm(v) for v in vs] # normalize each vector
m = np.array(nvs).squeeze(1) # shape (4, 768)
print(np.around(m @ m.T, decimals=2))

with torch.no_grad():
    vs = [sentence_embedding(sentence).numpy() for sentence in sentences]
    nvs = [v / np.linalg.norm(v) for v in vs] # normalize each vector
    m = np.array(nvs).squeeze(1) # shape (4, 768)
    print(np.around(m @ m.T, decimals=2))

print(1)
