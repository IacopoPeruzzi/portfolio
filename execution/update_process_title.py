import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/Process.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update title with dynamic classes
    new_content = content.replace('<h2>A strategic approach to complexity.</h2>', '<h2 className="dynamic-title reveal">A strategic approach to complexity.</h2>')
    new_content = new_content.replace('className="section"', 'className="section reveal"')
    
    with open(file_path, "w") as f:
        f.write(new_content)
    
    print("Process section title and animations updated!")

if __name__ == "__main__":
    update()
