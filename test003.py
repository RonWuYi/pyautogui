# wechat redraw

from random import uniform

value = uniform(0.01, 100)


def lucky_draw(money, size):
    money_list = []
    while True:
        value = uniform(0.01, (money / size) * 2)
        money_list.append(value)
        money -= uniform(0.01, (money / size) * 2)
        size -= 1
        if size == 1:
            money_list.append(money)
            break

    return money_list


class RedEnvelop:
    def __init__(self, money, size):
        self.money = money
        self.size = size
        self.get = 0

    def draw(self):
        self.money -= uniform(0.01, (self.money / self.size) * 2)
        self.size -= 1
        if self.size == 1:
            return self.money
        else:
            return uniform(0.01, (self.money / self.size) * 2)

    @classmethod
    def lucky(cls):
        # little = 0.01
        money = cls().draw()
        if money > cls().get:
            cls().get = money
        return money

    @classmethod
    def lucky_list(cls):
        money_list = []
        while True:
            value = uniform(0.01, (cls().money / cls().size) * 2)
            money_list.append(value)
            cls().money -= uniform(0.01, (cls().money / cls().size) * 2)
            cls().size -= 1
            if cls().size == 1:
                money_list.append(cls().money)
                break
        return money_list

    def empty(self):
        if self.money == 0:
            return True
        else:
            return False


class User:
    def __init__(self, number, money):
        self.name = number
        self.money = money
        self.bankrupt = False

    def generate(self):
        if self.money >= 200:
            self.money -= 200
        else:
            self.bankrupt = True

    def fetch(self):
        self.money += RedEnvelop.lucky()
        return self.money


class Game:
    def __init__(self, bet, **users):
        self.bet = bet
        self.users = users
        self.round = 0

    def play(self):
        while True:
            largest_amount = 0.01
            largest_user = None
            self.round += 1
            for i in self.users:
                pass
                # allocated_list = lucky_draw(self.bet, self.users)
                # for i in allocated_list:
                #     if i > largest_amount:
                #         largest_amount = i
                # largest_user = allocated_list.index(largest_amount)
                #
                # for i in gamer:

                #https: // coderemixer.com / 2019 / 03 / 26 / wechat - red - envelope - analyze /


