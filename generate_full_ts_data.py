import sys

# Script to assemble the final curriculumData.ts

with open('/src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    orig = f.read()

print("Original file read.")
