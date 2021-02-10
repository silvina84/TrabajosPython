#ChatBot
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer
import numpy
import tflearn
import tensorflow
import json
import random
import pickle

nltk.download('punkt')

with open("Contenido.json") as archivo:
    datos = json.load(archivo)


print(datos)    
