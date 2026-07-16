
const principles = [
  {
    word: 'Clarity',
    title: "Complexity is real. Complication is optional.",
    desc: "Expert users need depth, not friction. I preserve the domain logic while making the next right action clear."
  },
  {
    word: 'Empathy',
    title: "B2B deserves genuine empathy.",
    desc: "Industrial tools shape people’s daily work. They should feel as clear, confident and considered as the best consumer experiences."
  },
  {
    word: 'Alignment',
    title: "Design is an orchestration layer.",
    desc: "The strongest experiences align engineering feasibility, business model logic and user reality before they become expensive to change."
  }
];

const DesignPrinciples = () => (
  <section className="section section-principles" id="principles">
    <div className="container">
      <span className="section-label">Design Philosophy</span>
      <h2 className="dynamic-title" style={{marginBottom: '60px'}}>Principles that drive my work.</h2>
      <div className="principles-canvas">
        {principles.map((item, i) => (
          <article key={item.title} className="principle-note" style={{ '--note-index': `0${i + 1}` }}>
            <span className="principle-note__word" aria-hidden="true">{item.word}</span>
            <span className="principle-note__index">0{i + 1}</span>
            <div className="principle-note__content">
              <h3>{item.title}</h3>
              <p>{item.desc}</p>
            </div>
          </article>
        ))}
      </div>
    </div>
  </section>
);

export default DesignPrinciples;
