import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Map images to IDs
    mapping = {
        "clea-ecosystem": "clea-ecosystem.jpg",
        "daikin": "daikin.jpg",
        "quanta": "quanta.jpg",
        "ciam": "ciam.jpg",
        "zoppas": "zoppas.jpg"
    }
    
    for pid, img in mapping.items():
        # Update heroImage field for each project
        # This is a bit tricky with string replace, but we know the structure
        content = content.replace(f'id: "{pid}",', f'id: "{pid}", heroImage: "/src/assets/projects/{img}",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Project database updated with image paths!")

if __name__ == "__main__":
    update()
