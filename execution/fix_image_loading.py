import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/CaseStudy.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # We will use a helper to resolve the path or just fix the strings
    # In Vite, if we use /src/assets/... it should work in dev, but let's be sure.
    # A more robust way for dynamic images in Vite is to place them in 'public' 
    # OR use a specific path if they are in 'src/assets'
    
    # Let's try to make the paths absolute relative to the project root for now
    # or just ensure they are clean.
    
    # Actually, let's move the projects folder to 'public/assets/projects' 
    # for easier dynamic access without Vite's asset processing issues.
    
    print("Preparing to move assets to public folder for better dynamic access...")

if __name__ == "__main__":
    update()

# Move assets to public directory
mkdir -p /Users/iacopoperuzzi/Documents/projects/portfolio/web-app/public/assets/projects
cp -r /Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/assets/projects/* /Users/iacopoperuzzi/Documents/projects/portfolio/web-app/public/assets/projects/

# Update database paths
python3 -c "
path = '/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/data/projects.js'
with open(path, 'r') as f: content = f.read()
new_content = content.replace('/src/assets/projects/', '/assets/projects/')
with open(path, 'w') as f: f.write(new_content)
"
