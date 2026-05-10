
import React from 'react';

const Contact = () => (
  <section className="section" id="contact" style={{textAlign: 'center'}}>
    <div className="container">
      <span className="section-label">Get in Touch</span>
      <h2 className="dynamic-title" style={{margin: '40px auto'}}>Let's design the next ecosystem.</h2>
      <div className="contact-links" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '15px', fontSize: '1.2rem'}}>
        <a href="https://www.linkedin.com/in/iacopoperuzzi/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="https://drive.google.com/file/d/1hCBnd-JL6xGhEbh95RCcy4Suqqgf8SPE/view?usp=sharing" target="_blank" rel="noopener noreferrer" className="cv-link">Download CV</a>
      </div>
    </div>
  </section>
);

export default Contact;
