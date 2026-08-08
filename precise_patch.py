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

with open('src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

print("Read file, length:", len(text))

# Function to replace quiz array for a lesson
for lid, q_list in all_quizzes.items():
    # Find position of id: 'lid'
    pos = text.find(f"id: '{lid}'")
    if pos == -1:
        pos = text.find(f'id: "{lid}"')
    
    if pos != -1:
        # Find 'quiz:' after pos
        quiz_pos = text.find('quiz:', pos)
        if quiz_pos != -1:
            # Find the opening bracket '['
            bracket_open = text.find('[', quiz_pos)
            # Find matching closing bracket ']' by tracking bracket depth
            depth = 0
            bracket_close = -1
            for i in range(bracket_open, len(text)):
                if text[i] == '[':
                    depth += 1
                elif text[i] == ']':
                    depth -= 1
                    if depth == 0:
                        bracket_close = i
                        break
            
            if bracket_close != -1:
                # Format new quiz questions
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
                
                new_quiz_str = "[\n          " + ",\n          ".join(formatted_qs) + "\n        ]"
                text = text[:bracket_open] + new_quiz_str + text[bracket_close + 1:]
                print(f"Successfully updated quiz for {lid}")
            else:
                print(f"Error: closing bracket not found for {lid}")
        else:
            print(f"Error: quiz: not found for {lid}")
    else:
        print(f"Error: lesson id {lid} not found")

# Now add interphasoryQuiz to each phase
for p_num in range(1, 5):
    # Find phase id: p_num
    pos = text.find(f"id: {p_num},\n    title:")
    if pos == -1:
        pos = text.find(f"id: {p_num},")
    
    if pos != -1:
        # Find lessons: [ for this phase
        lessons_pos = text.find("lessons: [", pos)
        if lessons_pos != -1:
            # Find closing bracket for lessons array
            depth = 0
            lessons_close = -1
            for i in range(lessons_pos + 8, len(text)):
                if text[i] == '[':
                    depth += 1
                elif text[i] == ']':
                    depth -= 1
                    if depth == 0:
                        lessons_close = i
                        break
            
            if lessons_close != -1:
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
                
                inter_block = ",\n      interphasoryQuiz: [\n        " + ",\n        ".join(formatted_inter) + "\n      ]"
                
                # Check if interphasoryQuiz already exists in this phase
                next_close_brace = text.find("}", lessons_close)
                if "interphasoryQuiz" not in text[lessons_close:next_close_brace]:
                    text = text[:lessons_close + 1] + inter_block + text[lessons_close + 1:]
                    print(f"Successfully added interphasoryQuiz for Phase {p_num}")
                else:
                    print(f"interphasoryQuiz already present for Phase {p_num}")

# Save updated file
with open('src/data/curriculumData.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("All updates applied cleanly!")
