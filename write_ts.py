import re
import json
from patch_curriculum import make_interphasory_quiz
from generate_all_curriculum import p1_quizzes
from enrich_all_lessons import p2_quizzes, p3_quizzes
from generate_final_curriculum_ts import p4_quizzes

# Combine all lesson quizzes
all_quizzes = {}
all_quizzes.update(p1_quizzes)
all_quizzes.update(p2_quizzes)
all_quizzes.update(p3_quizzes)
all_quizzes.update(p4_quizzes)

with open('src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

print("File opened successfully. Total chars:", len(text))

# For each lesson ID, update its quiz field
for lid, q_list in all_quizzes.items():
    pattern = rf"(id:\s*['\"]{lid}['\"].*?quiz:\s*\[)(.*?)(\],\s*codingChallenge)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        prefix = match.group(1)
        suffix = match.group(3)
        formatted_qs = []
        for q_obj in q_list:
            opts = json.dumps(q_obj['options'])
            exp = json.dumps(q_obj['explanation'])
            q_str = f"""{{
            id: {json.dumps(q_obj['id'])},
            question: {json.dumps(q_obj['question'])},
            options: {opts},
            correctIndex: {q_obj['correctIndex']},
            explanation: {exp}
          }}"""
            formatted_qs.append(q_str)
        
        replacement = prefix + "\n          " + ",\n          ".join(formatted_qs) + "\n        " + suffix
        text = text[:match.start()] + replacement + text[match.end():]
    else:
        print(f"Warning: Could not match quiz for lesson {lid}")

# Now add interphasoryQuiz to each phase
for p_num in range(1, 5):
    p_inter = make_interphasory_quiz(p_num)
    formatted_inter = []
    for q_obj in p_inter:
        opts = json.dumps(q_obj['options'])
        exp = json.dumps(q_obj['explanation'])
        q_str = f"""{{
        id: {json.dumps(q_obj['id'])},
        question: {json.dumps(q_obj['question'])},
        options: {opts},
        correctIndex: {q_obj['correctIndex']},
        explanation: {exp}
      }}"""
        formatted_inter.append(q_str)
    
    inter_block = "interphasoryQuiz: [\n        " + ",\n        ".join(formatted_inter) + "\n      ]\n    }"
    
    # Locate end of phase lessons array
    p_match = re.search(rf"(id:\s*{p_num},.*?lessons:\s*\[.*?\]\s*)(\n\s*\}}|\n\s*,\n)", text, re.DOTALL)
    if p_match:
        text = text[:p_match.start(2)] + ",\n      " + inter_block + text[p_match.end(2):]
        print(f"Added interphasory quiz for Phase {p_num}")
    else:
        print(f"Warning: Could not match Phase {p_num}")

# Save updated file
with open('src/data/curriculumData.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated curriculumData.ts written successfully.")
