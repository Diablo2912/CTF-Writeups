import re

# Load the HTML content
with open('flag.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Regex: Match exactly uppercase 'NYP{...}' across lines
flags = re.findall(r'NYP\{.*?\}', html, flags=re.DOTALL)

flags = [flag for flag in flags if flag.startswith('NYP{')]

# Show results
for i, flag in enumerate(flags):
    print(f"[{i+1}] {flag}")
