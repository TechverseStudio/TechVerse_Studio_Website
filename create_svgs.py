import os

logo_dir = 'assets/images/logos'
os.makedirs(logo_dir, exist_ok=True)

svg_sanjeevani = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 80" width="300" height="80">
  <defs>
    <linearGradient id="gradS" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00C9FF" />
      <stop offset="100%" stop-color="#92FE9D" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 15)">
    <!-- Medical Cross -->
    <rect x="15" y="0" width="12" height="42" rx="3" fill="url(#gradS)" opacity="0.9"/>
    <rect x="0" y="15" width="42" height="12" rx="3" fill="url(#gradS)" opacity="0.9"/>
    <!-- Leaf -->
    <path d="M 28 5 C 45 5, 45 25, 28 25 C 20 25, 20 5, 28 5 Z" fill="#92FE9D" opacity="0.8"/>
  </g>
  <text x="65" y="48" font-family="'Inter', 'Segoe UI', sans-serif" font-size="22" font-weight="700" fill="#E0E0E0" letter-spacing="1">Sanjeevani</text>
  <text x="210" y="48" font-family="'Inter', 'Segoe UI', sans-serif" font-size="22" font-weight="300" fill="#A0A0A0" letter-spacing="1">Hospital</text>
</svg>"""

svg_stepup = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 80" width="280" height="80">
  <defs>
    <linearGradient id="gradSt" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8A2EFF" />
      <stop offset="100%" stop-color="#00BFFF" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 20)">
    <!-- Ascending Steps -->
    <rect x="0" y="24" width="10" height="12" rx="2" fill="url(#gradSt)"/>
    <rect x="14" y="12" width="10" height="24" rx="2" fill="url(#gradSt)"/>
    <rect x="28" y="0" width="10" height="36" rx="2" fill="url(#gradSt)"/>
    <!-- Arrow -->
    <path d="M 42 0 L 52 10 L 42 20 Z" fill="#00BFFF"/>
  </g>
  <text x="75" y="48" font-family="'Montserrat', sans-serif" font-size="24" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">STEPUP</text>
  <text x="180" y="48" font-family="'Montserrat', sans-serif" font-size="24" font-weight="400" fill="#00BFFF" letter-spacing="0.5">SOLUTIONS</text>
</svg>"""

svg_cafe = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 80" width="220" height="80">
  <defs>
    <linearGradient id="gradC" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF8C00" />
      <stop offset="100%" stop-color="#FF3D00" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 15)">
    <!-- Coffee Cup Outline -->
    <path d="M 5 10 Q 5 45, 25 45 Q 45 45, 45 10 Z" fill="none" stroke="url(#gradC)" stroke-width="4" stroke-linecap="round"/>
    <!-- Handle -->
    <path d="M 45 15 Q 55 15, 55 25 Q 55 35, 45 35" fill="none" stroke="url(#gradC)" stroke-width="3" stroke-linecap="round"/>
    <!-- Steam -->
    <path d="M 20 0 Q 25 -5, 20 -10" fill="none" stroke="#FF8C00" stroke-width="2" stroke-linecap="round"/>
    <path d="M 30 2 Q 35 -3, 30 -8" fill="none" stroke="#FF3D00" stroke-width="2" stroke-linecap="round"/>
  </g>
  <text x="75" y="45" font-family="'Playfair Display', serif, sans-serif" font-size="26" font-weight="700" fill="#FF8C00" letter-spacing="1.5">Cafe</text>
  <text x="140" y="45" font-family="'Playfair Display', serif, sans-serif" font-size="26" font-weight="400" fill="#FFFFFF" letter-spacing="1.5">Brew</text>
</svg>"""

svg_ca = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 80" width="180" height="80">
  <defs>
    <linearGradient id="gradCA" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFD700" />
      <stop offset="100%" stop-color="#DAA520" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 15)">
    <!-- Shield -->
    <path d="M 20 0 L 40 10 L 40 30 Q 20 50, 0 30 L 0 10 Z" fill="none" stroke="url(#gradCA)" stroke-width="3" stroke-linejoin="round"/>
    <!-- Chart -->
    <polyline points="10,35 15,25 25,30 30,15" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="60" y="45" font-family="'Georgia', serif" font-size="24" font-weight="700" fill="#FFD700" letter-spacing="2">CA</text>
  <text x="105" y="45" font-family="'Georgia', serif" font-size="24" font-weight="300" fill="#E0E0E0" letter-spacing="2">FIRMS</text>
</svg>"""

svg_dilip = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 80" width="320" height="80">
  <defs>
    <linearGradient id="gradD" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4FACFE" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 15)">
    <!-- Smartphone -->
    <rect x="10" y="0" width="24" height="46" rx="4" fill="none" stroke="url(#gradD)" stroke-width="3"/>
    <circle cx="22" cy="40" r="2" fill="#00F2FE"/>
    <!-- Signal -->
    <path d="M 40 15 Q 45 10, 50 15" fill="none" stroke="#4FACFE" stroke-width="2" stroke-linecap="round"/>
    <path d="M 38 7 Q 45 0, 52 7" fill="none" stroke="#00F2FE" stroke-width="2" stroke-linecap="round"/>
  </g>
  <text x="75" y="45" font-family="'Roboto', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF" letter-spacing="1">DILIP</text>
  <text x="145" y="45" font-family="'Roboto', sans-serif" font-size="22" font-weight="300" fill="#00F2FE" letter-spacing="1">MOBILE STORES</text>
</svg>"""

with open(f'{logo_dir}/sanjeevani.svg', 'w', encoding='utf-8') as f: f.write(svg_sanjeevani)
with open(f'{logo_dir}/stepup.svg', 'w', encoding='utf-8') as f: f.write(svg_stepup)
with open(f'{logo_dir}/cafe.svg', 'w', encoding='utf-8') as f: f.write(svg_cafe)
with open(f'{logo_dir}/ca.svg', 'w', encoding='utf-8') as f: f.write(svg_ca)
with open(f'{logo_dir}/dilip_mobile.svg', 'w', encoding='utf-8') as f: f.write(svg_dilip)

print("Generated 5 SVGs successfully.")
