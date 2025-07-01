import random

print("WELCOME TO HANGMAN GAME")

words_list = ['india', 'germany', 'japan', 'korea', 'cuba']
word = random.choice(words_list)   #any random word from the list is choosed
word_display = ['_' for i in word]  # the choosen word in underscores
attempt = 9
print(word_display)

while attempt>0 and '_' in word_display:   #goes until the attempts are left or the _ are left in the choosen word
    guess = input("Enter your guess : ")
    if guess in word:
        print("yes, it is in the word!!")
        attempt -=1          #attempts reduced as you guess your letters
        for index, letter in enumerate(word):   #enumerate helps you to index/give position to teh letters in the choosen word starting from 0
            if guess ==letter:
                word_display[index] = letter   #if guess and letter are same then the index position in choosen word will be replaced by the guess
                print(word_display)
    else:
        attempt= attempt-1
        print("no, it is not in the word!!")
        
print("no. of attempts left are : ", attempt)      

if '_' not in word_display:
    print("You won the game!")
elif attempt == 0:
    print("You lost the game!")

print("the word : ", ''.join(word_display))
