import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_track_content = '''
          <!-- Logo set 1 -->
          <div class="marquee-item"><span class="text-logo">Sanjeevani Hospital</span></div>
          <div class="marquee-item"><span class="text-logo">Stepup Solutions</span></div>
          <div class="marquee-item"><span class="text-logo">Cafe Brew</span></div>
          <div class="marquee-item"><span class="text-logo">CA Firms</span></div>
          <div class="marquee-item"><span class="text-logo">Dilip Abba Mobile Stores</span></div>
          
          <!-- Logo set 2 (Duplicate for infinite scroll) -->
          <div class="marquee-item"><span class="text-logo">Sanjeevani Hospital</span></div>
          <div class="marquee-item"><span class="text-logo">Stepup Solutions</span></div>
          <div class="marquee-item"><span class="text-logo">Cafe Brew</span></div>
          <div class="marquee-item"><span class="text-logo">CA Firms</span></div>
          <div class="marquee-item"><span class="text-logo">Dilip Abba Mobile Stores</span></div>
'''

html = re.sub(
    r'<div class="marquee-track">.*?</div>\s*</div>\s*</section>',
    f'<div class="marquee-track">\n{new_track_content}\n        </div>\n      </div>\n    </section>',
    html,
    flags=re.DOTALL
)

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_html = f.read()
    file_html = re.sub(r'css/style\.css\?v=\d+', 'css/style.css?v=18', file_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Add CSS for text-logo
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Text-based Logos for Marquee */
.text-logo {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
  letter-spacing: 2px;
  white-space: nowrap;
  display: inline-block;
  padding: 0 2rem;
  transition: color 0.3s ease;
}
.marquee-item:hover .text-logo {
  color: rgba(255, 255, 255, 0.8);
}
''')
