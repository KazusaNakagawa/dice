"""
2019/12/14

Roll the dice
"""

import time
import random
from logging import getLogger, debug, basicConfig, DEBUG, INFO, ERROR

FORMAT = '%(asctime)s - %(name)s %(levelname)s - %(lineno)d line : %(message)s'

# これはメインのファイルにのみ書く
basicConfig(level=ERROR, format=FORMAT)

# これはすべてのファイルに書く
logger = getLogger(__name__)


class Dice(object):
    def __init__(self, number=None, face=None):
        self.number = number
        self.face = face
        self.result_list = []

    def dice_data(self):
        while True:
            try:
                self.number = int(input("使用個数: "))
                if self.number < 1 or self.face < 1:
                    print("1以上で入力してください")
                    continue
                break
            except ValueError as ex:
                logger.error({ex: "空文字"})
                print("数字で入力してください")
                continue

    def dice_result(self):
        for _ in range(self.number):
            result = random.randint(1, self.face)
            self.result_list.append(result)

    def dice_result_display(self):
        rows = ['', '', '']

        for row in self.result_list:
            rows[0] += ' --- '
            if row == 1:
                rows[1] += '| ・|'
            elif row > 9:
                rows[1] += '| {} |'.format(row)
            elif row < 10:
                rows[1] += '| {} |'.format(row)
            rows[2] += ' --- '
        self.result_list.clear()
        for i in range(3):
            print(rows[i])
        print("")

    def dice_slow(self):
        while True:
            choice = input("振る: Enter 振らない: (E)ed\n").upper()
            if choice == "":
                self.dice_result()
                self.dice_result_display()
                continue
            elif choice == "E":
                break
            else:
                print("指定通りに選択してください")
                continue
        print("end")

    def test(self):
        num = 0
        while num < 500:
            time.sleep(0.01)
            self.dice_result()
            self.dice_result_display()
            num += 1
            print(num)

        print("test end")


def game():
    print(''' Roll the dice 
    ''')
    while True:
        choice = input("1: 固定 -> サイコロ数:2個 6面\n2: 自由に入力可能\n")
        if choice == '1':
            dice = Dice(2, 6)
            dice.dice_slow()
            break
        elif choice == '2':
            print("サイコロのデータ")
            dice = Dice(None, 6)
            dice.dice_data()
            dice.dice_slow()
            break
        else:
            print("入力は半角数字で")
            continue


if __name__ == "__main__":
    game()
    # dice_ = Dice(2, 6)
    # dice_.test()
