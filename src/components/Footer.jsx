
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
