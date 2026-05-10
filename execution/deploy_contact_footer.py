import os

def deploy():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    components_dir = os.path.join(src_dir, "components")
    
    # 1. Contact Component
    contact_code = """
import React from 'react';

const Contact = () => {
  return (
    <section id="contact" className="contact-section">
      <div className="section-header">
        <h2 className="section-title">Parliamo del tuo progetto</h2>
        <div className="section-line"></div>
      </div>
      <div className="contact-container">
        <div className="contact-info">
          <p>Hai un'idea in mente o vuoi collaborare? Mandami un messaggio.</p>
          <div className="info-item">
            <strong>Email:</strong> iacopo@example.com
          </div>
          <div className="info-item">
            <strong>Location:</strong> Milano, Italia
          </div>
        </div>
        <form className="contact-form">
          <input type="text" placeholder="Il tuo nome" />
          <input type="email" placeholder="La tua email" />
          <textarea placeholder="Il tuo messaggio" rows="5"></textarea>
          <button type="submit" className="primary-btn">Invia Messaggio</button>
        </form>
      </div>
    </section>
  );
};

export default Contact;
"""
    with open(os.path.join(components_dir, "Contact.jsx"), "w") as f:
        f.write(contact_code)

    # 2. Footer Component
    footer_code = """
import React from 'react';

const Footer = () => {
  return (
    <footer className="main-footer">
      <div className="footer-content">
        <div className="footer-logo">IP Portfolio</div>
        <div className="footer-socials">
          <a href="#">LinkedIn</a>
          <a href="#">GitHub</a>
          <a href="#">X</a>
        </div>
        <div className="copyright">
          © {new Date().getFullYear()} Iacopo Peruzzi. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
"""
    with open(os.path.join(components_dir, "Footer.jsx"), "w") as f:
        f.write(footer_code)

    # 3. Update App.jsx to include Contact and Footer
    app_code = """
import Header from './components/Header';
import Hero from './components/Hero';
import Projects from './components/Projects';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main>
        <Hero />
        <Projects />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    # 4. Add Contact & Footer Styles to index.css
    final_styles = """
/* Contact Section Styles */
.contact-section {
  padding: 100px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.contact-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;
  margin-top: 50px;
}

.contact-info p {
  font-size: 1.2rem;
  color: #888;
  margin-bottom: 30px;
}

.info-item {
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.info-item strong {
  color: var(--accent-color);
  margin-right: 10px;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.contact-form input, .contact-form textarea {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  padding: 15px;
  border-radius: 10px;
  color: white;
  font-family: inherit;
  font-size: 1rem;
}

.contact-form input:focus, .contact-form textarea:focus {
  outline: none;
  border-color: var(--accent-color);
}

/* Footer Styles */
.main-footer {
  border-top: 1px solid var(--glass-border);
  padding: 50px 20px;
  margin-top: 100px;
  background: #050505;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
}

.footer-logo {
  font-weight: 700;
  font-size: 1.5rem;
}

.footer-socials {
  display: flex;
  gap: 30px;
}

.footer-socials a {
  color: #888;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-socials a:hover {
  color: var(--accent-color);
}

.copyright {
  color: #555;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .contact-container {
    grid-template-columns: 1fr;
  }
}
"""
    with open(os.path.join(src_dir, "index.css"), "a") as f:
        f.write(final_styles)

    print("Contact and Footer components deployed successfully!")

if __name__ == "__main__":
    deploy()
