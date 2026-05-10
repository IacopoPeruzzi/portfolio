
import React from 'react';

const steps = [
  { title: "Discovery & Strategy", desc: "Aligning business goals with technical constraints and user needs through strategic research." },
  { title: "Design & Architecture", desc: "Defining complex information architectures and scalable user flows for connected ecosystems." },
  { title: "Leadership & Governance", desc: "Guiding multidisciplinary teams and maintaining consistency through robust design systems." },
  { title: "Delivery & Handoff", desc: "Ensuring high-quality implementation through structured handoff and technical alignment." }
];

const Process = () => (
  <section className="section" id="process">
    <div className="container">
      <span className="section-label">Process</span>
      <h2 className="dynamic-title">A strategic approach to complexity.</h2>
      
      <div className="process-flow">
        {steps.map((step, i) => (
          <div key={i} className="process-step">
            <div className="step-number">0{i+1}</div>
            <div className="step-content">
              <h3>{step.title}</h3>
              <p>{step.desc}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Process;
