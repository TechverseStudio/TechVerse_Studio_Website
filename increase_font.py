import os, re
logo_dir = 'assets/images/logos'
for f in os.listdir(logo_dir):
    if f.endswith('.svg'):
        path = os.path.join(logo_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Increase font size attributes
        def increase_font(match):
            size = int(match.group(1))
            return f'font-size="{size + 8}"'
        
        content = re.sub(r'font-size="(\d+)"', increase_font, content)
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
