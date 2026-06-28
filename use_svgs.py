import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_track_content = '''
          <!-- Logo set 1 -->
          <div class="marquee-item"><img src="assets/images/logos/sanjeevani.svg" alt="Sanjeevani Hospital Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/stepup.svg" alt="Stepup Solutions Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/cafe.svg" alt="Cafe Brew Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/ca.svg" alt="CA Firms Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/dilip_mobile.svg" alt="Dilip Mobile Stores Logo" class="full-svg-logo"></div>
          
          <!-- Logo set 2 (Duplicate for infinite scroll) -->
          <div class="marquee-item"><img src="assets/images/logos/sanjeevani.svg" alt="Sanjeevani Hospital Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/stepup.svg" alt="Stepup Solutions Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/cafe.svg" alt="Cafe Brew Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/ca.svg" alt="CA Firms Logo" class="full-svg-logo"></div>
          <div class="marquee-item"><img src="assets/images/logos/dilip_mobile.svg" alt="Dilip Mobile Stores Logo" class="full-svg-logo"></div>
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
    file_html = re.sub(r'css/style\.css\?v=\d+', 'css/style.css?v=21', file_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old client-logo stuff
css = re.sub(r'/\* Client Logo Flex Container \*/.*?(?=\n\n|\Z)', '', css, flags=re.DOTALL)

refined_css = '''
/* Full SVG Logo Marquee */
.full-svg-logo {
  height: 60px;
  width: auto;
  opacity: 0.6;
  filter: grayscale(100%);
  transition: all 0.4s ease;
  padding: 0 1rem;
}
.marquee-item:hover .full-svg-logo {
  opacity: 1;
  filter: grayscale(0%);
  transform: scale(1.05);
}
'''

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css.strip() + '\n\n' + refined_css.strip() + '\n')
