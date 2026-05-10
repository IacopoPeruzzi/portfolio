import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Precise cleanup of the image fields to avoid duplicates
    import re
    content = re.sub(r'heroImage: ".*?",', '', content)
    content = re.sub(r'additionalImage: ".*?",', '', content)

    # Correct Mapping
    # OOBE -> oobe.jpg
    # Zoppas -> zoppas.jpg
    # Quanta -> quanta.jpg
    # Daikin -> daikin-app.png + daikin-controller.png
    
    mapping = {
        'id: "oobe",': 'id: "oobe", heroImage: "/assets/projects/oobe.jpg",',
        'id: "zoppas",': 'id: "zoppas", heroImage: "/assets/projects/zoppas.jpg",',
        'id: "quanta",': 'id: "quanta", heroImage: "/assets/projects/quanta.jpg",',
        'id: "daikin",': 'id: "daikin", heroImage: "/assets/projects/daikin-app.png", additionalImage: "/assets/projects/daikin-controller.png",'
    }
    
    for old, new in mapping.items():
        content = content.replace(old, new)
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Mapping fixed correctly!")

if __name__ == "__main__":
    update()
