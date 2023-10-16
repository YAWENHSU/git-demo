"""
猜數字遊戲
1.要可以任意產生亂數(1~50)
2.使用者可以猜測數字
3.偵測是否猜對
4.可以多次猜測
5.
"""

import random

low, high = 1, 100
nums = 10
x = random.randint(low, high)
# print(x)
level=1
print(f"歡迎來到猜數字遊戲，目前等級Level:{level}")
count = 0
for i in range(nums):
    y = eval(input(f'({count+1}/{nums})請輸入一個數字{low}~{high}:'))
    if y == x:
        print('恭喜猜對')
        break
    else:
        if y > x:
            print("猜低一點")
            if y < high:
                high = y-1
        else:
            print("猜高一點")
            if y > low:
                low = y+1
    count += 1
if y != x:
    print("答案為:", x)
