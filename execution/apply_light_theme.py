import os

def update():
    comp_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components"

    # 1. Update StrategicInitiatives.jsx
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "r") as f:
        content = f.read()
    new_content = content.replace('className="section"', 'className="section section-light"')
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write(new_content)

    # 2. Update ClientProjects.jsx
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "r") as f:
        content = f.read()
    new_content = content.replace('className="section"', 'className="section section-light"')
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write(new_content)

    print("Light theme applied to project sections successfully!")

if __name__ == "__main__":
    update()
