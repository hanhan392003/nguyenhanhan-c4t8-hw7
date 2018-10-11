# # ex 17
high_scores = [45, 67, 56, 78]
t = sorted(high_scores, reverse = True)
print(t)

# # ex 18
print("High scores:")
for i, high_score in enumerate(t):
    print(i+1, ".", high_score)

# ex 19 + 20 + 21
while True:
    new_high_score = int(input("Enter your new scores: "))
    high_scores.append(new_high_score)
    sort_high_scores = sorted(high_scores, reverse = True)
    print("High scores:")
    for i, high_score in enumerate(sort_high_scores):
        if i <= 4:
            print(i+1, ".", high_score)