import question
bank=[['Q1:Why is Bloody Mary Called Bloody Mary?',
                '1:She drinks blood',\
                '2:She executes many people to revenge for her mum',\
                '3:She likes torturing people',\
                '4:She likes wine',\
                 '2'],\
                 ['Q2:When did Galileo start to create  a telescope?',\
                 '1:When he heard about Danish perspective glass',\
                 '2:When he saw it from a book',\
                 '3:When his friend encouraged him',\
                 '4:When he wants to prove his theory about the stars',\
                 '1'],\
                 ['Q3:Who invents coordinates?',\
                 '1:Newton',\
                 '2:Euler',\
                 '3:Descartes',\
                 '4:Euclid',\
                 '3'],\
                 ['Q4:Which country consumes the most chocolate per capita?',\
                 '1:America',\
                 '2:England',\
                 '3:Switzerland',\
                 '4:Australia',\
                 '3'],\
                 ['Q5:Which country invented ice cream?',\
                 '1:India',\
                 '2:Australia',\
                 '3:China',\
                 '4:Japan',\
                 '3'],\
                 ['Q6:What country has the most natural lake?',\
                 '1:Canada',\
                 '2:China',\
                 '3:Italy',\
                 '4:Denmark',\
                 '1'],\
                 ['Q7:Which planet has the most gravity?',\
                 '1:Mars',\
                 '2:Jupiter',\
                 '3:Venus',\
                 '4:Mercury',\
                 '2'],\
                 ['Q8:When was the first iphone released?',\
                 '1:2009',\
                 '2:2007',\
                 '3:2008',\
                 '4:2010',\
                 '2'],\
                 ['Q9:Which country produces the most coffee in the world?',\
                 '1:Brazil',\
                 '2:America',\
                 '3:Italy',\
                 '4:Spain',\
                 '1'],\
                 ['Q10:How many Pyramids of Giza were made?',\
                 '1:Three',\
                 '2:Four',\
                 '3:Five',\
                 '4:Six',\
                 '1']]
def main():
   print('This trivia game is for two players.There are 10 questions in total\
 and each player takes a turn at answering 5 questions.If the player answers\
 correctly,the player gets 1 point.\n')

   game = Game(bank)
   for _ in range(2): # We only have two players
      game.playRound()

   game.printScores()

class Game:
   def __init__(self, questionBank):
      self.player1=0
      self.player2=0
      self.currentPlayer = 1
      self.currentQuestionInd = 0
      self.questionBank = bank

   def switchPlayer(self):
      if self.currentPlayer == 1:
         self.currentPlayer = 2
      else:
         self.currentPlayer = 1

   def playRound(self):
      print(f"This is player {self.currentPlayer}'s turn\n")

      for _ in range(5): # _ is just a convention to indicate that this variable is not used in the code.
         x = bank[self.currentQuestionInd]
         ques=x[0]
         ans1=x[1]
         ans2=x[2]
         ans3=x[3]
         ans4=x[4]
         corr=x[5]
         q_a=question.Question(ques,ans1,ans2,ans3,ans4,corr)
         q_a.printQandA()

         player_answer=input('Which one is correct?Enter 1,2,3 or 4')
         if player_answer == q_a.correct:
            print('Congrat!You choose the correct answer!You earn a point\n')
            self.incrementCurrentPlayerScore()
         else:
            print(f"It is not the correct answer.The correct answer is {q_a.correct}\n")
         self.currentQuestionInd += 1
      self.switchPlayer()


   def incrementCurrentPlayerScore(self):
      if self.currentPlayer == 1:
         self.player1 += 1
      else:
         self.player2 += 1

   def printScores(self):
      print(f"Player1 gets {self.player1}")
      print(f"Player2 gets {self.player2}")

main()
