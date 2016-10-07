from random import randint
from itertools import combinations


class Team:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.goal = 0
        self.win = 0
        self.fail = 0
        self.draw = 0
        self.points = 0
        self.goalsum = 0

    def __str__(self):
        return 'Name:{0} GoalSum:{1} Win:{2} Fail:{3} Draw:' \
               '{4} Points:{5}'.format(self.name, self.goalsum,
                                       self.win, self.fail,
                                       self.draw,self.points)


class Game:
    def __init__(self, team1, team2, score):
        self.one = team1
        self.two = team2
        self.sc = score

    def __str__(self):
        return 'Game: {0} : {1} Score: {2}'.format(self.one,
                                                   self.two, self.sc)


def play(team1, team2, score, i):
    team1.goal = randint(0, 5)
    team1.goalsum += team1.goal
    team2.goal = randint(0, 5)
    team2.goalsum += team2.goal
    score[i] = Game(team1.name, team2.name, str(
        team1.goal) + ':' + str(team2.goal))
    if team1.goal > team2.goal:
        team1.win += 1
        team2.fail += 1
        team1.points += 3
    elif team1.goal < team2.goal:
        team2.win += 1
        team1.fail += 1
        team2.points += 3
    else:
        team1.draw += 1
        team2.draw += 1
        team1.points += 1
        team2.points += 1


def make_table(t, gam):
    i = 0
    for team1_num, team2_num in combinations(t, 2):
        play(num_to_team[team1_num], num_to_team[team2_num], gam, i)
        i += 1
    return t, gam


def find_team(teamf, team, bo):
    if team.name == teamf:
        print(team)
        bo = 1


def find_game(t1,t2,scoree, b):
    if scoree.one == t1 and scoree.two == t2:
        print(scoree)
        b = 1
    if scoree.one == t2 and scoree.two == t1:
        print(scoree)
        b = 1


gama = dict()
num_to_team = dict()
num_to_team[1] = Team(1, 'spartak')
num_to_team[2] = Team(2, 'loko')
num_to_team[3] = Team(3, 'dinamo')
num_to_team[4] = Team(4, 'cska')
num_to_team[5] = Team(5, 'anji')
num_to_team[6] = Team(6, 'sovety')
k = 1
make_table(num_to_team, gama)
while k == 1:
    command = input('Input command or "help": ')

    if command == 'out':
        for team in sorted(num_to_team.values(), key=lambda
                x: x.points, reverse=True):
            print(team)
    if command == 'exit':
        break
    if command == 'help':
        print('commands: out, search, igra, help, exit')
    if command == 'search':
        cmd = input('Print name of team:  ')
        i = 1
        b = 0
        while i <= 6:
            find_team(cmd, num_to_team[i], b)
            i += 1
            if b == 1:
                break
    if command == 'igra':
        first = input('Print first team:  ')
        second = input('Print second team:  ')
        i = 0
        b = 0
        while i <= 14:
            find_game(first, second, gama[i], b)
            i += 1
            if b == 1:
                break