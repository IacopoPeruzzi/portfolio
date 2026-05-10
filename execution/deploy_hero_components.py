import os

def deploy():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    components_dir = os.path.join(src_dir, "components")
    
    if not os.path.exists(components_dir):
        os.makedirs(components_dir)
        print(f"Created {components_dir}")

    # 1. Header Component
    header_code = """
import React from 'react';

const Header = () => {
  return (
    <nav className="glass-nav">
      <div className="nav-content">
        <div className="logo">IP Portfolio</div>
        <div className="nav-links">
          <a href="#work">Lavori</a>
          <a href="#about">Chi sono</a>
          <a href="#contact" className="cta-link">Contattami</a>
        </div>
      </div>
    </nav>
  );
};

export default Header;
"""
    with open(os.path.join(components_dir, "Header.jsx"), "w") as f:
        f.write(header_code)

    # 2. Hero Component
    hero_code = """
import React from 'react';

const Hero = () => {
  return (
    <section className="hero-section">
      <div className="hero-content">
        <h1 className="hero-title">Visione Digitale.<br/>Esperienza Reale.</h1>
        <p className="hero-subtitle">Sviluppo interfacce evolute e architetture scalabili per il web del futuro.</p>
        <div className="hero-actions">
          <button className="primary-btn">Vedi Progetti</button>
          <button className="secondary-btn">Scopri di più</button>
        </div>
      </div>
      <div className="hero-gradient"></div>
    </section>
  );
};

export default Hero;
"""
    with open(os.path.join(components_dir, "Hero.jsx"), "w") as f:
        f.write(hero_code)

    # 3. Update App.jsx
    app_code = """
import Header from './components/Header';
import Hero from './components/Hero';

function App() {
  return (
    <div className="app-container">
      <Header />
      <main>
        <Hero />
      </main>
    </div>
  );
}

export default App;
"""
    with open(os.path.join(src_dir, "App.jsx"), "w") as f:
        f.write(app_code)

    # 4. Update index.css with specific styles
    hero_styles = """
/* Hero & Header Styles */
.glass-nav {
  position: fixed;
  top: 0;
  width: 100%;
  height: 70px;
  background: rgba(10, 10, 10, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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

.logo {
  font-weight: 700;
  font-size: 1.2rem;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-links a {
  color: #888;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #fff;
}

.cta-link {
  background: var(--accent-color);
  color: white !important;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 500;
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 20px;
  overflow: hidden;
}

.hero-content {
  z-index: 2;
  max-width: 800px;
}

.hero-title {
  font-size: clamp(3rem, 8vw, 5rem);
  line-height: 1.1;
  margin-bottom: 1.5rem;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: #888;
  margin-bottom: 2.5rem;
  line-height: 1.5;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.primary-btn {
  background: #fff;
  color: #000;
  border: none;
  padding: 1rem 2rem;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.secondary-btn {
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 1rem 2rem;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
}

.primary-btn:hover {
  transform: scale(1.05);
}

.hero-gradient {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 113, 227, 0.15) 0%, transparent 70%);
  filter: blur(60px);
  z-index: 1;
}
"""
    with open(os.path.join(src_dir, "index.css"), "a") as f:
        f.write(hero_styles)

    print("Hero Section components deployed successfully!")

if __name__ == "__main__":
    deploy()
