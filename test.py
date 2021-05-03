import pyupbit

access = "GdKBZzKwqKo1oQZnx6mKGELIIxLxnxaG6qEqLWOos"          # 본인 값으로 변경
secret = "zNtKxMxx6LZfNHzAWGccTlKh8x0762QpW1Ytu5xi"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTT"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회