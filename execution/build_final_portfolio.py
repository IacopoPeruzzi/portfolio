import os

def build_final():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")
    
    if not os.path.exists(comp_dir):
        os.makedirs(comp_dir)

    # --- 1. CSS SYSTEM (Editorial & Minimal) ---
    css_content = """
:root {
  --bg-color: #050505;
  --surface-color: #0f0f0f;
  --text-primary: #f5f5f7;
  --text-secondary: #a1a1a6;
  --accent-color: #ffffff;
  --border-color: rgba(255, 255, 255, 0.1);
  --section-padding: 120px 20px;
  font-family: 'Inter', -apple-system, system-ui, sans-serif;
}

body {
  margin: 0;
  background-color: var(--bg-color);
  color: var(--text-primary);
  -webkit-font-smoothing: antialiased;
  line-height: 1.5;
}

h1, h2, h3, h4 {
  font-weight: 700;
  letter-spacing: -0.03em;
  margin: 0;
}

a {
  color: inherit;
  text-decoration: none;
  transition: opacity 0.3s;
}

a:hover {
  opacity: 0.7;
}

/* Layout Utilities */
.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--text-secondary);
  margin-bottom: 20px;
  display: block;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

/* Navigation */
.nav {
  position: fixed;
  top: 0;
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: center;
  z-index: 1000;
  background: rgba(5, 5, 5, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-color);
}

.nav-content {
  width: 90%;
  max-width: 1100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 40px;
  font-size: 0.85rem;
  font-weight: 500;
}

/* Hero */
.hero {
  height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-bottom: 1px solid var(--border-color);
}

.hero h1 {
  font-size: clamp(3rem, 8vw, 6rem);
  line-height: 1;
  margin-bottom: 40px;
}

.hero p {
  font-size: 1.5rem;
  color: var(--text-secondary);
  max-width: 800px;
}

/* Section Common */
.section {
  padding: var(--section-padding);
  border-bottom: 1px solid var(--border-color);
}

/* Cards */
.card {
  background: var(--surface-color);
  border: 1px solid var(--border-color);
  padding: 40px;
  border-radius: 1px;
  transition: border-color 0.4s;
}

.card:hover {
  border-color: rgba(255, 255, 255, 0.4);
}

.card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
}

.card p {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.tag-list {
  display: flex;
  gap: 10px;
  margin-top: 20px;
  flex-wrap: wrap;
}

.tag {
  font-size: 0.7rem;
  background: rgba(255, 255, 255, 0.05);
  padding: 4px 10px;
  color: var(--text-secondary);
}

/* Expertise List */
.expertise-item {
  padding: 30px 0;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.expertise-item:last-child {
  border-bottom: 1px solid var(--border-color);
}

/* Footer */
.footer {
  padding: 80px 20px;
  text-align: center;
  color: var(--text-secondary);
  font-size: 0.8rem;
}

@media (max-width: 768px) {
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .nav-links { display: none; }
}
"""
    with open(os.path.join(src_dir, "index.css"), "w") as f:
        f.write(css_content)

    # --- 2. COMPONENTS ---

    # Header
    with open(os.path.join(comp_dir, "Header.jsx"), "w") as f:
        f.write("""
import React from 'react';

const Header = () => (
  <nav className="nav">
    <div className="nav-content">
      <div style={{fontWeight: 800, letterSpacing: '-0.02em'}}>IACOPO PERUZZI</div>
      <div className="nav-links">
        <a href="#initiatives">Initiatives</a>
        <a href="#projects">Projects</a>
        <a href="#expertise">Expertise</a>
        <a href="#contact">Contact</a>
      </div>
    </div>
  </nav>
);

export default Header;
""")

    # Hero
    with open(os.path.join(comp_dir, "Hero.jsx"), "w") as f:
        f.write("""
import React from 'react';

const Hero = () => (
  <section className="section hero">
    <div className="container">
      <span className="section-label">UX & Service Design Manager</span>
      <h1>Designing complex industrial ecosystems.</h1>
      <p>I lead multidisciplinary teams in creating digital products, connected services, and embedded interfaces across IoT and AI contexts.</p>
    </div>
  </section>
);

export default Hero;
""")

    # About
    with open(os.path.join(comp_dir, "About.jsx"), "w") as f:
        f.write("""
import React from 'react';

const About = () => (
  <section className="section" id="about">
    <div className="container grid-2">
      <div>
        <h2 style={{fontSize: '2.5rem'}}>Leading design at the edge of hardware and software.</h2>
      </div>
      <div>
        <p style={{fontSize: '1.2rem', color: 'var(--text-secondary)'}}>
          With 8+ years of experience, I grew professionally within SECO SpA, where I now lead a team designing the future of industrial connectivity. My work focuses on making complex technologies—like AI and IoT—accessible, intuitive, and strategically aligned with business goals.
        </p>
      </div>
    </div>
  </section>
);

export default About;
""")

    # Expertise
    with open(os.path.join(comp_dir, "Expertise.jsx"), "w") as f:
        f.write("""
import React from 'react';

const expertise = [
  "UX & UI for Industrial Products",
  "Service Design for Connected Ecosystems",
  "AI & IoT Experience Design",
  "Product & Business Strategy",
  "Design Leadership"
];

const Expertise = () => (
  <section className="section" id="expertise">
    <div className="container">
      <span className="section-label">Expertise</span>
      <div style={{marginTop: '40px'}}>
        {expertise.map(item => (
          <div key={item} className="expertise-item">
            <h3 style={{fontSize: '1.8rem'}}>{item}</h3>
            <span style={{color: 'var(--text-secondary)'}}>→</span>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Expertise;
""")

    # Strategic Initiatives
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write("""
import React from 'react';

const initiatives = [
  {
    title: "Clea Ecosystem",
    desc: "Designing the experience foundation for SECO’s connected product ecosystem.",
    tags: ["Ecosystem Design", "Platform Strategy"]
  },
  {
    title: "Clea AI Studio",
    desc: "Making AI workflows accessible through a visual editor for model creation and deployment.",
    tags: ["AI Tools", "Visual Programming"]
  },
  {
    title: "SECO Application Hub",
    desc: "Simplifying discovery and deployment of AI applications on edge devices.",
    tags: ["Marketplace", "Edge Computing"]
  },
  {
    title: "Developer Center",
    desc: "Structuring a self-service experience for technical documentation and software enablement.",
    tags: ["Developer Experience", "Documentation"]
  }
];

const StrategicInitiatives = () => (
  <section className="section" id="initiatives">
    <div className="container">
      <span className="section-label">Strategic Product Initiatives</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Orchestrating internal platforms.</h2>
      <div className="grid-2">
        {initiatives.map(item => (
          <div key={item.title} className="card">
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
            <div className="tag-list">
              {item.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default StrategicInitiatives;
""")

    # Client Projects
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write("""
import React from 'react';

const projects = [
  {
    client: "Daikin Applied Europe",
    title: "Professional HVAC Workflows",
    desc: "Embedded HMI and companion app for mission-critical environmental control."
  },
  {
    client: "SNAM",
    title: "Methane Detection Systems",
    desc: "Operational applications for industrial leak prevention and safety monitoring."
  },
  {
    client: "Fastweb",
    title: "Infrastructure Monitoring",
    desc: "Alerting and visualization tools for distributed telecom networks."
  }
];

const ClientProjects = () => (
  <section className="section" id="projects">
    <div className="container">
      <span className="section-label">Client Projects</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Industry-defining solutions.</h2>
      <div className="grid-3">
        {projects.map(p => (
          <div key={p.client} className="card" style={{padding: '30px'}}>
            <span style={{fontSize: '0.7rem', color: 'var(--accent-color)'}}>{p.client}</span>
            <h3 style={{fontSize: '1.2rem', marginTop: '10px'}}>{p.title}</h3>
            <p style={{fontSize: '0.85rem'}}>{p.desc}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default ClientProjects;
""")

    # Contact
    with open(os.path.join(comp_dir, "Contact.jsx"), "w") as f:
        f.write("""
import React from 'react';

const Contact = () => (
  <section className="section" id="contact" style={{textAlign: 'center', background: 'var(--surface-color)'}}>
    <div className="container">
      <span className="section-label">Get in Touch</span>
      <h2 style={{fontSize: '4rem', margin: '40px 0'}}>Let's design the next ecosystem.</h2>
      <div style={{display: 'flex', justifyContent: 'center', gap: '30px', fontSize: '1.2rem'}}>
        <a href="mailto:iacopo.peruzzi90@gmail.com">Email</a>
        <a href="https://linkedin.com/in/iacopoperuzzi" target="_blank">LinkedIn</a>
      </div>
    </div>
  </section>
);

export default Contact;
""")

    # Main App.jsx
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write("""
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import ClientProjects from './components/ClientProjects';
import Contact from './components/Contact';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main>
        <Hero />
        <About />
        <Expertise />
        <StrategicInitiatives />
        <ClientProjects />
        <Contact />
      </main>
      <footer className="footer">
        IACOPO PERUZZI — UX & SERVICE DESIGN MANAGER — {new Date().getFullYear()}
      </footer>
    </div>
  );
}

export default App;
""")

    print("Final Senior Portfolio build completed successfully!")

if __name__ == "__main__":
    build_final()
