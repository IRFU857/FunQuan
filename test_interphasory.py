import json
from patch_curriculum import make_q, make_interphasory_quiz

# Let's verify interphasory quiz lengths
p1_exam = make_interphasory_quiz(1)
p2_exam = make_interphasory_quiz(2)
p3_exam = make_interphasory_quiz(3)
p4_exam = make_interphasory_quiz(4)

print(f"P1 Exam count: {len(p1_exam)}")
print(f"P2 Exam count: {len(p2_exam)}")
print(f"P3 Exam count: {len(p3_exam)}")
print(f"P4 Exam count: {len(p4_exam)}")
