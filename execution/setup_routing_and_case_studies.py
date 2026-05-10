import os
import subprocess

def setup_case_studies():
    project_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app"
    src_dir = os.path.join(project_dir, "src")
    comp_dir = os.path.join(src_dir, "components")
    data_dir = os.path.join(src_dir, "data")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # 1. Install react-router-dom
    print("Installing react-router-dom...")
    subprocess.run("npm install react-router-dom", shell=True, cwd=project_dir)

    # 2. Create Projects Data (src/data/projects.js)
    projects_data = """
export const projects = [
  {
    id: "clea-ecosystem",
    title: "Clea Ecosystem",
    subtitle: "Orchestrating the foundation for industrial connectivity.",
    type: "strategic",
    metadata: { client: "SECO SpA", year: "2021-Present", role: "Design Lead" },
    challenge: "Industrial ecosystems are often fragmented and difficult to scale. The goal was to unify hardware and software touchpoints into a single, cohesive experience.",
    context: "SECO needed a scalable platform to manage millions of connected edge devices.",
    role: "Leading a team of UX/UI designers to define the design system and service strategy.",
    process: "Strategic mapping, stakeholder interviews, and iterative prototyping of core platform services.",
    decisions: "Adopting a software-defined architecture to allow flexible UI updates across various hardware types.",
    outcome: "A unified portal that reduced onboarding time by 40% for new enterprise clients.",
    learnings: "Design governance is as critical as the design itself in large-scale ecosystems.",
    tags: ["Ecosystem Design", "Platform Strategy"]
  },
  {
    id: "clea-ai-studio",
    title: "Clea AI Studio",
    subtitle: "Democratizing AI deployment on the edge.",
    type: "strategic",
    metadata: { client: "SECO SpA", year: "2023", role: "UX Manager" },
    challenge: "AI model configuration is typically restricted to data scientists. We aimed to make it accessible to industrial engineers.",
    context: "The need for 'No-Code' or 'Low-Code' solutions in the industrial AI market.",
    role: "Overseeing the visual editor design and deployment workflow optimization.",
    process: "User research with industrial engineers, testing visual programming paradigms.",
    decisions: "Using a node-based visual editor to simplify complex neural network configurations.",
    outcome: "Reduced time-to-deployment for AI models from weeks to days.",
    learnings: "Simplicity in AI tools requires a deep understanding of underlying technical constraints.",
    tags: ["AI Tools", "Visual Programming"]
  },
  {
    id: "daikin",
    title: "Daikin Applied Europe",
    subtitle: "Advanced HMI for mission-critical HVAC systems.",
    type: "client",
    metadata: { client: "Daikin", year: "2022", role: "Service Designer" },
    challenge: "Professional HVAC management requires high precision and immediate error detection.",
    context: "Large-scale chillers and air handling units in commercial buildings.",
    role: "Designing the HMI for embedded touchscreens and the companion mobile app.",
    process: "On-site ethnography at industrial plants, task analysis of maintenance workflows.",
    decisions: "Implementing a high-contrast dark interface to ensure readability in mechanical rooms.",
    outcome: "Significant reduction in maintenance errors and faster reaction times to system alerts.",
    learnings: "Industrial environments dictate UI constraints that differ drastically from consumer apps.",
    tags: ["Industrial HMI", "Service Design"]
  },
  {
    id: "quanta-systems",
    title: "Quanta Systems",
    subtitle: "Service design for medical and aesthetic innovation.",
    type: "client",
    metadata: { client: "Quanta Systems", year: "2023", role: "Strategic Designer" },
    challenge: "Transitioning from a product-selling model to an AI-driven service-subscription model.",
    context: "High-end laser systems for medical and aesthetic treatments.",
    role: "Defining the service blueprint for the new connected service offering.",
    process: "Business modeling, service blueprinting, and UX strategy for the professional portal.",
    decisions: "Focusing on remote diagnostics as the primary value driver for the subscription model.",
    outcome: "Approved roadmap for a new recurring revenue stream based on IoT data.",
    learnings: "Strategic design is about aligning user needs with business model transformations.",
    tags: ["Medical IoT", "Business Strategy"]
  }
];
"""
    with open(os.path.join(data_dir, "projects.js"), "w") as f:
        f.write(projects_data)

    # 3. Create CaseStudy Template (src/components/CaseStudy.jsx)
    case_study_code = """
import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { projects } from '../data/projects';

const CaseStudy = () => {
  const { id } = useParams();
  const project = projects.find(p => p.id === id);

  if (!project) return <div>Project not found.</div>;

  return (
    <div className="case-study-page">
      <header className="cs-hero section">
        <div className="container">
          <Link to="/" className="back-link">← Back to Overview</Link>
          <span className="section-label" style={{marginTop: '40px'}}>{project.metadata.client}</span>
          <h1 className="hero-title">{project.title}</h1>
          <p className="hero-subtitle">{project.subtitle}</p>
        </div>
      </header>

      <section className="section cs-snapshot">
        <div className="container grid-3">
          <div><label className="section-label">Year</label><p>{project.metadata.year}</p></div>
          <div><label className="section-label">My Role</label><p>{project.metadata.role}</p></div>
          <div><label className="section-label">Expertise</label><p>{project.tags.join(', ')}</p></div>
        </div>
      </section>

      <section className="section">
        <div className="container grid-2">
          <div>
            <h2 className="cs-heading">The Challenge</h2>
            <p className="cs-body">{project.challenge}</p>
          </div>
          <div>
            <h2 className="cs-heading">Context</h2>
            <p className="cs-body">{project.context}</p>
          </div>
        </div>
      </section>

      <section className="section" style={{background: 'var(--surface-color)'}}>
        <div className="container">
          <h2 className="cs-heading">My Strategic Role</h2>
          <p className="cs-body" style={{maxWidth: '800px'}}>{project.role}</p>
        </div>
      </section>

      <section className="section">
        <div className="container grid-2">
          <div>
            <h2 className="cs-heading">Process & Decisions</h2>
            <p className="cs-body">{project.process}</p>
            <p className="cs-body" style={{marginTop: '20px'}}><strong>Key Decision:</strong> {project.decisions}</p>
          </div>
          <div>
            <h2 className="cs-heading">Outcome</h2>
            <p className="cs-body">{project.outcome}</p>
          </div>
        </div>
      </section>

      <section className="section" style={{borderBottom: 'none'}}>
        <div className="container">
          <h2 className="cs-heading">Learnings</h2>
          <p className="cs-body" style={{maxWidth: '800px'}}>{project.learnings}</p>
          <div style={{marginTop: '100px', textAlign: 'center'}}>
            <Link to="/" className="back-link" style={{fontSize: '1.5rem'}}>Next Project →</Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default CaseStudy;
"""
    with open(os.path.join(comp_dir, "CaseStudy.jsx"), "w") as f:
        f.write(case_study_code)

    # 4. Update index.css with Case Study specific styles
    cs_styles = """
/* Case Study Specific Styles */
.case-study-page {
  padding-top: 80px;
}

.back-link {
  font-size: 0.85rem;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.cs-heading {
  font-size: 2rem;
  margin-bottom: 25px;
}

.cs-body {
  font-size: 1.1rem;
  color: var(--text-secondary);
  line-height: 1.7;
}

.cs-hero {
  border-bottom: 1px solid var(--border-color);
}
"""
    with open(os.path.join(src_dir, "index.css"), "a") as f:
        f.write(cs_styles)

    # 5. Update Home components to use Links
    # Update StrategicInitiatives.jsx
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write("""
import React from 'react';
import { Link } from 'react-router-dom';

const initiatives = [
  {
    id: "clea-ecosystem",
    title: "Clea Ecosystem",
    desc: "Designing the experience foundation for SECO’s connected product ecosystem.",
    tags: ["Ecosystem Design", "Platform Strategy"],
    hasCaseStudy: true
  },
  {
    id: "clea-ai-studio",
    title: "Clea AI Studio",
    desc: "Making AI workflows accessible through a visual editor for model creation and deployment.",
    tags: ["AI Tools", "Visual Programming"],
    hasCaseStudy: true
  },
  {
    id: "app-hub",
    title: "SECO Application Hub",
    desc: "Simplifying discovery and deployment of AI applications on edge devices.",
    tags: ["Marketplace", "Edge Computing"],
    hasCaseStudy: false
  },
  {
    id: "oobe",
    title: "Out-of-the-box Experience",
    desc: "Reducing friction from first setup to product activation across touchpoints.",
    tags: ["Onboarding", "CX"],
    hasCaseStudy: false
  }
];

const StrategicInitiatives = () => (
  <section className="section" id="initiatives">
    <div className="container">
      <span className="section-label">Strategic Product Initiatives</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Orchestrating internal platforms.</h2>
      <div className="grid-2">
        {initiatives.map(item => (
          <div key={item.id} className="card">
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
            <div className="tag-list">
              {item.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
            {item.hasCaseStudy && <Link to={`/case-study/${item.id}`} style={{marginTop: '20px', display: 'block', color: 'var(--accent-color)', fontWeight: 600}}>Read Case Study →</Link>}
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default StrategicInitiatives;
""")

    # Update ClientProjects.jsx
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write("""
import React from 'react';
import { Link } from 'react-router-dom';

const projects = [
  {
    id: "daikin",
    client: "Daikin Applied Europe",
    title: "Professional HVAC Workflows",
    desc: "Embedded HMI and companion app for mission-critical environmental control.",
    hasCaseStudy: true
  },
  {
    id: "quanta",
    client: "Quanta Systems",
    title: "Strategic Service Design",
    desc: "Transitioning to AI-driven services in medical and aesthetic applications.",
    hasCaseStudy: true
  },
  {
    id: "snam",
    client: "SNAM",
    title: "Methane Detection Systems",
    desc: "Operational applications for industrial leak prevention.",
    hasCaseStudy: false
  }
];

const ClientProjects = () => (
  <section className="section" id="projects">
    <div className="container">
      <span className="section-label">Client Projects</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Industry-defining solutions.</h2>
      <div className="grid-3">
        {projects.map(p => (
          <div key={p.id} className="card" style={{padding: '30px'}}>
            <span style={{fontSize: '0.7rem', color: 'var(--accent-color)'}}>{p.client}</span>
            <h3 style={{fontSize: '1.2rem', marginTop: '10px'}}>{p.title}</h3>
            <p style={{fontSize: '0.85rem'}}>{p.desc}</p>
            {p.hasCaseStudy && <Link to={`/case-study/${p.id}`} style={{marginTop: '15px', display: 'block', color: 'var(--accent-color)', fontSize: '0.8rem', fontWeight: 600}}>Case Study →</Link>}
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default ClientProjects;
""")

    # 6. Update App.jsx with Router
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write("""
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import ClientProjects from './components/ClientProjects';
import Contact from './components/Contact';
import CaseStudy from './components/CaseStudy';

const Home = () => (
  <>
    <Hero />
    <About />
    <Expertise />
    <StrategicInitiatives />
    <ClientProjects />
    <Contact />
  </>
);

function App() {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/case-study/:id" element={<CaseStudy />} />
          </Routes>
        </main>
        <footer className="footer">
          IACOPO PERUZZI — UX & SERVICE DESIGN MANAGER — {new Date().getFullYear()}
        </footer>
      </div>
    </Router>
  );
}

export default App;
""")

    print("Routing and Case Study system deployed successfully!")

if __name__ == "__main__":
    setup_case_studies()
