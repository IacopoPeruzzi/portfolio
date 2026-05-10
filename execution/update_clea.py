import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Update clea-ecosystem image
    content = content.replace('id: "clea-ecosystem",', 'id: "clea-ecosystem", heroImage: "/assets/projects/clea-ecosystem.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database updated: Clea Ecosystem visual is now active!")

if __name__ == "__main__":
    update()
