with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
body_start = text.find('<body')
main_start = text.find('<main>')
main_end = text.find('</main>')
modals_start = text.find('id="member-modal"')
script_start = text.find('<script>')
script_end = text.rfind('</script>')

print('style:', style_start, style_end)
print('body:', body_start)
print('main:', main_start, main_end)
print('modals:', modals_start)
print('script:', script_start, script_end)
