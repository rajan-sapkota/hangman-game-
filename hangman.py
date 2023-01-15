import random

word_list = ["Apple","Banana","Mango","Avocado"]

hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

def hash_maker(selection, word):
  dashes = ""
  string_selection = ''.join(selection)
  for i in range(0, len(word)):
    found_letter = " _ "
    for j in range(0, len(string_selection)):
      if word[i].upper() == string_selection[j]:
        found_letter = string_selection[j]
    dashes = dashes + found_letter

  return dashes

def hangman():
  word = random.choice(word_list)
  letter_to_be_guessed = set(word.upper())
  selection = set()
  guess = set()
  print("\nGuess the Fruit from below letters")
  print(letter_to_be_guessed)

  hang = 0 
  print(hangman_art[hang])

  while(len(letter_to_be_guessed) > 0 and hang < len(hangman_art) - 1):
    user_input = input("Type the letter_to_be_guessed of the word to be guessed: ").upper()
    if user_input in letter_to_be_guessed:
      selection.add(user_input)
      guess.add(user_input)
      letter_to_be_guessed.remove(user_input)
      dash = hash_maker(selection, word)
      print(dash)  

    elif user_input in guess:
      print("You've already used the letter_to_be_guessed try something else")
      print(hangman_art[hang])

    else:
      hang += 1
      print(hangman_art[hang])
      guess.add(user_input)
      print(user_input + " is not a letter of the word to be guessed.")
      dash = hash_maker(selection, word)
      print(dash)  

  if(len(letter_to_be_guessed) == 0):
    print("YOU'VE WON THE GAME !!!")
  elif(hang == len(hangman_art) - 1) :
    print("YOU'VE LOST AND DIED !!!")

hangman()