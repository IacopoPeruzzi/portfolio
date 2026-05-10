import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update app-hub image
    content = content.replace('id: "app-hub",', 'id: "app-hub", heroImage: "/assets/projects/app-hub.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database updated: Application Hub visual is now active!")

if __name__ == "__main__":
    update()
