from random import randint


class Hangman:
    def __init__(self):
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        self.lives = 6
        self.hsteps = {
            6: '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
            5: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
            4: '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
            3: '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
            2: '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
            1: '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
            0: '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
        }

    def play(self, word=""):
        self.word = word.lower()
        if self.word == "":
            rand = randint(0, 63)
            words = (
                'ant baboon badger bat bear beaver camel cat clam cobra cougar '
                'coyote crow deer dog donkey duck eagle ferret fox frog goat '
                'goose hawk lion lizard llama mole monkey moose mouse mule newt '
                'otter owl panda parrot pigeon python rabbit ram rat raven '
                'rhino salmon seal shark sheep skunk sloth snake spider '
                'stork swan tiger toad trout turkey turtle weasel whale wolf '
                'wombat zebra ').split()
            self.word = words[rand]
            self.game(self.word)

    def game(self, word):
        print(self.hsteps[self.lives])
        print("\n")
        blnkwrd = []
        for i in word:
            blnkwrd.append("_")
        print("The word is:")
        while "_" in blnkwrd:
            for i in blnkwrd:
                print(i, end=" ")
            print("\n")
            for i in self.alphabet:
                print(i, end=" ")
            print("\n")
            letter = (input("Guess a letter: ")).lower()
            if letter in self.alphabet:
                self.alphabet[self.alphabet.index(letter)] = "_"
                if word.count(letter) != 0:
                    cnt = 0
                    for i in word:
                        if i == letter:
                            blnkwrd[cnt] = letter
                        cnt += 1
                else:
                    if self.livesubtract() == 0:
                        pass
                    else:
                        return
            else:
                print("Letter Already Guessed\n")
        print("\nYou Got it, The word was...\n\t{}".format(word))

    def livesubtract(self):
        if self.lives > 0:
            self.lives -= 1
            print(self.hsteps[self.lives])
            return 0
        else:
            print("Game Over!")
            print("The word was {}".format(self.word))
            return 1


game = Hangman()
game.play()
