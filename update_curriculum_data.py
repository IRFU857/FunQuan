import json
import re

# Read original curriculum file
with open('/src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original content length:", len(content))
