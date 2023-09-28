"""
猜數字遊戲
1.要可以任意產生亂數(1~50)
2.使用者可以猜測數字
3.偵測是否猜對
4.可以多次猜測
5.
"""

import random

low, high = 1, 50
x = random.randint(low, high)
print(x)
y = eval(input(f'請輸入一個數字{low}~{high}:'))
if y == x:
    print('恭喜猜對')
else:
    print('猜錯了')
