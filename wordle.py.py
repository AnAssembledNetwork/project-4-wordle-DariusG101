import random
colors = {"green": "\033[1;32;40m","yellow": "\033[1;33;40m","red": "\033[1;31;40m","reset": "\033[0;37;40m"}

def makeValidguess(correct_Answer):
  guess = (input("\nGuess a word:\n\n")) 
  while len(guess) !=  5 or guess not in word_Bank:
    if len(guess) != 5:
      guess = (input("The word you chose was not a 5 letter word \nTry again\n\n"))
    else:
      guess = (input("this is not a real 5 letter word \nTry again\n\n")) 
    
  return guess

def compare_word(guess):  
  for i in range(5):
    if correct_Answer[i] == guess[i]:
      gReen.append(guess[i])
    elif guess[i] in correct_Answer:
      yEllow.append(guess[i])
    else:
      rEd.append(guess[i])
  keyboard()    
    

    
    
 
def printColor(guess):
  for i in range(0,len(guess)):
    if correct_Answer[i] == guess[i]:
      print( colors["green"] + guess[i] + colors["reset"])
    elif guess[i] in correct_Answer:
      print(colors["yellow"] + guess[i] + colors["reset"])
    else:
      print(colors["red"] + guess[i] + colors["reset"])
    

  
        
    # if guess in gReen:
    #   print(gReen + "\033[1;32;40m")
    # if guess in yEllow:
    #   print(yEllow + "\033[1;33;40m")
    # if guess in rEd:
    #   print(rEd + "\033[0;31;47m")
  
 
    
  
def keyboard():  
  row1 = (" q w e r t y u i o p ")
  row2 = ("  a s d f g h j k l ")
  row3 = ("   z x c v b n m ")
  line1Returns = keyboardColors(row1)
  line2Returns = keyboardColors(row2)
  line3Returns =keyboardColors(row3)
  print(line1Returns)
  print(line2Returns)
  print(line3Returns)
def keyboardColors(line):  
  line1 = ""
  for letter in line:
    if (letter != " "):
      if letter in gReen:
        line1 += colors["green"] + letter + colors["reset"]
      elif letter in yEllow:
        line1 += colors["yellow"] + letter + colors["reset"]
      elif letter in rEd:
        line1 += colors["red"] + letter + colors["reset"]
      else:
        line1 += letter
    else: line1 += letter
  return line1


 


def wordle():
  global gReen
  global yEllow 
  global rEd 
  global word_Bank
  global correct_Answer
  gReen = []
  yEllow = []
  rEd = []
  word_Bank = (open("words.txt", "r").readline().split())
  correct_Answer = random.choice( word_Bank)
  # print(correct_Answer)
  guesses = 0
  for i in range(0,6):
    guesses += 1
    guess = makeValidguess(correct_Answer)
    guess = guess.lower()
    if guess == correct_Answer:
        print(f"Congratulations! You guessed the correct word in {guesses} attempts! Nice job!")
    if guesses == 6:
      print(f"sorry you lost the correct word was {correct_Answer}")
    printColor(guess)
    compare_word(guess)
    
   
   
  
 
  
  
    


  
  
def main():
  wordle()
 

  



if __name__ == "__main__":
    main()