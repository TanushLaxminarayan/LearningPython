import random

word_list = ["black","white", "blue", "red"]

Chosen_Word = random.choice(word_list)
print(Chosen_Word)

placeholder = ""
word_length = len(Chosen_Word)
for position in range (word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters= []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in Chosen_Word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("you win:)")