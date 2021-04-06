import random
from datetime import datetime
import time

random.seed(0)

class Player:
    def __init__(self):
        self.name = None
        self.mode = mode

    def getName(self):
        return self.name

class HumanPlayer(Player):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hold_score = 0
        self.status = True
        self.mode = 'human'

    def Roll_Dice(self):
        round_score = random.randint(1, 6)
        return round_score

    def Run_Total(self):
        self.score += round_score
        return self.score

    def Hold(self):
        self.hold_score = self.score
        return self.hold_score

class ComputerPlayer(Player):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hold_score = 0
        self.status = True
        self.mode = 'computer'

    def Roll_Dice(self):
        round_score = random.randint(1, 6)
        return round_score

    def Run_Total(self):
        self.score += round_score
        return self.score

    def Hold(self):
        self.hold_score = self.score
        return self.hold_score

class TimedGameProxy(Player):

    def __init__(self):
        self.time = 0

    def Time(self):
        self.time = datetime.time(datetime.now())
        return self.time

class PlayerFactory:
    # select mode and pass the name to create an instance
    def getPlayer(self, name, mode):
        if mode == 'human':
            return HumanPlayer(name)
        if mode == 'computer':
            return ComputerPlayer(name)

if __name__ == '__main__':
    #Create interface to Player1 and Player2
    playerfactory = PlayerFactory()
    Player1 = playerfactory.getPlayer("Player1", "human")
    Player2 = playerfactory.getPlayer("Player2", "computer")

    #Track the session
    Time_Tracker = TimedGameProxy()

print("Game Started!")
while Player1.status is True and Player1.mode == 'human':
    print("Player1's turn.")

    start_time = Time_Tracker.Time()
    action = input("r = roll, h = hold")
    round_score = Player1.Roll_Dice()
    end_time = Time_Tracker.Time()

    # if the human player idle more than 1 minute and no action more than 3 seconds, tracker will determine the session is expired.

    if end_time.minute - start_time.minute >= 1 and end_time.second - start_time.second >= 3 and Player1.score > Player2.score:
        print("-----Session Expired------")
        print(f"Player1's score is : {Player1.score} and Player2's score is : {Player2.score}")
        print("Winer is Player 1!")
        break

    if end_time.minute - start_time.minute >= 1 and end_time.second - start_time.second >= 3 and Player1.score < Player2.score:
        print("-----Session Expired-----")
        print(f"Player1's score is : {Player1.score} and Player2's score is : {Player2.score}")
        print("Winer is Player 2!")
        break

    if action == 'h':
        Player1.status = False
        Player2.status = True
        Player1.Hold()
        print(f"Player1, You hold the score: {Player1.hold_score}")
        print("Player2's turn.")

    if round_score == 1:
        Player1.status = False
        Player2.status = True
        round_score = 0
        Player1.score = round_score + Player1.hold_score
        print(f"Round score is 1. Roll back to {Player1.score}")

    if action != 'h' and end_time.minute - start_time.minute < 1:
        Player1.Run_Total()
        print(f"round score: {round_score}, total: {Player1.score}")

    if Player1.score >= 100:
        print("Player1, you won!")
        break

    while Player1.status is False and Player2.mode == 'computer':
        print("Player2's turn.")
        round_score = Player2.Roll_Dice()
        if round_score == 1:
            Player2.status = False
            Player1.status = True
            round_score = 0
            Player2.score = round_score + Player2.hold_score
            print(f"Round score is 1. Roll back to {Player2.score}")

        Player2.Run_Total()
        print(f"Player2, your round score is: {round_score} and your score is : {Player2.score}")

        if Player2.score >= 25 + Player2.hold_score:
            Player2.status = False
            Player1.status = True
            Player2.Hold()
            print(f"Player2, You hold the score: {Player2.hold_score}")

        if Player2.score >= 100:
            print("Player2, you won!")
            break


