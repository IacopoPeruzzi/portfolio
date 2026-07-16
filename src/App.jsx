
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';
import useReveal from './hooks/useReveal';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import AboutPage from './components/AboutPage';
import DesignPrinciples from './components/DesignPrinciples';
import Expertise from './components/Expertise';
import StrategicInitiatives from './components/StrategicInitiatives';
import ClientProjects from './components/ClientProjects';
import Process from './components/Process';
import Contact from './components/Contact';
import CaseStudy from './components/CaseStudy';

import useThemeSwitcher from './hooks/useThemeSwitcher';

const Home = () => {
  useReveal();
  useThemeSwitcher();
  return (
    <>
      <Hero />
      <About />
      <DesignPrinciples />
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
            <Route path="/about" element={<AboutPage />} />
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
