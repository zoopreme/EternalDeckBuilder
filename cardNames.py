import json
import os
from pprint import pprint

f = open ("eternalDic.txt", "r")

cardDic = {}

for line in f:
    key = line.rstrip()
    cardDic[key] = "EternalCardAssets/" + key + ".png"

f.close()

with open("eternalDict.json", "w") as fp:
    json.dump(cardDic, fp)


