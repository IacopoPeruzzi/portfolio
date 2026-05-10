import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update title and add image
    content = content.replace('title: "Clea AI Studio",', 'title: "Clea Studio AI", heroImage: "/assets/projects/studio-ai.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database updated: Clea Studio AI is now active with its visual!")

if __name__ == "__main__":
    update()
