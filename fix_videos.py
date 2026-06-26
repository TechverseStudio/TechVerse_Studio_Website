import re
with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'autoplay loop muted playsinline', r'preload="metadata" loop muted playsinline', html)
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)
