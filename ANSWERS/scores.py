#!/usr/bin/env python

scores_by_student = {}
sum_of_scores = 0.0

with open("../DATA/testscores.dat") as scores_in:

    for line in scores_in:
        (name, score) = line.split(":")
        score = int(score)
        scores_by_student[name] = score
        sum_of_scores += score

for student, score in sorted(scores_by_student.items()):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    print("{:<20s} {} {}".format(student, score, grade))

average = sum_of_scores/len(scores_by_student)
print("\naverage score is  {:.2f}\n".format(average))
