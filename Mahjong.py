# coding: UTF-8
import settings
import tweepy
import random
from PIL import Image

'''
#-----------------------------------------------------------------------------
# keyの指定(情報漏洩を防ぐため伏せています)
consumer_key = settings.CK
consumer_secret = settings.CS
access_token = settings.AT
access_token_secret = settings.ATC

# tweepyの設定（認証情報を設定）
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepyの設定（APIインスタンスの作成）
api = tweepy.API(auth)

#-----------------------------------------------------------------------------
'''
def oya():
    tile1 = chr(random.randint(65, 68))
    if tile1 == 'D':
        tile2 = str(random.randrange(1, 7))
    else:
        tile2 = str(random.randrange(1, 9))
        if tile2 == '5' and random.randint(0, 1) == 1 and l.count(tile1 + '6!') == 0:
            tile2 = '6!'
    global tile
    tile = tile1 + tile2 + '.png'


l = []
num = 0
while num < 14:
    oya()
    if l.count(tile) < 4:
        l.append(tile)
        num += 1
print(sorted(l))
while num < 15:
    oya()
    if l.count(tile) < 4:
        dora = tile
        num += 1
print(dora)

back = Image.open('./images/background.png')
img1 = back.copy()
x = 0
img1.save('./images/upload.png', quality=95)
for i in l:
    img1 = Image.open('./images/upload.png')
    img2 = Image.open('./images/' + i)
    size = (round(img2.width * 0.25), round(img2.height * 0.25))
    img2 = img2.resize(size)
    img1.paste(img2, (x, 50))
    img1.save('./images/upload.png', quality=95)
    x += 60
    