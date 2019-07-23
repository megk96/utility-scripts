import json
import os
import re
import operator
import urllib.request
import random
import validators
os.chdir('/home/meg')
with open('condition_image.json') as f:
    data = json.load(f)
print(len(data))
condition_images = {}
for d in data:
    conditions = d['conditions'].replace('{', '')
    conditions = conditions.replace('}', '')
    conditions = [int(s) for s in conditions.split(',')]
    images = []
    responses = d['responses']
    responses = json.loads(responses)

    for r in responses:

        if r["type"] == "file_url":
            if "face" in r["question"]:
                images.append(r["answer"])
    for c in conditions:
        if c not in condition_images:
            condition_images[c] = images

        else:
            condition_images[c] = condition_images[c] + images


with open('images_classified.json', 'w') as outfile:
    json.dump(condition_images, outfile)
listt = [2,3,4,5,6,7,8]



condition_key = {}
with open('condition_key.json') as f:
    data = json.load(f)
    for d in data:
        condition_key[d['id']] = d['key']

nums = {}
with open('images_classified.json') as f:
    data = json.load(f)
    for key, value in data.items():

        if int(key) in listt:
            nums[condition_key[int(key)]] = len(value)
            random.shuffle(value)
            for i, v in enumerate(value):
                LIMIT = 10
                if not validators.url(v):
                    LIMIT += 1
                    continue
                if i < LIMIT:
                    print(v)
                    #urllib.request.urlretrieve(v, "acne_images/%s_%d.jpg" % (condition_key[int(key)], i))






    nums = sorted(nums.items(), key=operator.itemgetter(1), reverse=True)
    print(nums)


