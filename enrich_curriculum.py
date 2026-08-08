import re
import json

# Read current file
with open('/src/data/curriculumData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

print("File loaded. Preparing questions...")
