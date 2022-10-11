# importing the required modules.
# import random
import json
import pickle
# import numpy as np
import nltk

# from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
# from keras.layers import Dense, Activation, Dropout
# from keras.optimizers import SGD


def training_model():
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    lemmatizer = WordNetLemmatizer()
    # reading the json.intense file
    intents = json.loads(open("data.json").read())

    # creating empty lists to store data
    words = []
    classes = []
    documents = []
    ignore_letters = ["?", "!", ".", ","]
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # separating words from patterns
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)  # and adding them to words list

            # associating patterns with respective tags
            documents.append(((word_list), intent['tag']))
            # appending the tags to the class list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
            print()
    # storing the root words or lemma
    words = [lemmatizer.lemmatize(word)
             for word in words if word not in ignore_letters]
    words = sorted(set(words))
    print("words", words)
    # saving the words and classes list to binary files
    pickle.dump(words, open('words.pkl', 'wb'))
    pickle.dump(classes, open('classes.pkl', 'wb'))
