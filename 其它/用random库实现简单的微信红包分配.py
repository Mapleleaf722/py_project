import random


def red_packet(total, num):
    for i in range(1, num):
        # 保证每个人获得红包的期望是total/num
        per = random.uniform(0.01, total / (num - i + 1) * 2)
        total -= per
        print(f"第{i}位的红包金额：{round(per, 2)}元，")
    else:
        print(f"第{num}位的红包金额：{round(total, 2)}元，")


red_packet(10, 5)
