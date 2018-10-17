#!/usr/bin/env python

scores_by_student = {}
sum_of_scores = 0

def number_to_grade(raw_score):
    if raw_score > 94:
        letter_grade = 'A'
    elif raw_score > 88:
        letter_grade = 'B'
    elif raw_score > 82:
        letter_grade = 'C'
    elif raw_score > 74:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade

a = 88
b = 99
print(number_to_grade(a))
print(number_to_grade(b))
print(number_to_grade(47))


with open("../DATA/testscores.dat") as scores_in:

    for line in scores_in:
        name, score = line.split(":")
        score = int(score)
        scores_by_student[name] = score
        sum_of_scores += score

for student, score in sorted(scores_by_student.items()):
    grade = number_to_grade(score)
    #               0      1    2            0        1      2
    # print("{0:20.20s} {1:3d} {2}".format(student, score, grade))
    print(f"{student:20.20s} {score:3d} {grade}")

average = sum_of_scores/len(scores_by_student)
print("\naverage score is  {:.2f}\n".format(average))
