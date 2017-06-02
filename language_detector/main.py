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
    
    score_list = []
    for lang in languages:
        score = 0
        for word in lang['common_words']:
            if word in word_count:
                score += word_count[word]
        score_list.append((score, lang['name']))
    
    return sorted(score_list, reverse=True)[0][1]
