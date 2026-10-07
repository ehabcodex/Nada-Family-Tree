import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_match = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
if style_match:
    css = style_match.group(1)
    # Find comments that look like section titles
    comments = re.findall(r'/\*\s*([^/*\n]+)\s*\*/', css)
    print("CSS sections count:", len(comments))
    for c in comments[:40]:
        print(" -", c.strip())
