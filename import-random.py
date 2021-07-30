# 使用 random - 隨機
# 讓使用者重複輸入數字,直到猜對指定數字才停止 使用 while

import random
star = int(input('請輸入隨機範圍數字起始值: '))
end = int(input('請輸入隨機範圍數字結束值:'))
r = random.randint(star, end)
count = 0
while True:
    count += 1
    num = int(input('請猜數字: '))
    if num == r:
        print('猜中了!')
        break
    elif num > r:
        print('提示: 比答案大')
    elif num < r:
        print('提示: 比答案小')
    print('這是你猜的第', count, '次')