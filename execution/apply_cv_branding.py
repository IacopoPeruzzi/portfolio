import os

def apply_branding():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")
    
    # 1. Update index.css with CV Design System
    cv_css = """
:root {
  --cv-yellow: #f2c94c;
  --cv-dark: #2d2d2d;
  --cv-light-bg: #ffffff;
  --cv-text-dark: #1a1a1a;
  --cv-text-light: #ffffff;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

body {
  margin: 0;
  background-color: var(--cv-light-bg);
  color: var(--cv-text-dark);
}

.dark-section {
  background-color: var(--cv-dark);
  color: var(--cv-text-light);
  padding: 80px 20px;
}

.light-section {
  background-color: var(--cv-light-bg);
  color: var(--cv-text-dark);
  padding: 80px 20px;
}

.yellow-accent {
  position: relative;
  display: inline-block;
}

.yellow-accent::after {
  content: '';
  position: absolute;
  bottom: 8px;
  left: 0;
  width: 100%;
  height: 8px;
  background: var(--cv-yellow);
  z-index: -1;
}

.section-title-cv {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 40px;
  border-bottom: 2px solid var(--cv-text-dark);
  padding-bottom: 10px;
  display: inline-block;
}

.dark-section .section-title-cv {
  border-bottom-color: var(--cv-text-light);
}

/* Updated Components Styles */
.hero-cv {
  padding: 100px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-cv h1 {
  font-size: 3.5rem;
  margin: 0;
}

.hero-cv h2 {
  font-size: 2.2rem;
  color: #666;
  font-weight: 300;
  margin-top: 10px;
}

.contact-banner-cv {
  background-color: var(--cv-yellow);
  padding: 40px 20px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 20px;
}

.contact-item-cv {
  display: flex;
  flex-direction: column;
}

.contact-item-cv label {
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
}

.contact-item-cv span, .contact-item-cv a {
  font-size: 1rem;
  color: inherit;
  text-decoration: none;
}

/* Experience & Education Grid */
.cv-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.cv-item {
  margin-bottom: 30px;
}

.cv-date {
  font-weight: 700;
  color: var(--cv-yellow);
  margin-bottom: 5px;
}

.cv-org {
  font-weight: 700;
  margin-bottom: 5px;
}

.cv-role {
  font-style: italic;
  margin-bottom: 10px;
  color: #888;
}

.cv-desc {
  font-size: 0.9rem;
  line-height: 1.5;
}
"""
    with open(os.path.join(src_dir, "index.css"), "w") as f:
        f.write(cv_css)

    # 2. Update Hero.jsx
    hero_code = """
import React from 'react';

const Hero = () => {
  return (
    <section className="hero-cv">
      <h1>Ciao! Sono <span className="yellow-accent">Iacopo Peruzzi,</span></h1>
      <h2>User Experience e<br/>Service Design Manager</h2>
    </section>
  );
};

export default Hero;
"""
    with open(os.path.join(comp_dir, "Hero.jsx"), "w") as f:
        f.write(hero_code)

    # 3. Create About.jsx (The gray section in CV)
    about_code = """
import React from 'react';

const About = () => {
  return (
    <section className="dark-section">
      <div style={{maxWidth: '1200px', margin: '0 auto', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '50px'}}>
        <div>
          <p style={{fontSize: '1.1rem', lineHeight: '1.6'}}>
            Sono un UX & Service Design Manager con oltre otto anni di esperienza nella progettazione di esperienze digitali e servizi innovativi, con un focus su tecnologie IoT, AI e interfacce embedded in ambito industriale. Cresciuto professionalmente all'interno di SECO SpA, ho ricoperto ruoli di crescente responsabilità fino a guidare oggi un team multidisciplinare in progetti strategici aziendali e customer-facing.
          </p>
          <p style={{fontSize: '1.1rem', lineHeight: '1.6'}}>
            Ho lavorato su progetti chiave come lo sviluppo della piattaforma Clea, dell'editor AI Clea AI Studio e del SECO Application Hub, oltre a soluzioni custom per clienti come Daikin Applied Europe, SNAM, Fastweb, Zoppas Industries, Quanta Systems, Pizzarotti, Riello UPS, Rhea Vendors e CIAM SpA.
          </p>
        </div>
        <div>
          <h3 className="section-title-cv" style={{color: '#fff', borderBottomColor: '#fff'}}>Istruzione_</h3>
          <div className="cv-item">
            <div className="cv-date">2024 - Master</div>
            <div className="cv-org">Talent Garden | Hybrid</div>
            <div className="cv-desc">Innovation management</div>
          </div>
          <div className="cv-item">
            <div className="cv-date">2020 - Alta Formazione</div>
            <div className="cv-org">Poli Design | Milano</div>
            <div className="cv-desc">Service Design for Business</div>
          </div>
          <div className="cv-item">
            <div className="cv-date">2018 - Alta Formazione</div>
            <div className="cv-org">Poli Design | Milano</div>
            <div className="cv-desc">User Experience Design</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
"""
    with open(os.path.join(comp_dir, "About.jsx"), "w") as f:
        f.write(about_code)

    # 4. Create Experience.jsx
    exp_code = """
import React from 'react';

const experiences = [
  {
    date: "2024 - in corso",
    org: "SECO SpA",
    role: "UX e Service Design Manager",
    desc: "Guido il team di UX e Service Design in progetti strategici aziendali e attività a contatto con i clienti, con un focus su innovazione, AI e soluzioni IoT."
  },
  {
    date: "2022 - 2024",
    org: "SECO SpA",
    role: "UX e Service Design Team Leader",
    desc: "Ho coordinato un team multidisciplinare nella progettazione di esperienze digitali e servizi in ambito industriale."
  },
  {
    date: "2021 - 2022",
    org: "SECO Mind srl",
    role: "Senior UX e Service Designer",
    desc: "Ho contribuito alla definizione della visione progettuale e allo sviluppo di soluzioni digitali complesse."
  },
  {
    date: "2020 - 2021",
    org: "Aidilab srl",
    role: "UX e Service Designer",
    desc: "Ho lavorato alla progettazione di interfacce e servizi digitali orientati al valore."
  }
];

const Experience = () => {
  return (
    <section className="light-section">
      <div style={{maxWidth: '1200px', margin: '0 auto'}}>
        <h3 className="section-title-cv">Esperienze Lavorative_</h3>
        <div className="cv-grid">
          {experiences.map((exp, index) => (
            <div key={index} className="cv-item">
              <div className="cv-date">{exp.date}</div>
              <div className="cv-org">{exp.org}</div>
              <div className="cv-role">{exp.role}</div>
              <p className="cv-desc">{exp.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Experience;
"""
    with open(os.path.join(comp_dir, "Experience.jsx"), "w") as f:
        f.write(exp_code)

    # 5. Update Contact Banner (Yellow section)
    contact_code = """
import React from 'react';

const Contact = () => {
  return (
    <section className="contact-banner-cv">
      <div className="contact-item-cv">
        <label>Cellulare:</label>
        <span>(+39) 342 8047146</span>
      </div>
      <div className="contact-item-cv">
        <label>Email:</label>
        <a href="mailto:iacopo.peruzzi90@gmail.com">iacopo.peruzzi90@gmail.com</a>
      </div>
      <div className="contact-item-cv">
        <label>Linkedin:</label>
        <a href="https://www.linkedin.com/in/iacopoperuzzi/" target="_blank">linkedin.com/in/iacopoperuzzi/</a>
      </div>
    </section>
  );
};

export default Contact;
"""
    with open(os.path.join(comp_dir, "Contact.jsx"), "w") as f:
        f.write(contact_code)

    # 6. Update App.jsx
    app_code = """
import Hero from './components/Hero';
import About from './components/About';
import Experience from './components/Experience';
import Contact from './components/Contact';

function App() {
  return (
    <div className="app-container">
      <main>
        <Hero />
        <About />
        <Contact />
        <Experience />
      </main>
      <footer style={{textAlign: 'center', padding: '40px', color: '#888', fontSize: '0.8rem'}}>
        © {new Date().getFullYear()} Iacopo Peruzzi - UX & Service Design Manager
      </footer>
    </div>
  );
}

export default App;
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    print("CV Branding and content applied successfully!")

if __name__ == "__main__":
    apply_branding()
