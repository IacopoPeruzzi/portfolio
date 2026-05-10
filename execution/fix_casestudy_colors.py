import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/CaseStudy.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Remove specific white text overrides
    new_content = content.replace("color: '#fff'", "")
    new_content = new_content.replace('color: "#fff"', "")
    new_content = new_content.replace('color: "var(--text-secondary)"', "") # Let CSS handle it
    new_content = new_content.replace("background: 'var(--surface-color)'", "background: '#f5f5f7'")
    
    with open(file_path, "w") as f:
        f.write(new_content)
    
    print("CaseStudy component colors updated to light theme!")

if __name__ == "__main__":
    update()
