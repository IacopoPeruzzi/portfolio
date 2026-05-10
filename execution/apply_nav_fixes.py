import os

def update():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")

    # 1. Update Expertise.jsx (Remove Arrows)
    with open(os.path.join(comp_dir, "Expertise.jsx"), "w") as f:
        f.write('''
import React from 'react';

const expertise = [
  { area: "UX Strategy", details: "Product Vision, Experience Logic, Design Roadmap" },
  { area: "Service Design", details: "Ecosystems, User Journeys, Service Logic" },
  { area: "Interaction Design", details: "Complex Flows, Industrial HMI, B2B Platforms" },
  { area: "Design Leadership", details: "Team Coordination, Design Governance, DesignOps" }
];

const Expertise = () => (
  <section className="section" id="expertise">
    <div className="container">
      <span className="section-label">Expertise</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Bridging strategy and delivery.</h2>
      <div className="expertise-list">
        {expertise.map((item, i) => (
          <div key={i} className="expertise-item">
            <h3>{item.area}</h3>
            <span>{item.details}</span>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Expertise;
''')

    # 2. Update StrategicInitiatives.jsx (Full clickable cards)
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { Link } from 'react-router-dom';

const initiatives = [
  { id: "clea-ecosystem", title: "Clea Ecosystem", desc: "Designing the experience foundation for SECO’s connected product ecosystem.", tags: ["Ecosystem Design", "Platform Strategy"] },
  { id: "clea-ai-studio", title: "Clea AI Studio", desc: "Visual AI workflow editor for model creation, configuration and deployment.", tags: ["AI Tools", "Visual Programming"] },
  { id: "app-hub", title: "SECO Application Hub", desc: "Developer-oriented hub for discovery and deployment of AI applications.", tags: ["Marketplace", "Edge AI"] },
  { id: "oobe", title: "Out-of-the-box Experience", desc: "Reducing friction from first setup to product activation across touchpoints.", tags: ["Onboarding", "CX"] },
  { id: "dev-center", title: "SECO Developer Center", desc: "Structuring a self-service experience for technical documentation.", tags: ["Developer Experience", "Documentation"] }
];

const StrategicInitiatives = () => (
  <section className="section" id="initiatives">
    <div className="container">
      <span className="section-label">Strategic Product Initiatives</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Orchestrating internal platforms.</h2>
      <div className="grid-2">
        {initiatives.map(item => (
          <Link key={item.id} to={} className="card" style={{display: 'block', textDecoration: 'none', color: 'inherit'}}>
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
            <div className="tag-list">
              {item.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
            <span style={{marginTop: '20px', display: 'block', color: 'var(--accent-color)', fontWeight: 600, fontSize: '0.8rem'}}>Read Case Study →</span>
          </Link>
        ))}
      </div>
    </div>
  </section>
);

export default StrategicInitiatives;
''')

    # 3. Update ClientProjects.jsx (Full clickable cards)
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { Link } from 'react-router-dom';

const projects = [
  { id: "daikin", client: "Daikin Applied Europe", title: "Professional HVAC Workflows" },
  { id: "quanta", client: "Quanta Systems", title: "Medical & Aesthetic Innovation" },
  { id: "snam", client: "SNAM", title: "Methane Detection Systems" },
  { id: "fastweb", client: "Fastweb", title: "Telecom Monitoring Tools" },
  { id: "riello", client: "Riello UPS", title: "Application Migration" },
  { id: "rhea", client: "Rhea Vendors", title: "Smart Vending Monitoring" },
  { id: "pizzarotti", client: "Pizzarotti", title: "Construction IoT Data" },
  { id: "ciam", client: "CIAM", title: "Refrigeration Remote Setup" },
  { id: "zoppas", client: "Zoppas Industries", title: "Strategic Service Innovation" }
];

const ClientProjects = () => (
  <section className="section" id="projects">
    <div className="container">
      <span className="section-label">Client Projects</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Industry-defining solutions.</h2>
      <div className="grid-3">
        {projects.map(p => (
          <Link key={p.id} to={} className="card" style={{padding: '30px', display: 'block', textDecoration: 'none', color: 'inherit'}}>
            <span style={{fontSize: '0.7rem', color: 'var(--accent-color)', textTransform: 'uppercase', letterSpacing: '0.1em'}}>{p.client}</span>
            <h3 style={{fontSize: '1.2rem', marginTop: '10px'}}>{p.title}</h3>
            <span style={{marginTop: '15px', display: 'block', color: 'var(--accent-color)', fontSize: '0.75rem', fontWeight: 600}}>Case Study →</span>
          </Link>
        ))}
      </div>
    </div>
  </section>
);

export default ClientProjects;
''')

    # 4. Update App.jsx (Integrate ScrollToTop)
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write('''
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import ClientProjects from './components/ClientProjects';
import Process from './components/Process';
import Contact from './components/Contact';
import CaseStudy from './components/CaseStudy';

const Home = () => (
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

    print("Navigation fixes and UI clean-up applied successfully!")

if __name__ == "__main__":
    update()
