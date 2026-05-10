import os

def refine_details():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    comp_dir = os.path.join(src_dir, "components")
    
    # Updated About.jsx with full Education and Skills
    about_code = """
import React from 'react';

const About = () => {
  return (
    <section className="dark-section">
      <div style={{maxWidth: '1200px', margin: '0 auto', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '60px'}}>
        <div>
          <h3 className="section-title-cv" style={{color: '#fff', borderBottomColor: '#fff'}}>Profilo_</h3>
          <p style={{fontSize: '1.1rem', lineHeight: '1.6', marginBottom: '30px'}}>
            Sono un UX & Service Design Manager con oltre otto anni di esperienza nella progettazione di esperienze digitali e servizi innovativi, con un focus su tecnologie IoT, AI e interfacce embedded in ambito industriale. Cresciuto professionalmente all'interno di SECO SpA, ho ricoperto ruoli di crescente responsabilità fino a guidare oggi un team multidisciplinare in progetti strategici aziendali e customer-facing.
          </p>
          
          <h3 className="section-title-cv" style={{color: '#fff', borderBottomColor: '#fff', fontSize: '1.5rem'}}>Competenze & Lingue_</h3>
          <div style={{display: 'flex', gap: '40px', flexWrap: 'wrap'}}>
            <div>
              <div className="cv-date">Lingue</div>
              <div className="cv-desc">Italiano (Madrelingua)</div>
              <div className="cv-desc">Inglese (B2)</div>
            </div>
            <div>
              <div className="cv-date">Focus</div>
              <div className="cv-desc">IoT & AI Solutions</div>
              <div className="cv-desc">Industrial Interfaces</div>
              <div className="cv-desc">Service Strategy</div>
            </div>
          </div>
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
          <div className="cv-item">
            <div className="cv-date">2014 - 2017 Laurea Magistrale</div>
            <div className="cv-org">Università degli Studi di Siena</div>
            <div className="cv-desc">Strategie e Tecniche della Comunicazione</div>
          </div>
          <div className="cv-item">
            <div className="cv-date">2010 - 2010 Laurea Triennale</div>
            <div className="cv-org">Università degli Studi di Siena</div>
            <div className="cv-desc">Strategie e Tecniche della Comunicazione</div>
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

    print("CV details refined successfully!")

if __name__ == "__main__":
    refine_details()
