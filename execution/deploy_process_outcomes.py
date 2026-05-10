import os

def deploy():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")

    # 1. PROCESS COMPONENT
    process_code = """
import React from 'react';

const steps = [
  { title: "Discovery & Strategy", desc: "Aligning business goals with technical constraints and user needs through strategic research." },
  { title: "Design & Architecture", desc: "Defining complex information architectures and scalable user flows for connected ecosystems." },
  { title: "Leadership & Governance", desc: "Guiding multidisciplinary teams and maintaining consistency through robust design systems." },
  { title: "Delivery & Handoff", desc: "Ensuring high-quality implementation through structured handoff and technical alignment." }
];

const Process = () => (
  <section className="section" id="process">
    <div className="container">
      <span className="section-label">Process</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>A strategic approach to complexity.</h2>
      <div className="grid-2" style={{gap: '40px'}}>
        {steps.map((step, i) => (
          <div key={i} style={{padding: '40px', border: '1px solid var(--border-color)'}}>
            <span style={{fontSize: '0.8rem', color: 'var(--text-secondary)'}}>0{i+1}</span>
            <h3 style={{fontSize: '1.5rem', margin: '20px 0'}}>{step.title}</h3>
            <p style={{color: 'var(--text-secondary)', lineHeight: '1.6'}}>{step.desc}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Process;
"""
    with open(os.path.join(comp_dir, "Process.jsx"), "w") as f:
        f.write(process_code)

    # 2. OUTCOMES COMPONENT
    outcomes_code = """
import React from 'react';

const outcomes = [
  { label: "15+ Projects", desc: "Unified across a single design language and ecosystem." },
  { label: "40% Faster", desc: "Onboarding and configuration time reduced for enterprise clients." },
  { label: "DesignOps", desc: "Scaling quality across distributed products and engineering teams." },
  { label: "B2B Value", desc: "Directly supporting new AI-driven subscription and service models." }
];

const Outcomes = () => (
  <section className="section" id="outcomes" style={{background: 'var(--surface-color)'}}>
    <div className="container">
      <span className="section-label">Selected Outcomes</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Impact at scale.</h2>
      <div className="grid-4" style={{display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '30px'}}>
        {outcomes.map((item, i) => (
          <div key={i}>
            <h3 style={{fontSize: '2.5rem', marginBottom: '10px'}}>{item.label}</h3>
            <p style={{color: 'var(--text-secondary)', fontSize: '0.9rem'}}>{item.desc}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Outcomes;
"""
    with open(os.path.join(comp_dir, "Outcomes.jsx"), "w") as f:
        f.write(outcomes_code)

    # 3. UPDATE APP.JSX
    app_code = """
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import DesignGovernance from './components/DesignGovernance';
import ClientProjects from './components/ClientProjects';
import Process from './components/Process';
import Outcomes from './components/Outcomes';
import Contact from './components/Contact';
import CaseStudy from './components/CaseStudy';

const Home = () => (
  <>
    <Hero />
    <About />
    <Expertise />
    <StrategicInitiatives />
    <DesignGovernance />
    <ClientProjects />
    <Process />
    <Outcomes />
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
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    # Update index.css for grid-4
    with open(os.path.join(src_dir, "index.css"), "a") as f:
        f.write("\\n@media (max-width: 1024px) { .grid-4 { grid-template-columns: 1fr 1fr !important; } }\\n@media (max-width: 600px) { .grid-4 { grid-template-columns: 1fr !important; } }\\n")

    print("Process and Outcomes sections deployed successfully!")

if __name__ == "__main__":
    deploy()
