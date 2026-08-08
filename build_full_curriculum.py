# Helper script to assemble complete curriculumData.ts

import json

# We will define quiz questions for all 40 lessons (5 per lesson)
# and interphasory quiz questions for all 4 phases (20 per phase)

def make_q(qid, question, options, correct_idx, exp):
    return {
        "id": qid,
        "question": question,
        "options": options,
        "correctIndex": correct_idx,
        "explanation": exp
    }

print("Script generator ready")
