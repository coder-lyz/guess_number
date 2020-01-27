##########################################
# This is a game which can let you guess #
# a number. You can choose the level di- #
# fficult, medium or easy. If the number #
# you guessed is too big or too small it #
# will give you a hint, until the number #
# you guessed is equals to the number g- #
# ame choose.                            #
##########################################

import random

class GuessNumber():
    def __init__(self):
        self.num = 0
        self.max = 0
        self.min = 0
        self.player_num = 0
        self.levels = ['d','m','e']
        self.level = None
        self.choose_level()

    def choose_level(self):
        choice = input('Which level do you want to choose, difficult, medium or easy? (d/m/e)\n').strip()
        if choice == self.levels[0]:
            self.level = 'Difficult'
            self.max, self.min = 10000, 1
        elif choice == self.levels[1]:
            self.level = 'Medium'
            self.max, self.min = 1000, 1
        elif choice == self.levels[2]:
            self.level = 'Easy'
            self.max, self.min = 100, 1
        else:
            choice = input('Which level do you want to choose, difficult, medium or easy? (d/m/e)\n').strip()
        print(f'You have already chosen the level "{self.level}". The max number is {self.max}, and the min number is {self.min}. Game starts.')
        self.get_number()

    def get_number(self):
        self.num = random.randint(self.min,self.max)
        self.game()

    def game(self):
        while self.player_num != self.num:
            try:
                self.player_num = int(input('Now you can guess the number.\n'))
                if self.player_num > self.num:
                    print('Too big.\n')
                elif self.player_num < self.num:
                    print('Too small.\n')
            except:
                print('Please type a number! \n')
        print(f'\nCongratulations! You have already guessed the number {self.num}!')
        self.if_restart()
    
    def if_restart(self):
        r = input('Do you want to replay the game? (y/n)\n').strip()
        if r == 'y':
            self.__init__()
        elif r == 'n':
            print('Okay. See you next time!')


number_game = GuessNumber()