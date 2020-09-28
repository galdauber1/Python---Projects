from hangman_helper import *
from collections import Counter



def letter_index(word, letter):
    """ return list of the indexs of a letter in a word"""
    return [i for i, ltr in enumerate(word) if ltr == letter]


def update_word_pattern(word, pattern, letter):
    """update the pattern if the letter is in the word"""
    pattern_list = list(pattern)
    for i in range(len(letter_index(word, letter))):
        pattern_list[letter_index(word, letter)[i]] = letter
    pattern_list = ''.join(pattern_list)
    return pattern_list


def word_to_pattern(word):
    """word to to hidden pattern"""
    pattern = len(word) * "_"
    return pattern, word


def pattern_preparation(word_list):
    """return the hidden pattern of a word """
    return word_to_pattern(get_random_word(word_list))


def run_single_game(word_list):
    """"run a single game of hangman"""
    ask_play, error_count, choosen_letters_list, msg, pattern, word,\
    word_solved, wrong_guess_lst = pre_game(word_list)
    while error_count < MAX_ERRORS and not word_solved:
        display_state(pattern, error_count, wrong_guess_lst, msg, ask_play)
        l = get_input()  # l for letter
        if l[0] == HINT:
            word_hint_list = filter_words_list(word_list,pattern,wrong_guess_lst)
            l = choose_letter(word_hint_list,pattern)
            msg = HINT_MSG + "" + l
        if l[0] == LETTER:
            letter = str(l[1])
            if (valid_letter(ask_play, error_count, letter, msg, pattern,
                             wrong_guess_lst)) is True:
                if letter not in word and letter not in wrong_guess_lst:
                    wrong_guess_lst.append(letter)  # update wrong guess lst
                    msg = DEFAULT_MSG
                    error_count += 1
                elif letter in wrong_guess_lst or letter in pattern:
                    msg = ALREADY_CHOSEN_MSG
                elif letter in word:  # if the word contain the letter
                    msg = DEFAULT_MSG
                    pattern = update_word_pattern(word, pattern, letter)
                if pattern == word:  # if the user find the word
                    word_solved = True
            else:
                msg = NON_VALID_MSG

    end_game(error_count,pattern,word,word_solved,wrong_guess_lst)


def end_game(error_count, pattern, word, word_solved, wrong_guess_lst):
    """this is the func that decide if the player lose or won and show msg"""
    if word_solved:
        msg = WIN_MSG
    else:
        msg = LOSS_MSG + "" + word
    ask_play = True
    display_state(pattern, error_count, wrong_guess_lst, msg, ask_play)


def filter_pattern(words,pattern):
    """return new list of words that are similar to the pattern"""
    exposed_list = [i for i, ltr in enumerate(pattern) if ltr != '_']
    # list of all the index of exposed letters in pattern
    filterd_list = []
    for word in words:  # run over every word
        counter = 0  # counts if all the exposed letter is similar
        for i in exposed_list:  # run over the amount of exposed letters
            if word[i] == pattern[i]:  # if the exposed let in  same position
                counter += 1  # add to the counter
        if counter == len(exposed_list):  # the counter should be len(exposed)
            filterd_list.append(word)  # add to ne list
    return filterd_list


def filter_words_list(words, pattern, wrong_guess_lst):
    """filtering words"""
    filter_list = [s for s in words if len(s) == len(pattern)]
    # filter the words that not in the same len
    filter_list = filter_pattern(filter_list, pattern)
    # filter words that not in the same pattern
    # check if word from filter list contain letter from wrong guess list
    return [word for word in filter_list if not \
        any(bad in word for bad in wrong_guess_lst)]



def choose_letter(words, pattern):
    """
        this function will return the most frequent letter in words and also
        not in the pattern
        """
    alphabetic_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                       'v', 'w', 'x', 'y', 'z']
    freq_list = [0]*26  # define new alphabetic list
    for word in words:  # new empty list
        for i in range(len(alphabetic_list)):   # run over the words
            freq_list[i] += word.count(alphabetic_list[i])  # count each letter
    index = freq_list.index(max(freq_list))  # the index of the most frequent
    while alphabetic_list[index] in pattern:  # while letter in pattern
        del freq_list[index]
        index = freq_list.index(max(freq_list))  # and dfine the new max
    return alphabetic_list[index]


def valid_letter(ask_play, error_count, letter, msg, pattern, wrong_guess_lst):
    """this function check if the letter is valid letter"""
    if len(letter) > 1:  # len = 1
        msg = NON_VALID_MSG
    elif not letter.isalpha():  # alphabetic
        msg = NON_VALID_MSG
    elif not letter.islower():  # lower case
        msg = NON_VALID_MSG
    else:  # letter is valid
        return True
    return msg


def pre_game(word_list):
    """define some verbiales"""
    msg = DEFAULT_MSG
    wrong_guess_lst = []
    pattern, word = pattern_preparation(word_list)
    error_count = 0
    ask_play = False
    hint_list = []
    word_solved = False
    return ask_play, error_count, hint_list, msg, pattern, word,\
        word_solved, wrong_guess_lst


def main():
    answer = True
    word_list = load_words(file='words.txt')
    while answer:
        run_single_game(word_list)
        answer = get_input()[1]


if __name__ == '__main__':
    start_gui_and_call_main(main)
    close_gui()



