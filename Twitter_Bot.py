# coding: UTF-8
import settings
import tweepy
import random


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
###z = np.random.choice(['麻', '雀', '部', '設', '立', '部', '同', '好', '会'])
text_li = ['麻雀部', '設立部', '同好会']
li = []
for l in text_li:
    for i in range(3):
        li.append(random.choice(l))
li = ''.join(li) + '(非公式)'
print(li)

api.update_status(status=li)
