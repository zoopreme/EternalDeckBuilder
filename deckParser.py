import os, sys
from PIL import Image
import glob
import json

with open('eternalDict.json') as data_file:    
    eternalDict = json.load(data_file)

f = open('testDeck.txt', 'r')

assets = []

for card in f:
    c1 = card.split(' (')[0]
    cnt = c1.split(' ')[0]
    cardName = " ".join(c1.split(' ')[1:])
    assets.append((cardName, cnt))

