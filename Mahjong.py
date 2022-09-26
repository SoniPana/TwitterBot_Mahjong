# coding: UTF-8
import settings
import tweepy
import random
import numpy as np

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
    global tile
    tile = tile1 + tile2


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