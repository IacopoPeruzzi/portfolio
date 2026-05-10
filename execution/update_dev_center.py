import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update dev-center image
    content = content.replace('id: "dev-center",', 'id: "dev-center", heroImage: "/assets/projects/dev-center.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database updated: Developer Center visual is now active!")

if __name__ == "__main__":
    update()
