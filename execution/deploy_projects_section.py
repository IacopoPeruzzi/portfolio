import os

def deploy():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    components_dir = os.path.join(src_dir, "components")
    
    # 1. Projects Component
    projects_code = """
import React from 'react';

const projects = [
  {
    id: 1,
    title: "SNAM Portal Architecture",
    description: "Integrazione di sistemi di monitoraggio metano con dashboard real-time e gestione allarmi.",
    tags: ["React", "Data Viz", "UI/UX"],
    link: "#"
  },
  {
    id: 2,
    title: "Elite Industrial Interface",
    description: "Design system avanzato per interfacce di controllo industriale ad alta affidabilità.",
    tags: ["Vanilla CSS", "Design System"],
    link: "#"
  }
];

const Projects = () => {
  return (
    <section id="work" className="projects-section">
      <div className="section-header">
        <h2 className="section-title">Progetti Selezionati</h2>
        <div className="section-line"></div>
      </div>
      <div className="projects-grid">
        {projects.map(project => (
          <div key={project.id} className="project-card">
            <div className="project-info">
              <div className="project-tags">
                {project.tags.map(tag => <span key={tag} className="tag">{tag}</span>)}
              </div>
              <h3 className="project-title">{project.title}</h3>
              <p className="project-desc">{project.description}</p>
              <a href={project.link} className="project-link">Scopri di più →</a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
"""
    with open(os.path.join(components_dir, "Projects.jsx"), "w") as f:
        f.write(projects_code)

    # 2. Update App.jsx to include Projects
    app_code = """
import Header from './components/Header';
import Hero from './components/Hero';
import Projects from './components/Projects';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main>
        <Hero />
        <Projects />
      </main>
    </div>
  );
}

export default App;
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    # 3. Add Project Styles to index.css
    project_styles = """
/* Projects Section Styles */
.projects-section {
  padding: 100px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  margin-bottom: 50px;
}

.section-title {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.section-line {
  width: 60px;
  height: 4px;
  background: var(--accent-color);
  border-radius: 2px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
}

.project-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 30px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  backdrop-filter: blur(10px);
}

.project-card:hover {
  transform: translateY(-10px);
  border-color: rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.08);
}

.project-tags {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.tag {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: rgba(255, 255, 255, 0.1);
  padding: 4px 10px;
  border-radius: 12px;
  color: #aaa;
}

.project-title {
  font-size: 1.5rem;
  margin-bottom: 15px;
}

.project-desc {
  color: #888;
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 25px;
}

.project-link {
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: opacity 0.2s;
}

.project-link:hover {
  opacity: 0.8;
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
"""
    with open(os.path.join(src_dir, "index.css"), "a") as f:
        f.write(project_styles)

    print("Projects Section components deployed successfully!")

if __name__ == "__main__":
    deploy()
