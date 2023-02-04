# coding: UTF-8
import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("API_KEY") # 環境変数の値をCKに代入
CS = os.environ.get("API_SECRET")
AT = os.environ.get("ACCESS_TOKEN")
ATC = os.environ.get("ACCESS_TOKEN_SECRET")
