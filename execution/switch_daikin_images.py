import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Swap heroImage and additionalImage for Daikin
    # Old: heroImage: "/assets/projects/daikin-app.png", additionalImage: "/assets/projects/daikin-controller.jpg"
    # New: heroImage: "/assets/projects/daikin-controller.jpg", additionalImage: "/assets/projects/daikin-app.png"
    
    content = content.replace('heroImage: "/assets/projects/daikin-app.png", additionalImage: "/assets/projects/daikin-controller.jpg"', 
                              'heroImage: "/assets/projects/daikin-controller.jpg", additionalImage: "/assets/projects/daikin-app.png"')
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print("Daikin images swapped successfully!")

if __name__ == "__main__":
    update()
