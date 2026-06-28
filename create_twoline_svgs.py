import os

logo_dir = 'assets/images/logos'
os.makedirs(logo_dir, exist_ok=True)

# 1. Sanjeevani Hospital
svg_sanjeevani = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 120" width="350" height="120">
  <defs>
    <linearGradient id="gradS" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00C9FF" />
      <stop offset="100%" stop-color="#92FE9D" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 20) scale(1.4)">
    <rect x="20" y="0" width="16" height="56" rx="4" fill="url(#gradS)" opacity="0.9"/>
    <rect x="0" y="20" width="56" height="16" rx="4" fill="url(#gradS)" opacity="0.9"/>
    <path d="M 38 6 C 60 6, 60 33, 38 33 C 27 33, 27 6, 38 6 Z" fill="#92FE9D" opacity="0.8"/>
  </g>
  <text x="110" y="55" font-family="'Inter', 'Segoe UI', sans-serif" font-size="46" font-weight="900" fill="#E0E0E0" letter-spacing="1">Sanjeevani</text>
  <text x="110" y="105" font-family="'Inter', 'Segoe UI', sans-serif" font-size="46" font-weight="300" fill="#A0A0A0" letter-spacing="1">Hospital</text>
</svg>"""

# 2. Stepup Solutions
svg_stepup = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 120" width="350" height="120">
  <defs>
    <linearGradient id="gradSt" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8A2EFF" />
      <stop offset="100%" stop-color="#00BFFF" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 25) scale(1.4)">
    <rect x="0" y="32" width="14" height="16" rx="3" fill="url(#gradSt)"/>
    <rect x="18" y="16" width="14" height="32" rx="3" fill="url(#gradSt)"/>
    <rect x="36" y="0" width="14" height="48" rx="3" fill="url(#gradSt)"/>
    <path d="M 54 0 L 68 14 L 54 28 Z" fill="#00BFFF"/>
  </g>
  <text x="120" y="55" font-family="'Montserrat', sans-serif" font-size="46" font-weight="900" fill="#FFFFFF" letter-spacing="1">STEPUP</text>
  <text x="120" y="105" font-family="'Montserrat', sans-serif" font-size="46" font-weight="400" fill="#00BFFF" letter-spacing="1">SOLUTIONS</text>
</svg>"""

# 3. Cafe Brew
svg_cafe = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 120" width="250" height="120">
  <defs>
    <linearGradient id="gradC" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF8C00" />
      <stop offset="100%" stop-color="#FF3D00" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 20) scale(1.4)">
    <path d="M 6 14 Q 6 60, 34 60 Q 60 60, 60 14 Z" fill="none" stroke="url(#gradC)" stroke-width="5" stroke-linecap="round"/>
    <path d="M 60 20 Q 74 20, 74 34 Q 74 48, 60 48" fill="none" stroke="url(#gradC)" stroke-width="4" stroke-linecap="round"/>
    <path d="M 28 0 Q 35 -7, 28 -14" fill="none" stroke="#FF8C00" stroke-width="3" stroke-linecap="round"/>
    <path d="M 42 4 Q 49 -3, 42 -10" fill="none" stroke="#FF3D00" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="120" y="55" font-family="'Playfair Display', serif, sans-serif" font-size="52" font-weight="900" fill="#FF8C00" letter-spacing="1">Cafe</text>
  <text x="120" y="105" font-family="'Playfair Display', serif, sans-serif" font-size="52" font-weight="400" fill="#FFFFFF" letter-spacing="1">Brew</text>
</svg>"""

# 4. CA Firms
svg_ca = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 120" width="250" height="120">
  <defs>
    <linearGradient id="gradCA" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFD700" />
      <stop offset="100%" stop-color="#DAA520" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 20) scale(1.4)">
    <path d="M 26 0 L 52 14 L 52 40 Q 26 66, 0 40 L 0 14 Z" fill="none" stroke="url(#gradCA)" stroke-width="4" stroke-linejoin="round"/>
    <polyline points="14,46 20,34 32,40 40,20" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="100" y="55" font-family="'Georgia', serif" font-size="46" font-weight="900" fill="#FFD700" letter-spacing="2">CA</text>
  <text x="100" y="105" font-family="'Georgia', serif" font-size="46" font-weight="300" fill="#E0E0E0" letter-spacing="2">FIRMS</text>
</svg>"""

# 5. Dilip Mobile Stores
svg_dilip = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 120" width="380" height="120">
  <defs>
    <linearGradient id="gradD" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4FACFE" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 20) scale(1.4)">
    <rect x="14" y="0" width="32" height="60" rx="5" fill="none" stroke="url(#gradD)" stroke-width="4"/>
    <circle cx="30" cy="52" r="3" fill="#00F2FE"/>
    <path d="M 54 20 Q 60 14, 68 20" fill="none" stroke="#4FACFE" stroke-width="3" stroke-linecap="round"/>
    <path d="M 50 10 Q 60 0, 70 10" fill="none" stroke="#00F2FE" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="120" y="55" font-family="'Roboto', sans-serif" font-size="46" font-weight="900" fill="#FFFFFF" letter-spacing="1">DILIP</text>
  <text x="120" y="105" font-family="'Roboto', sans-serif" font-size="46" font-weight="300" fill="#00F2FE" letter-spacing="1">MOBILE STORES</text>
</svg>"""

with open(f'{logo_dir}/sanjeevani.svg', 'w', encoding='utf-8') as f: f.write(svg_sanjeevani)
with open(f'{logo_dir}/stepup.svg', 'w', encoding='utf-8') as f: f.write(svg_stepup)
with open(f'{logo_dir}/cafe.svg', 'w', encoding='utf-8') as f: f.write(svg_cafe)
with open(f'{logo_dir}/ca.svg', 'w', encoding='utf-8') as f: f.write(svg_ca)
with open(f'{logo_dir}/dilip_mobile.svg', 'w', encoding='utf-8') as f: f.write(svg_dilip)

print("Generated two-line SVGs successfully.")
