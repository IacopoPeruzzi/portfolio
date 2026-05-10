import os

def restore():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")
    
    # 1. Restore Premium index.css
    premium_css = """
:root {
  --bg-color: #0a0a0a;
  --text-color: #f5f5f7;
  --accent-color: #0071e3;
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-border: rgba(255, 255, 255, 0.1);
  font-family: 'Inter', -apple-system, system-ui, sans-serif;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-color);
  color: var(--text-color);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Glass Navigation */
.glass-nav {
  position: fixed;
  top: 0;
  width: 100%;
  height: 70px;
  background: rgba(10, 10, 10, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--glass-border);
  z-index: 1000;
  display: flex;
  justify-content: center;
}

.nav-content {
  width: 90%;
  max-width: 1200px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Sections */
section {
  padding: 100px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-section {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.hero-title {
  font-size: clamp(3rem, 10vw, 5.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  margin: 0;
  background: linear-gradient(180deg, #fff 0%, #888 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.5rem;
  color: #888;
  margin-top: 20px;
  max-width: 700px;
}

/* Timeline / Experience */
.timeline {
  position: relative;
  margin-top: 50px;
}

.timeline-item {
  position: relative;
  padding-left: 40px;
  margin-bottom: 50px;
  border-left: 2px solid var(--glass-border);
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -7px;
  top: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent-color);
  box-shadow: 0 0 10px var(--accent-color);
}

.item-date {
  font-size: 0.9rem;
  color: var(--accent-color);
  font-weight: 600;
  margin-bottom: 5px;
}

.item-title {
  font-size: 1.4rem;
  font-weight: 700;
}

.item-org {
  font-size: 1.1rem;
  color: #888;
  margin-bottom: 15px;
}

/* Contact Banner */
.contact-banner {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 40px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 30px;
  backdrop-filter: blur(10px);
}

.contact-box h4 {
  margin: 0;
  color: #555;
  text-transform: uppercase;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
}

.contact-box p, .contact-box a {
  margin: 5px 0 0;
  font-size: 1.2rem;
  color: #fff;
  text-decoration: none;
}
"""
    with open(os.path.join(src_dir, "index.css"), "w") as f:
        f.write(premium_css)

    # 2. Update Header.jsx
    header_code = """
import React from 'react';

const Header = () => {
  return (
    <nav className="glass-nav">
      <div className="nav-content">
        <div style={{fontWeight: 800, fontSize: '1.2rem'}}>IP.DESIGN</div>
        <div style={{display: 'flex', gap: '30px'}}>
          <a href="#about" style={{color: '#888', textDecoration: 'none'}}>Profilo</a>
          <a href="#experience" style={{color: '#888', textDecoration: 'none'}}>Esperienza</a>
          <a href="#contact" style={{color: '#888', textDecoration: 'none'}}>Contatto</a>
        </div>
      </div>
    </nav>
  );
};

export default Header;
"""
    with open(os.path.join(comp_dir, "Header.jsx"), "w") as f:
        f.write(header_code)

    # 3. Update Hero.jsx
    hero_code = """
import React from 'react';

const Hero = () => {
  return (
    <section className="hero-section">
      <h1 className="hero-title">Iacopo Peruzzi</h1>
      <p className="hero-subtitle">User Experience & Service Design Manager</p>
      <div style={{marginTop: '40px'}}>
        <button style={{padding: '12px 30px', borderRadius: '30px', border: 'none', background: '#fff', fontWeight: 600, cursor: 'pointer'}}>Vedi Progetti</button>
      </div>
    </section>
  );
};

export default Hero;
"""
    with open(os.path.join(comp_dir, "Hero.jsx"), "w") as f:
        f.write(hero_code)

    # 4. Update About.jsx
    about_code = """
import React from 'react';

const About = () => {
  return (
    <section id="about">
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '80px', alignItems: 'center'}}>
        <div>
          <h2 style={{fontSize: '2.5rem', marginBottom: '30px'}}>Visione & Strategia</h2>
          <p style={{fontSize: '1.1rem', color: '#888', lineHeight: '1.7'}}>
            Con oltre otto anni di esperienza nel settore IoT e AI, guido team multidisciplinari per creare soluzioni digitali che fondono intuizione umana e potenza tecnologica. Il mio approccio integra ricerca, strategia e design per risolvere problemi complessi in contesti industriali e aziendali.
          </p>
        </div>
        <div style={{background: 'var(--glass-bg)', padding: '40px', borderRadius: '20px', border: '1px solid var(--glass-border)'}}>
          <h3 style={{marginTop: 0}}>Focus</h3>
          <ul style={{listStyle: 'none', padding: 0, color: '#888'}}>
            <li style={{marginBottom: '10px'}}>→ Industrial AI & IoT</li>
            <li style={{marginBottom: '10px'}}>→ Embedded User Interfaces</li>
            <li style={{marginBottom: '10px'}}>→ Service Design Strategy</li>
            <li style={{marginBottom: '10px'}}>→ Multidisciplinary Team Lead</li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default About;
"""
    with open(os.path.join(comp_dir, "About.jsx"), "w") as f:
        f.write(about_code)

    # 5. Update Experience.jsx
    exp_code = """
import React from 'react';

const Experience = () => {
  const experiences = [
    {
      date: "2024 - Present",
      title: "UX & Service Design Manager",
      org: "SECO SpA",
      desc: "Guida di team strategici su soluzioni IoT e AI ad alto impatto."
    },
    {
      date: "2022 - 2024",
      title: "Team Leader",
      org: "SECO SpA",
      desc: "Coordinamento di esperienze digitali per il settore industriale."
    },
    {
      date: "2021 - 2022",
      title: "Senior UX Designer",
      org: "SECO Mind srl",
      desc: "Sviluppo di architetture software-defined e interfacce complesse."
    }
  ];

  return (
    <section id="experience">
      <h2 style={{fontSize: '2.5rem', marginBottom: '50px'}}>Esperienza Professionale</h2>
      <div className="timeline">
        {experiences.map((exp, i) => (
          <div key={i} className="timeline-item">
            <div className="item-date">{exp.date}</div>
            <div className="item-title">{exp.title}</div>
            <div className="item-org">{exp.org}</div>
            <p style={{color: '#888'}}>{exp.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Experience;
"""
    with open(os.path.join(comp_dir, "Experience.jsx"), "w") as f:
        f.write(exp_code)

    # 6. Update Contact.jsx
    contact_code = """
import React from 'react';

const Contact = () => {
  return (
    <section id="contact">
      <div className="contact-banner">
        <div className="contact-box">
          <h4>Email</h4>
          <a href="mailto:iacopo.peruzzi90@gmail.com">iacopo.peruzzi90@gmail.com</a>
        </div>
        <div className="contact-box">
          <h4>LinkedIn</h4>
          <a href="https://www.linkedin.com/in/iacopoperuzzi/" target="_blank">in/iacopoperuzzi</a>
        </div>
        <div className="contact-box">
          <h4>Location</h4>
          <p>Milano / Siena, Italia</p>
        </div>
      </div>
    </section>
  );
};

export default Contact;
"""
    with open(os.path.join(comp_dir, "Contact.jsx"), "w") as f:
        f.write(contact_code)

    # 7. Update App.jsx
    app_code = """
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Experience from './components/Experience';
import Contact from './components/Contact';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main>
        <Hero />
        <About />
        <Experience />
        <Contact />
      </main>
      <footer style={{textAlign: 'center', padding: '60px 20px', color: '#444', fontSize: '0.9rem', borderTop: '1px solid var(--glass-border)'}}>
        IP.DESIGN © {new Date().getFullYear()} — Made with Passion.
      </footer>
    </div>
  );
}

export default App;
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    print("Premium UI restored and CV content integrated successfully!")

if __name__ == "__main__":
    restore()
