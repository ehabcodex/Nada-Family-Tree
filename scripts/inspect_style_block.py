with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
print(f"Style start: {style_start}, end: {style_end}, len: {style_end - style_start}")

# Print first 200 lines of style
style_lines = text[style_start:style_end].split('\n')
print(f"Total lines in style: {len(style_lines)}")
print('\n'.join(style_lines[:60]))
