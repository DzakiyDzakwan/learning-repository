student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# SUM()
built_in_sum_score = sum(student_scores)

print(built_in_sum_score)

# Manually Sum function

sum_score = 0

for score in student_scores:
    sum_score += score

print(sum_score)

# MAX()

built_in_max_score = max(student_scores)

print(built_in_max_score)

# Manually Max Score

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

# MIN()

built_in_min_score = min(student_scores)

print(built_in_min_score)

# Manually Min Score

min_score = student_scores[0]

for score in student_scores:
    if score <= min_score:
        min_score = score

print(min_score)