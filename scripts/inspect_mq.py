import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Google fonts link
import re
print("Link tags:")
for m in re.finditer(r'<link[^>]+>', text):
    print(m.group(0))

# Let's see the beginning of <style>
style_start = text.find('<style>')
style_end = text.find('</style>')
print(f"Style tag length: {style_end - style_start} characters")

# Check if there are media queries
media_queries = re.findall(r'@media[^{]+', text)
print(f"Media queries count: {len(media_queries)}")
for mq in set(media_queries):
    print(" ", mq.strip())
