stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
print("\n")

import random

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]
ran_word = random.randint(0, len(word_list) - 1)
chosen_word = word_list[ran_word]
#chosen_word = random.choice(word_list)
num_of_lives = 6
show_list = []
for i in range(0, len(chosen_word)):
    show_list += "_"
print(show_list)
print("\n")
stop = False
while not stop:
    guess = input("Guess a letter:").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            show_list[pos] = guess
    if guess not in chosen_word:
        num_of_lives -= 1
        if (num_of_lives == 0):
            stop = True
            print("You lose !!")
    print(show_list)
    if "_" not in show_list:
        stop = True
        print("You win !!")
    print(stages[num_of_lives])
