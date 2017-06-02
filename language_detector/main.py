# -*- coding: utf-8 -*-

"""This is the entry point of the program."""


def detect_language(text, languages):
    word_count = {}
    word_list = text.split()
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] +=1

    spanish_score = 0
    for lang in languages:
        if lang['name'] == 'Spanish':
            for word in lang['common_words']:
                if word in word_count:
                    spanish_score += word_count[word]

    german_score = 0
    for lang in languages:
        if lang['name'] == 'German':
            for word in lang['common_words']:
                if word in word_count:
                    german_score += word_count[word]
                    
    english_score = 0
    for lang in languages:
        if lang['name'] == 'English':
            for word in lang['common_words']:
                if word in word_count:
                    english_score += word_count[word]

    if spanish_score > german_score and spanish_score > english_score:
        return 'Spanish'
    elif german_score > spanish_score and german_score > english_score:
        return 'German'
    else:
        return 'English'
    