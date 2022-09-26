# coding: UTF-8
import settings
import tweepy
import random
from PIL import Image


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
# 牌決め
def haipai():
    # 萬子、筒子、索子、字牌決め
    tile1 = chr(random.randint(65, 68))
    # 字牌の場合は7種類のどれか
    if tile1 == 'D':
        tile2 = str(random.randrange(1, 7))
    else:
        tile2 = str(random.randrange(1, 9))
        # 赤ドラ抽選(既にある場合は除外)
        if tile2 == '5' and random.randint(0, 4) == 1 and l.count(tile1 + '6!') == 0:
            tile2 = '6!'
    global tile
    tile = tile1 + tile2 + '.png'

# 廃の画像貼り付け
def image_paste(a, b, c):
    # 背景画像、牌の画像を開く
    img1 = Image.open('./images/upload.png')
    img2 = Image.open('./images/' + a)
    # サイズ調節
    img2_size = (round(img2.width * 0.25), round(img2.height * 0.25))
    img2 = img2.resize(img2_size)
    # 背景と同サイズの透明な画像を生成し、透明画像の上に牌の画像をペースト
    img_clear = Image.new("RGBA", img1.size, (255, 255, 255, 0))
    img_clear.paste(img2, (b, c))
    img1 = Image.alpha_composite(img1, img_clear)
    img1.save('./images/upload.png', quality=95)


#-----------------------------------------------------------------------------
l = []
num = 0
# 牌の数が14になるまで繰り返す
while num < 14:
    haipai()
    # 同じ牌が既に4つあるなら除外
    if l.count(tile) < 4:
        l.append(tile)
        num += 1
print(sorted(l))
# ドラ表示牌抽選
while num < 15:
    haipai()
    if l.count(tile) < 4:
        dora = tile
        num += 1

# 牌の画像並べ
back = Image.open('./images/background.png')
img1 = back.copy()
x = 148
img1.save('./images/upload.png', quality=95)
for i in sorted(l):
    image_paste(i, x, 393)
    x += 65
image_paste(dora, 570, 188)

#-----------------------------------------------------------------------------
# ツイート
api.update_status_with_media(filename="./images/upload.png")