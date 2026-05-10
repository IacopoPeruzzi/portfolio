import subprocess
import os
import shutil
import sys

def run_command(command, cwd=None):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    return True

def setup_vite():
    project_path = "/Users/iacopoperuzzi/Documents/projects/portfolio"
    web_app_dir = os.path.join(project_path, "web-app")

    if os.path.exists(web_app_dir):
        print(f"Directory {web_app_dir} already exists. Skipping initialization.")
    else:
        # 1. Create Vite project (React template)
        print("Initializing Vite project...")
        success = run_command(f"npx -y create-vite@latest web-app --template react --no-interactive", cwd=project_path)
        if not success: return

    # 2. Install dependencies
    print("Installing dependencies...")
    success = run_command("npm install", cwd=web_app_dir)
    if not success: return

    # 3. Clean boilerplate
    print("Cleaning boilerplate...")
    src_dir = os.path.join(web_app_dir, "src")
    files_to_remove = ["App.css", "assets/react.svg"]
    for f in files_to_remove:
        path = os.path.join(src_dir, f)
        if os.path.exists(path):
            os.remove(path)
            print(f"Removed {f}")
    
    # 4. Reset App.jsx
    app_jsx_path = os.path.join(src_dir, "App.jsx")
    with open(app_jsx_path, "w") as f:
        f.write('function App() {\n  return (\n    <div className="app-container">\n      <h1>Portfolio in costruzione</h1>\n    </div>\n  );\n}\n\nexport default App;\n')

    # 5. Set Premium CSS Base
    index_css_path = os.path.join(src_dir, "index.css")
    premium_css = """
:root {
  --bg-color: #0a0a0a;
  --text-color: #f5f5f7;
  --accent-color: #0071e3;
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-border: rgba(255, 255, 255, 0.1);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-color);
  color: var(--text-color);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: radial-gradient(circle at top right, #1a1a1a, #0a0a0a);
}

h1 {
  font-weight: 700;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #fff 0%, #888 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
"""
    with open(index_css_path, "w") as f:
        f.write(premium_css)

    print("Setup completed successfully!")

if __name__ == "__main__":
    setup_vite()
