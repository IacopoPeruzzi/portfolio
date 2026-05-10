import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/CaseStudy.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # New Header Structure: Image first, then Title
    new_header = '''
      <div className="container" style={{paddingTop: '120px'}}>
        <Link to="/" className="back-link" style={{marginBottom: '40px', display: 'inline-block', textDecoration: 'none'}}>← Back to Portfolio</Link>
        
        {project.heroImage && (
          <div className="cs-hero-image" style={{marginTop: '40px', marginBottom: '80px'}}>
            <img src={project.heroImage} alt={project.title} />
          </div>
        )}

        <h1 className="hero-title reveal">{project.title}</h1>
        <p className="hero-subtitle reveal">{project.subtitle}</p>
      </div>
    '''
    
    # Replace the container inside the hero header
    # (Using a simpler search/replace based on markers)
    import re
    content = re.sub(r'<header className="hero section">.*?</header>', f'<header className="hero section">{new_header}</header>', content, flags=re.DOTALL)

    with open(file_path, "w") as f:
        f.write(content)
    
    print("Case Study layout refined: Hero Image is now prominent!")

if __name__ == "__main__":
    update()
