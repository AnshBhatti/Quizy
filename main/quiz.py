from random import shuffle, choice
from . import models


def make_quiz(MC=False, MT=False, FB=False, TF=False):
    objs = list(models.Questions.objects.all())
    shuffle(objs)
    answers = []
    answers2 = []
    quiz = {}
    answer_key = {}
    alloc = [0, 0, 0, 0]
    for each in objs[:5]:
        if each.qtype == 'alpha':
            quiz[each.question] = [each.answer,
                                   each.answer1, each.answer2, each.answer3]
            answer_key[each.question] = each.answer
        else:
            quiz[each.question] = [each.img, each.img1, each.img2, each.img3]
            answer_key[each.question] = each.img
        shuffle(quiz[each.question])
    if MT:
        alloc[0] = 3
    if MC:
        alloc[1] = 1
    if FB:
        alloc[2] = 1
    if TF:
        alloc[3] = 1
    c = 3
    while sum(alloc) < 5:
        if alloc[c]:
            alloc[c] += 1
        c -= 1
        c %= 4
    c = 3
    while sum(alloc) > 5:
        if alloc[c]:
            alloc[c] = 0
        c -= 1
        c %= 4
    return quiz, answer_key, alloc
