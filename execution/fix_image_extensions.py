import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Correcting extensions for Daikin (they were PNGs)
    content = content.replace('heroImage: "/src/assets/projects/daikin-app.jpg",', 'heroImage: "/src/assets/projects/daikin-app.png",')
    content = content.replace('additionalImage: "/src/assets/projects/daikin-controller.jpg",', 'additionalImage: "/src/assets/projects/daikin-controller.png",')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Database image extensions fixed!")

if __name__ == "__main__":
    update()
