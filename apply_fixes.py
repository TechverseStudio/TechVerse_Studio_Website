import re
import glob

# Fix portfolio glitch by waiting for 'load' instead of 'DOMContentLoaded'
with open('js/portfolio.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('load', () => {")
with open('js/portfolio.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Fix video autoplay and preload in services.html (and portfolio.html if any)
for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Lazy loading for images (skip logo)
    def lazy_image(match):
        img_tag = match.group(0)
        if 'loading="lazy"' not in img_tag and 'logo.png' not in img_tag:
            # insert loading="lazy" before the closing bracket
            if img_tag.endswith('/>'):
                img_tag = img_tag[:-2] + ' loading="lazy" />'
            else:
                img_tag = img_tag[:-1] + ' loading="lazy">'
        return img_tag
        
    html = re.sub(r'<img\s+[^>]+>', lazy_image, html)
    
    # Fix video tags: replace preload="auto" with preload="metadata", and ensure autoplay is present if it's a looping background video
    def fix_video(match):
        vid_tag = match.group(0)
        # We want to add autoplay if it has loop and muted but doesn't have autoplay
        if 'loop' in vid_tag and 'muted' in vid_tag and 'autoplay' not in vid_tag:
            vid_tag = vid_tag.replace('loop', 'autoplay loop')
        # We want to change preload="auto" to preload="metadata" to save initial bandwidth but still allow fast play
        if 'preload="auto"' in vid_tag:
            vid_tag = vid_tag.replace('preload="auto"', 'preload="metadata"')
        return vid_tag

    html = re.sub(r'<video\s+[^>]+>', fix_video, html)
    
    # Bust cache for portfolio.js in portfolio.html just in case
    if html_file == 'portfolio.html':
        html = re.sub(r'js/portfolio\.js\?v=\d+', 'js/portfolio.js?v=2', html)
        if 'js/portfolio.js?v=' not in html and 'js/portfolio.js' in html:
            html = html.replace('js/portfolio.js', 'js/portfolio.js?v=2')
            
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied performance fixes.")
