import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/Process.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Remove reveal from section, keep it on the title
    new_content = content.replace('className="section reveal"', 'className="section"')
    # Ensure title has reveal
    if 'className="dynamic-title reveal"' not in new_content:
        new_content = new_content.replace('<h2 className="dynamic-title">', '<h2 className="dynamic-title reveal">')
    
    with open(file_path, "w") as f:
        f.write(new_content)
    
    print("Process section visibility fixed!")

if __name__ == "__main__":
    update()
