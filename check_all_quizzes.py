import json
from patch_curriculum import make_interphasory_quiz
from generate_all_curriculum import p1_quizzes
from enrich_all_lessons import p2_quizzes, p3_quizzes
from generate_final_curriculum_ts import p4_quizzes

all_quizzes = {}
all_quizzes.update(p1_quizzes)
all_quizzes.update(p2_quizzes)
all_quizzes.update(p3_quizzes)
all_quizzes.update(p4_quizzes)

print("Quiz count:", len(all_quizzes))
