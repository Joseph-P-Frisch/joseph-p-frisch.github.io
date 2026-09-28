from random import randint

scores = []
score = randint(1,100)

def update_high_scores():
    global score, scores
    j = 5
    for i in range(20):
        scores.append(randint(1,100))
    scores.append(score)

    for i in range(len(scores)):
        print(f"scores: {scores}")
        for j in range(len(scores)-1):
            #print(f"is scores[i] {scores[i]} > scores[j] {scores[j]}? if so, swap them")
            if int(scores[i]) > int(scores[j]):
                scores[j], scores[i] = scores[i], scores[j]
    print(f"scores: {scores}")

update_high_scores()