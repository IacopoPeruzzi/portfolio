
import React from 'react';

const expertise = [
  { area: "UX Strategy", details: "Product Vision, Experience Logic, Design Roadmap" },
  { area: "Service Design", details: "Ecosystems, User Journeys, Service Logic" },
  { area: "Interaction Design", details: "Complex Flows, Industrial HMI, B2B Platforms" },
  { area: "Design Leadership", details: "Team Coordination, Design Governance, DesignOps" }
];

const Expertise = () => (
  <section className="section" id="expertise">
    <div className="container">
      <span className="section-label">Expertise</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Bridging strategy and delivery.</h2>
      <div className="expertise-list">
        {expertise.map((item, i) => (
          <div key={i} className="expertise-item">
            <h3>{item.area}</h3>
            <span>{item.details}</span>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Expertise;
