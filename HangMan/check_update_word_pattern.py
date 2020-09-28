from hangman import update_word_pattern
def test_updtae_word_pattern():
    """testing update word pattern"""
    check_list = [['aaa', '___', 'a'], ['lol', '___', 'a'],
                  ['bbq', '__q', 'b'],['booob','_____','b']]
    answer_list = ['aaa', '___', 'bbq','b___b']
    count = 0  # for counting right answers should be 4
    # run over check list and check if the the function return the answer list
    for i in range(len(check_list)):
        if update_word_pattern(check_list[i][0], check_list[i][1],
                               check_list[i][2]) == answer_list[i]:
            count += 1
    if count == 4:
        print("test success")
        return True
    else:
        print('test failed')
        return False


if __name__ == '__main__':
    test_updtae_word_pattern()