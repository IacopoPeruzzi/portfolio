import os
import re

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Precise cleanup
    content = re.sub(r'heroImage: ".*?",', '', content)
    content = re.sub(r'additionalImage: ".*?",', '', content)

    # Ultra Final Mapping
    mapping = {
        'id: "oobe",': 'id: "oobe", heroImage: "/assets/projects/oobe.jpg",',
        'id: "zoppas",': 'id: "zoppas", heroImage: "/assets/projects/zoppas.png",',
        'id: "quanta",': 'id: "quanta", heroImage: "/assets/projects/quanta.jpg",',
        'id: "daikin",': 'id: "daikin", heroImage: "/assets/projects/daikin-app.png", additionalImage: "/assets/projects/daikin-controller.jpg",'
    }
    
    for old, new in mapping.items():
        content = content.replace(old, new)
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database mapping fixed once and for all!")

if __name__ == "__main__":
    update()
