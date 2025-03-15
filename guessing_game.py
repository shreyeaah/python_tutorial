from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "guessing game")
        self.myNumber = random.randint(1,100)
        self.count=0

        greeting = "Guess a number between 1 and 100"
        self.hintLabel = self.addLabel(text = greeting, row =0, column = 0, columnspan=2 )
        self.addLabel(text = "your guess", row = 1, column = 0)
        self.guessField = self.addIntegerField(value =0, row = 1, column = 1, width = 10)
        self.nextBtn = self.addButton(text="Next", row =2, column = 0, command = self.next)
        self.newBtn = self.addButton("New Game", row = 2, column= 1, command = self.newgame)
    def next(self):
        self.count+=1
        guess = self.guessField.getNumber()
        if guess == self.myNumber:
            self.hintLabel["text"]="You've guessed it right in" +str(self.count) +"attempts"
            self.nextBtn["state"]="disabled"
        elif guess < self.myNumber:
            self.hintLabel["text"]= "It's too small"
        else:
            self.hintLabel["text"]="It's too large"
    def newgame(self):
        self.myNumber = random.randint(1, 100)
        self.count=0
        greeting = "Guess a number between 1 and 100"
        self.hintLabel["text"]=greeting
        self.guessField.setNumber(0)
        self.nextBtn["state"]="normal"
        
def main():
        GuessingGame().mainloop()
if __name__=="__main__":
        main()
        
        
