
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { name: 'About', to: '/about' },
    { name: 'Strategy', href: '/#initiatives' },
    { name: 'Selected Work', href: '/#projects' },
    { name: 'Approach', href: '/#process' },
    { name: 'Contact', href: '/#contact' },
  ];

  const toggleMenu = () => setIsOpen(!isOpen);
  const closeMenu = () => setIsOpen(false);

  React.useEffect(() => {
    if (isOpen) {
      document.body.classList.add('mobile-menu-open');
    } else {
      document.body.classList.remove('mobile-menu-open');
    }
    return () => document.body.classList.remove('mobile-menu-open');
  }, [isOpen]);

  return (
    <>
      <nav className="nav">
        <div className="nav-content">
          <Link to="/" className="brand-mark">Iacopo Peruzzi<span> / UX &amp; Service Design</span></Link>
          
          <div className="nav-links">
            {navLinks.map((link) => link.to
              ? <Link key={link.name} to={link.to}>{link.name}</Link>
              : <a key={link.name} href={link.href}>{link.name}</a>)}
          </div>

          <button className="mobile-toggle" onClick={toggleMenu} aria-label="Toggle menu">
            {isOpen ? (
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            ) : (
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            )}
          </button>
        </div>
      </nav>

      <div className={`mobile-menu ${isOpen ? 'is-open' : ''}`}>
        {navLinks.map((link) => (
          link.to
            ? <Link key={link.name} to={link.to} onClick={closeMenu}>{link.name}</Link>
            : <a key={link.name} href={link.href} onClick={closeMenu}>{link.name}</a>
        ))}
      </div>
    </>
  );
};

export default Header;
