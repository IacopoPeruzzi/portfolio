import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Remove previous wrong mapping attempt (if any)
    # Resetting the fields to be sure
    content = content.replace('heroImage: "/src/assets/projects/clea-ecosystem.jpg",', '')
    content = content.replace('heroImage: "/src/assets/projects/ciam.jpg",', '')
    
    # Correct Mapping
    mapping = {
        "oobe": "oobe.jpg",
        "zoppas": "zoppas.jpg",
        "quanta": "quanta.jpg",
        "daikin": "daikin-app.jpg"
    }
    
    for pid, img in mapping.items():
        content = content.replace(f'id: "{pid}",', f'id: "{pid}", heroImage: "/src/assets/projects/{img}",')
    
    # Special case for Daikin second image
    content = content.replace('id: "daikin",', 'id: "daikin", additionalImage: "/src/assets/projects/daikin-controller.jpg",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Project database updated with corrected mapping and secondary images!")

if __name__ == "__main__":
    update()
