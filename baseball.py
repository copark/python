#!/usr/bin/env python
import random
import math

class Baseball:
    STR_LENGTH = 3
    MAX_GAME_COUNT = 5

    def __init__(self):
        self.game = ""
        self.count = 0;
        while len(self.game) != Baseball.STR_LENGTH:
            var = random.randrange(1, 10)
            svar = ("%d" % var)
            if self.game.find(svar) >= 0:
                continue
            self.game += svar

        print self.game

    def run(self, value):
        return self.judge_strike(self.game, value) | self._judge_ballg(self.game, value)


    def _cmp_char(self, x, y):
        return (x == y)

    def _contain(self, x, y, e):
        i = x.find(y)
        return (i >= 0) & (i != e)

    def judge_strike(self, base, value):
        result = 0
        for index in range(0, len(base)):
            if self._cmp_char(base[index], value[index]):
                result += (1 << (index))
        return result

    def _judge_ballg(self, base, value):
        result = 0
        for index in range(0, len(base)):
            if self._contain(base, value[index], index):
                result += (1 << (index + Baseball.STR_LENGTH))
        return result

is_out = lambda x: x == Baseball.STR_LENGTH
get_bin = lambda x: format(x, 'b')

def get_strike(x):
    count = 0
    for index in range(0, Baseball.STR_LENGTH):
        if x & (1 << index):
            count += 1
    return count

def get_ball(x):
    count = 0
    for index in range(0, Baseball.STR_LENGTH):
        if x & (1 << (index + Baseball.STR_LENGTH)):
            count += 1
    return count

def Main():
    print "Baseball Game!"

    bb = Baseball()

    left_count = Baseball.MAX_GAME_COUNT
    while True:
        if left_count == 0:
            print "Game Over!"
            exit()

        print "Left count = ", left_count
        left_count -= 1

        val = input("Guess ? ")

        result = bb.run(str(val));
        s = get_strike(result)
        b = get_ball(result)

        if is_out(s):
            print "You did it! Good Boy! Bye!!"
            exit()

        print "%dStrike(s), %dBall(s)" % (s, b)

if __name__ == '__main__':
    Main()
