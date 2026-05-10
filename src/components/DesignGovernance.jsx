
import React from 'react';
import { Link } from 'react-router-dom';

const DesignGovernance = () => (
  <section className="section" id="governance" style={{background: 'var(--surface-color)'}}>
    <div className="container">
      <span className="section-label">Design Leadership</span>
      <h2 style={{fontSize: '3rem', marginBottom: '40px'}}>Governance & Scalability.</h2>
      <div className="card" style={{maxWidth: '800px'}}>
        <h3>Design System & Governance</h3>
        <p>Scaling design quality across products, teams and industrial interfaces through shared foundations and DesignOps.</p>
        <div className="tag-list">
          <span className="tag">Design System</span>
          <span className="tag">Design Governance</span>
          <span className="tag">UI Scalability</span>
        </div>
        <Link to="/case-study/design-system" style={{marginTop: '20px', display: 'block', color: 'var(--accent-color)', fontWeight: 600}}>Read Case Study →</Link>
      </div>
    </div>
  </section>
);

export default DesignGovernance;
