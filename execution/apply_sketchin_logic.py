import os

def update():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")

    # 1. Update StrategicInitiatives.jsx
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { Link } from 'react-router-dom';

const initiatives = [
  { id: "clea-ecosystem", title: "Clea Ecosystem", desc: "Experience foundation for connected ecosystems.", tags: ["Platform", "Strategy"] },
  { id: "clea-ai-studio", title: "Clea AI Studio", desc: "Visual AI workflow editor for model creation.", tags: ["AI", "Visual Tools"] },
  { id: "app-hub", title: "SECO Application Hub", desc: "Developer hub for AI application deployment.", tags: ["Edge AI", "Marketplace"] },
  { id: "oobe", title: "Out-of-the-box Experience", desc: "Reducing friction from first setup to activation.", tags: ["Onboarding", "CX"] },
  { id: "dev-center", title: "SECO Developer Center", desc: "Self-service technical documentation platform.", tags: ["DevEx", "Docs"] }
];

const StrategicInitiatives = () => (
  <section className="section" id="initiatives" style={{overflow: 'hidden'}}>
    <div className="container">
      <span className="section-label reveal">Strategic Initiatives</span>
      <h2 className="dynamic-title reveal">Orchestrating internal platforms.</h2>
      <div className="grid-2" style={{marginTop: '100px'}}>
        {initiatives.map(item => (
          <Link key={item.id} to={} className="card reveal" style={{display: 'block', textDecoration: 'none', color: 'inherit'}}>
            <h3 style={{fontSize: '2rem'}}>{item.title}</h3>
            <p style={{fontSize: '1.1rem'}}>{item.desc}</p>
            <div className="tag-list">
              {item.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
          </Link>
        ))}
      </div>
    </div>
  </section>
);

export default StrategicInitiatives;
''')

    # 2. Update ClientProjects.jsx
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { Link } from 'react-router-dom';

const projects = [
  { id: "daikin", client: "Daikin", title: "Professional HVAC Workflows" },
  { id: "quanta", client: "Quanta Systems", title: "Medical Innovation" },
  { id: "snam", client: "SNAM", title: "Methane Detection" },
  { id: "fastweb", client: "Fastweb", title: "Telecom Monitoring" },
  { id: "riello", client: "Riello UPS", title: "App Migration" },
  { id: "rhea", client: "Rhea Vendors", title: "Smart Vending" },
  { id: "pizzarotti", client: "Pizzarotti", title: "Construction IoT" },
  { id: "ciam", client: "CIAM", title: "Refrigeration Setup" },
  { id: "zoppas", client: "Zoppas", title: "Service Innovation" }
];

const ClientProjects = () => (
  <section className="section" id="projects">
    <div className="container">
      <span className="section-label reveal">Client Projects</span>
      <h2 className="dynamic-title reveal">Industry-defining solutions.</h2>
      <div className="grid-3" style={{marginTop: '100px'}}>
        {projects.map(p => (
          <Link key={p.id} to={} className="card reveal" style={{padding: '40px', display: 'block', textDecoration: 'none', color: 'inherit'}}>
            <span style={{fontSize: '0.7rem', color: 'var(--accent-color)', textTransform: 'uppercase', letterSpacing: '0.2em'}}>{p.client}</span>
            <h3 style={{fontSize: '1.4rem', marginTop: '10px'}}>{p.title}</h3>
          </Link>
        ))}
      </div>
    </div>
  </section>
);

export default ClientProjects;
''')

    # 3. Update App.jsx
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';
import useReveal from './hooks/useReveal';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import ClientProjects from './components/ClientProjects';
import Process from './components/Process';
import Contact from './components/Contact';
import CaseStudy from './components/CaseStudy';

const Home = () => {
  useReveal();
  return (
    <>
      <Hero />
      <About />
      <Expertise />
      <StrategicInitiatives />
      <ClientProjects />
      <Process />
      <Contact />
    </>
  );
};

function App() {
  return (
    <Router>
      <ScrollToTop />
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
''')

    print("Sketchin-style dynamic layout and animations applied successfully!")

if __name__ == "__main__":
    update()
