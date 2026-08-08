import re
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

print(f"Total quiz sets mapped: {len(all_quizzes)}")

# Read original curriculumData.ts text
with open('src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect all lesson IDs present in content
lesson_ids = re.findall(r"id:\s*['\"](lesson-\d+-\d+)['\"]", content)
print("Found lesson IDs:", lesson_ids)
