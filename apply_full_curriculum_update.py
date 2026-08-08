import json
import re
from patch_curriculum import make_interphasory_quiz
from generate_all_curriculum import p1_quizzes
from enrich_all_lessons import p2_quizzes, p3_quizzes
from generate_final_curriculum_ts import p4_quizzes

# Combine all lesson quizzes
all_lesson_quizzes = {}
all_lesson_quizzes.update(p1_quizzes)
all_lesson_quizzes.update(p2_quizzes)
all_lesson_quizzes.update(p3_quizzes)
all_lesson_quizzes.update(p4_quizzes)

print(f"Total lesson quiz sets: {len(all_lesson_quizzes)}")

# Generate interphasory quizzes
p1_inter = make_interphasory_quiz(1)
p2_inter = make_interphasory_quiz(2)
p3_inter = make_interphasory_quiz(3)
p4_inter = make_interphasory_quiz(4)

interphasory_map = {
    1: p1_inter,
    2: p2_inter,
    3: p3_inter,
    4: p4_inter
}

print("Interphasory exams ready.")
