import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_track_content = '''
          <!-- Logo set 1 -->
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/sanjeevani.png" alt="Sanjeevani Logo">
            <span class="text-logo">Sanjeevani Hospital</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/stepup.png" alt="Stepup Logo">
            <span class="text-logo">Stepup Solutions</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/cafe.png" alt="Cafe Brew Logo">
            <span class="text-logo">Cafe Brew</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/ca.png" alt="CA Firms Logo">
            <span class="text-logo">CA Firms</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/dilip_mobile.png" alt="Dilip Mobile Logo">
            <span class="text-logo">Dilip Mobile Stores</span>
          </div>
          
          <!-- Logo set 2 (Duplicate for infinite scroll) -->
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/sanjeevani.png" alt="Sanjeevani Logo">
            <span class="text-logo">Sanjeevani Hospital</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/stepup.png" alt="Stepup Logo">
            <span class="text-logo">Stepup Solutions</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/cafe.png" alt="Cafe Brew Logo">
            <span class="text-logo">Cafe Brew</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/ca.png" alt="CA Firms Logo">
            <span class="text-logo">CA Firms</span>
          </div>
          <div class="marquee-item client-logo">
            <img src="assets/images/logos/dilip_mobile.png" alt="Dilip Mobile Logo">
            <span class="text-logo">Dilip Mobile Stores</span>
          </div>
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
    file_html = re.sub(r'css/style\.css\?v=\d+', 'css/style.css?v=19', file_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Client Logo Flex Container */
.client-logo {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 0 1rem;
}
.client-logo img {
  height: 40px;
  width: 40px;
  border-radius: 8px;
  object-fit: cover;
  transition: all 0.3s ease;
  filter: grayscale(100%) opacity(0.7);
}
.marquee-item:hover .client-logo img {
  filter: grayscale(0%) opacity(1);
  box-shadow: 0 0 15px rgba(0, 191, 255, 0.3);
}
.text-logo {
  padding: 0 !important;
}
''')
