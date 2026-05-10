import os

def update():
    file_path = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src/components/CaseStudy.jsx"
    with open(file_path, "r") as f:
        content = f.read()
    
    # Block for additional image
    additional_image_jsx = '''
      {project.additionalImage && (
        <section className="section" style={{padding: '0 20px'}}>
          <div className="container">
            <div className="cs-hero-image" style={{marginTop: '0', marginBottom: '80px'}}>
              <img src={project.additionalImage} alt="Project Detail" />
            </div>
          </div>
        </section>
      )}
    '''
    
    # Insert after Key Design Decisions section
    if '</section>' in content:
        # Finding the second occurrence of </section> (after snapshot) is not reliable
        # Let's target the end of the Decisions section
        content = content.replace('{project.decisions.map((d, i) => (', additional_image_jsx + '{project.decisions.map((d, i) => (')

    with open(file_path, "w") as f:
        f.write(content)
    
    print("CaseStudy component updated with support for secondary images!")

if __name__ == "__main__":
    update()
