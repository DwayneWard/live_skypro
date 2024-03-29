import random


def load_words_from_file(filename):
    """ чтение слов из файла """
    with open(filename, 'r', encoding='utf-8') as f:
        records = f.read().splitlines()

    return records


def shuffle_word(word):
    """ перемешивание букв """
    word_as_list = list(word)
    random.shuffle(word_as_list)
    word_shuffled = ''.join(word_as_list)
    return word_shuffled


def read_top(filename):
    """ чтение топового результата и возврат данных в виде словаря с ключами count и max"""
    with open(filename, 'r', encoding='utf-8') as f:
        records = f.read().splitlines()

    local_max = 0

    for record in records:
        record_name_and_score = record.split(' ')
        player_score = int(record_name_and_score[-1])
        if player_score > local_max:
            local_max = player_score

    number_of_games = len(records)

    return {'count': number_of_games, 'max': local_max}


def save_records_to_file(filename, name, score):
    """ запись в топ игроков """
    line_to_record = f"{name} {score}\n"

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(line_to_record)


def main():
    user_score = 0
    print('Введите ваше имя:')
    user_name = input()

    list_of_words = load_words_from_file('words.txt')

    for word in list_of_words:

        word_shuffled = shuffle_word(word)

        print(f'Угадайте слово: {word_shuffled}')
        print('Ваш ответ: ')
        user_input = input().lower()

        if user_input == word:
            print('Верно! Вы получаете 10 очков.')
            user_score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')

    save_records_to_file('history.txt', user_name, user_score)

    history_data = read_top('history.txt')

    print()
    print(f'Всего игр сыграно: {history_data["count"]}')
    print(f'Максимальный рекорд: {history_data["max"]}')


if __name__ == '__main__':
    main()
