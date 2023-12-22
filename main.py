from hangman_words import word_list
from pictures import stages
import random
from art import logo


#function for revealing characters
def reveal_characters(word, index, letter):
    converted_to_list = list(word)
    converted_to_list[index] = letter
    word = ""
    for item in converted_to_list:
        word += item
    return word

#START OF THE GAME
print(logo)

#configuration
generated_word = random.choice(word_list)
word_len = len(generated_word)
current_stage = 6
guessing_word = "_" * word_len
end_of_game = False

while not end_of_game:
    #input a character
    letter = input("\nGuess a letter: ").lower()
    if letter in guessing_word:
        print("You already guessed that letter correct")
        continue

    #checking
    if letter not in generated_word:
        current_stage -= 1
    else:
        for i in range(0, word_len):
            if letter == generated_word[i]:
                guessing_word = reveal_characters(guessing_word, i, letter)

    print(guessing_word)

    #checking for the end of the game
    if current_stage == 0:
        print(f"You lost, the word you were looking for was {generated_word}")
        end_of_game = True
    elif guessing_word == generated_word:
        print("YOU WON!")
        end_of_game = True

    print(stages[current_stage])

print("Thank you for playing our game!\nBy Kibshh")
