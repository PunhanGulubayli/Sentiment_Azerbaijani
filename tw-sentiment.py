'''from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tweet = 'İ am really excited to go to Paris'

# precprcess tweet
tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    
    elif word.startswith('http'):
        word = "http"
    tweet_words.append(word)

tweet_proc = " ".join(tweet_words)

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
# output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)

for i in range(len(scores)):
    
    l = labels[i]
    s = scores[i]
    print(l,s)
'''
'''
#-*- coding: utf-8 -*-

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from deep_translator import GoogleTranslator
import torch

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

while True:
    tweet = input("Mətni daxil edin (bitirmək üçün 'Son' yazın): ")
    if tweet.strip().lower() == "son":
        print("Proqram dayandırıldı.")
        break

    # translate Azerbaijani → English
    translated_text = GoogleTranslator(source="az", target="en").translate(tweet)
    print(f"🔄 Tərcümə olunmuş mətn: {translated_text}")

    # preprocess
    tweet_words = []
    for word in translated_text.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    print("📊 Sentiment nəticələri:")
    for i in range(len(scores)):
        l = labels[i]
        s = scores[i]
        print(f"{l}: {s:.4f}")
    print("-" * 40)'''

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from deep_translator import GoogleTranslator
import torch

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

def analyze_text(tweet: str):
    # translate Azerbaijani → English
    translated_text = GoogleTranslator(source="az", target="en").translate(tweet)

    # preprocess
    tweet_words = []
    for word in translated_text.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # nəticə dict formatında qaytar
    result = {labels[i]: float(scores[i]) for i in range(len(scores))}
    return translated_text, result

