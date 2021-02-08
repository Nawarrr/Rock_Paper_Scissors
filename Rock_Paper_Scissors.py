# CSE314
#
# Topic: HW Assignment 1
# Author : Abdelrahman Medhat Saad Nawar
# Date : 06/ 12/ 2020
# Text Based Rock Paper Scissors
# Important Note: I wanted to have as much fun as possible doing this code,
#                 The code might be a little competitive and mean(in a funny way)


import random


class Rock_Paper_Scissors:
    """This Class simulates a Rock Paper Scissors game between the user and The Computer"""

    def __init__(self, num_of_rounds):
        """
        Initializing The needed variables
        :param num_of_rounds: The number of rounds is taken as input
        """
        self.num_of_rounds = num_of_rounds
        self.rps = ['R', 'P', 'S'] # R for Rock , P for Paper and S for Scissors
        self.human_wins = 0
        self.computer_wins = 0
        self.draw = 0
        self.won = ''

    def round(self):
        """
        This function simulates a round of Rock Paper Scissors takes input for your choice and randoms the computer
        choice Implementing the winner of the round using the comouter and the human choices The point is both the
        input and The computer choice is either R , P  or S , Noting that R < P , P < S , S < R which means that
        every element losses to the element after with a cycle, So when the difference between their indices
        in the list self.rps =[R , P , S] is 1 or  -2(for the case of Scissors and Rock) The 1st player wins
        (E.g : x1 -  x2 = 1 Then x1 wins)
        :return:
        """
        computer_choice = random.choice(self.rps)  # random choice from the rps List which includes R , P and S
        human_choice = input("Enter R for Rock , P for Paper , S for Scissors : ").strip()  # Taking the human input and
        # removing the spaces so it's only a string with either R, P or S

        hw = self.rps.index(human_choice) - self.rps.index(computer_choice) == 1 or self.rps.index(
            human_choice) - self.rps.index(computer_choice) == -2  # this the human win condition as mentioned in
        # the docstring
        cw = self.rps.index(computer_choice) - self.rps.index(human_choice) == 1 or self.rps.index(
            computer_choice) - self.rps.index(human_choice) == -2  # this the computer win condition as mentioned
        # in the docstring
        if hw:  # If statement to decide the round winner and add a point to it's counter
            self.human_wins += 1
            print('Computer :', computer_choice)
            print("You won this round")
        elif cw:
            print('Computer :', computer_choice)
            print("I won this round")
            self.computer_wins += 1
        else:
            self.draw += 1
            print('Computer :', computer_choice)
            print("Draw")

    def game(self):
        """This function simulates a Game of Rock Paper scissors using the Round Method and the num_of_rounds chosen by
         the user and decide who is the winner depending on the number of rounds won by the user and the computer"""

        for i in range(0, self.num_of_rounds):  # looping with number of rounds and calss the Method round
            print("Round : " + str(i + 1))
            self.round()
            # defining KO (Knock out) if somebody won before the game is done
            KO = self.human_wins > 0.5 * self.num_of_rounds or self.computer_wins > 0.5 * self.num_of_rounds
            if KO:
                break
        if self.human_wins > self.computer_wins:  # checks if human wins
            self.won = "You are cheating, You must have edited me to win"
        elif self.computer_wins > self.human_wins:  # checks if computer wins
            self.won = "HaHa you got beaten by a Spaghetti Code , Spaghetti Code go brr"
        else:  # a Draw
            self.won = "It's a Draw." \
                       "Me, You, Rematch, NOW"

    def results(self):
        """This function prints the Results of the game by printing the number of rounds won and the winner """
        print(" Computer wins : ", self.computer_wins, "\n", "Human wins    : ", self.human_wins, "\n"
              , "Draws         : ", self.draw, "\n", self.won)


def main(y):
    x = Rock_Paper_Scissors(y)
    x.game()
    x.results()


main(5)
