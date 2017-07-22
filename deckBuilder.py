import os, sys
from PIL import Image
import glob
import json

def makeSprite(imgs):
    print "%d images will be combine." % len(imgs)

    image_height = 73

    master_width = 450
    #seperate each image with lots of whitespace
    master_height = image_height * len(imgs)
    print "the master image will by %d by %d" % (master_width, master_height)
    print "creating image...",
    master = Image.new(
        mode='RGBA',
        size=(master_width, master_height),
        color=(0,0,0,0))  # fully transparent

    print "created."

    for count, image in enumerate(imgs):
        location = image_height*count
        countImg = Image.open("EternalCardAssets/" + image[1] + ".png")
        cardImg = Image.open(eternalDict[image[0]])
        master.paste(cardImg,(0,location))
        master.paste(countImg,(395,location+10))
    print "done adding icons."

    print "saving deck.png...",
    master.save('deck.png')
    print "saved!"


with open('eternalDict.json') as data_file:    
    eternalDict = json.load(data_file)

f = open('testDeck.txt', 'r')

assets = []

for card in f:
    c1 = card.split(' (')[0]
    cnt = c1.split(' ')[0]
    cardName = " ".join(c1.split(' ')[1:])
    assets.append((cardName, cnt))

makeSprite(assets)