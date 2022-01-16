from ast import Global
import pyupbit
import requests
import numpy as np

access = "key"          # 본인 값으로 변경
secret = "key"          # 본인 값으로 변경
myToken = "key"
upbit = pyupbit.Upbit(access, secret)

start_time = 0
def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    global start_time 
    start_time = df.index[0]
    print(df)
    return start_time

get_start_time("KRW-BTC")
print(start_time)
