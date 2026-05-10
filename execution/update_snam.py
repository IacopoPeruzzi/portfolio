import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update snam image
    content = content.replace('id: "snam",', 'id: "snam", heroImage: "/assets/projects/snam.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database updated: SNAM visual is now active!")

if __name__ == "__main__":
    update()
