import pyupbit

access = "R3xbCxI9k7HaMNiImDIrqqtyB8Fs77mpwvv1Tr7N"          # 본인 값으로 변경
secret = "f98Ob9FBgXRkMQxDEhxQOyzzSnsBgbGyHT2P8mPI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회