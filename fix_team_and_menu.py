import re
import glob

# 1. Remove duplicate mobile menu button in all HTML files
button_to_remove = r'<a href="contact\.html" class="mobile-cta".*?>Start Your Project</a>'

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove the second button
    html = re.sub(button_to_remove, '', html, flags=re.DOTALL)
    
    # Update CSS cache version
    html = re.sub(r'css/style\.css\?v=\d+', 'css/style.css?v=17', html)
    html = re.sub(r'css/style\.css"', 'css/style.css?v=17"', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Update contact.html with LinkedIn hover effects
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

# Define the team members replacement
team_html_old = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
              <div class="contact-method" style="margin-bottom: 0; padding: 1rem; cursor: default;">
                <div><strong>Chief Executive Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem;">Samruddhi Dudhe</span></div>
              </div>
              <div class="contact-method" style="margin-bottom: 0; padding: 1rem; cursor: default;">
                <div><strong>Chief Technology Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem;">Pranav Chavan</span></div>
              </div>
              <div class="contact-method" style="margin-bottom: 0; padding: 1rem; cursor: default;">
                <div><strong>Chief Operating Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem;">Abhay Potdar</span></div>
              </div>
              <div class="contact-method" style="margin-bottom: 0; padding: 1rem; cursor: default;">
                <div><strong>Chief Marketing Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem;">Prajwal Landge</span></div>
              </div>
            </div>
"""

team_html_new = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
              
              <div class="contact-method team-member-card" style="margin-bottom: 0; padding: 1rem; cursor: default; position: relative; overflow: hidden;">
                <div><strong>Chief Executive Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem; font-weight:bold;">Samruddhi Dudhe</span></div>
                <a href="https://www.linkedin.com/in/samruddhi-dudhe-50a031353" target="_blank" rel="noopener noreferrer" class="linkedin-hover-overlay">
                  <span>Connect on LinkedIn</span>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
              </div>
              
              <div class="contact-method team-member-card" style="margin-bottom: 0; padding: 1rem; cursor: default; position: relative; overflow: hidden;">
                <div><strong>Chief Technology Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem; font-weight:bold;">Pranav Chavan</span></div>
                <a href="https://www.linkedin.com/in/pranav-chavan-621b86392" target="_blank" rel="noopener noreferrer" class="linkedin-hover-overlay">
                  <span>Connect on LinkedIn</span>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
              </div>
              
              <div class="contact-method team-member-card" style="margin-bottom: 0; padding: 1rem; cursor: default; position: relative; overflow: hidden;">
                <div><strong>Chief Operating Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem; font-weight:bold;">Abhay Potdar</span></div>
                <a href="https://www.linkedin.com/in/abhayy-potdar?trk=contact-info" target="_blank" rel="noopener noreferrer" class="linkedin-hover-overlay">
                  <span>Connect on LinkedIn</span>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
              </div>
              
              <div class="contact-method team-member-card" style="margin-bottom: 0; padding: 1rem; cursor: default; position: relative; overflow: hidden;">
                <div><strong>Chief Marketing Officer</strong><br><span style="color:var(--text-muted);font-size:0.875rem; font-weight:bold;">Prajwal Landge</span></div>
              </div>
              
            </div>
"""

# Replace the HTML block
if team_html_old.strip() in contact_html:
    contact_html = contact_html.replace(team_html_old.strip(), team_html_new.strip())
else:
    # If indentation doesn't exactly match, try regex
    contact_html = re.sub(r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(140px, 1fr\)\); gap: 1rem; margin-bottom: 2rem;">.*?</div>\s*</div>\s*</div>\s*</div>', team_html_new.strip(), contact_html, flags=re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)


# 3. Add CSS for the linkedin hover effect
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Team Member LinkedIn Hover */
.team-member-card {
  transition: all 0.3s ease;
}
.linkedin-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #0077b5; /* LinkedIn Blue */
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  opacity: 0;
  transform: translateY(100%);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: inherit;
}
.team-member-card:hover .linkedin-hover-overlay {
  opacity: 1;
  transform: translateY(0);
}
.linkedin-hover-overlay svg {
  fill: white;
}
''')
