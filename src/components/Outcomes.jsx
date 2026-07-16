

const outcomes = [
  { label: "15+ Projects", desc: "Unified across a single design language and ecosystem." },
  { label: "40% Faster", desc: "Onboarding and configuration time reduced for enterprise clients." },
  { label: "DesignOps", desc: "Scaling quality across distributed products and engineering teams." },
  { label: "B2B Value", desc: "Directly supporting new AI-driven subscription and service models." }
];

const Outcomes = () => (
  <section className="section" id="outcomes" style={{background: 'var(--surface-color)'}}>
    <div className="container">
      <span className="section-label">Selected Outcomes</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Impact at scale.</h2>
      <div className="grid-4" style={{display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '30px'}}>
        {outcomes.map((item, i) => (
          <div key={i}>
            <h3 style={{fontSize: '2.5rem', marginBottom: '10px'}}>{item.label}</h3>
            <p style={{color: 'var(--text-secondary)', fontSize: '0.9rem'}}>{item.desc}</p>
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Outcomes;
