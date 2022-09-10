import random
class Game:
    def __init__(self):
        self.num = random.randint(1,100)
        self.totalGuess = 0
        self.isCompleted = False

    def guess(self, guess):
        self.totalGuess += 1
        if guess==self.num:
            print('Congratulations!')
            print(f'Your total guess is {self.totalGuess}')
            self.isCompleted = True
        elif guess>self.num:
            print('Too high,try again')

        elif guess<self.num:
            print('too low,try again')


if __name__ == "__main__":
    game = Game()
    while not game.isCompleted:
        guess= int(input('enter a number between 1 and 100\n'))
        game.guess(guess)
