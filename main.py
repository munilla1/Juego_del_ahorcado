import random
import re
from hangmanpics import HANGMANPICS, SAVED

MAX_GUESS = 6


def remove_tilts(old):
    new = old.lower()
    new = re.sub(r'[àáâãäå]', 'a', new)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)

    return new


def pick_random_word():
    words = [
        'pelota',
        'chancho',
        'diccionario'
    ]

    index = random.randint(0, len(words) - 1)

    word = remove_tilts(words[index].strip()).upper()

    return word


def ask_user_for_next_letter():
    letter = input("Adivina la letra: ")
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)


def main():
    WORD = pick_random_word()

    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0

    print("Bienvenid@ al juego del ahorcado!")
    while (len(letters_to_guess) > 0) and num_guesses < MAX_GUESS:
        guess = ask_user_for_next_letter()

        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            print("Ya has escogido esa letra.")
            continue

        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1

        word_string = generate_word_string(WORD, correct_letters_guessed)

        print(f"""{word_string}""")
        print(HANGMANPICS[num_guesses])

        print("Te quedan {} intentos".format(MAX_GUESS - num_guesses))

    # tell the user they have won or lost
    if num_guesses < MAX_GUESS:
        print("Felicidades, has acertado correctamente la palabra: {}".format(WORD)+SAVED)
    else:
        print("Lo Siento!, la palabra que buscanas era: {}".format(WORD))


if __name__ == '__main__':
    main()
