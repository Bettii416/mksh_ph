scores = list()
score = int(input("score="))
wwhile score>=0:
    scores.append(score)
    score = int(input("score="))
print("總分是：", scores)
print("總分是：", sum(scores))