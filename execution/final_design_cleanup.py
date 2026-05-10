import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/index.css"
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Remove all backdrop-filter and filter: blur
    import re
    content = re.sub(r'backdrop-filter:.*?;', 'backdrop-filter: none !important;', content)
    content = re.sub(r'filter: blur\(.*?\);', 'filter: none !important;', content)
    
    # 2. Fix the Light Mode overrides that were turning card text black
    # Targeted removal of card-related color overrides in body.is-light
    content = content.replace('body.is-light .card h3 {', 'body.is-light .ignore-this {')
    content = content.replace('body.is-light .card span {', 'body.is-light .ignore-this {')
    
    # 3. Add explicit rule for card stability
    final_rules = '''
/* FINAL CARD STABILITY RULES */
.card, .card-content, .card h3, .card p, .card span, .card .tag {
  color: #FFFFFF !important;
}

.card-overlay {
  background: linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%) !important;
  backdrop-filter: none !important;
}

.card .tag {
  background: rgba(255, 255, 255, 0.1) !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  backdrop-filter: none !important;
}
'''
    content += final_rules
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("CSS Cleaned: No blur, card titles forced to white.")

if __name__ == "__main__":
    update()
