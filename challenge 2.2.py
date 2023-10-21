'''Implement a class Player that represents a cricket player.The Player class should have a
method called play() which prints "The player is playing criket. Derive two classes, Batsman and
Bowler, from the player class. Override the play() method in each derive class to print "The batman
is batting" and "The bowler is bowling", respectively. Write a program to create object of both the
Batman and Bowler classes and call the play() method for each object.'''


# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")
    
# Define the derived class Batman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
    
# create objects of Batsman are Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() mathod for each object
batsman.play()
bowler.play()
  

