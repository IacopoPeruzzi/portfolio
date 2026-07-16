

const Experience = () => {
  const experiences = [
    {
      date: "2024 - Present",
      title: "UX & Service Design Manager",
      org: "SECO SpA",
      desc: "Guida di team strategici su soluzioni IoT e AI ad alto impatto."
    },
    {
      date: "2022 - 2024",
      title: "Team Leader",
      org: "SECO SpA",
      desc: "Coordinamento di esperienze digitali per il settore industriale."
    },
    {
      date: "2021 - 2022",
      title: "Senior UX Designer",
      org: "SECO Mind srl",
      desc: "Sviluppo di architetture software-defined e interfacce complesse."
    }
  ];

  return (
    <section id="experience">
      <h2 style={{fontSize: '2.5rem', marginBottom: '50px'}}>Esperienza Professionale</h2>
      <div className="timeline">
        {experiences.map((exp, i) => (
          <div key={i} className="timeline-item">
            <div className="item-date">{exp.date}</div>
            <div className="item-title">{exp.title}</div>
            <div className="item-org">{exp.org}</div>
            <p style={{color: '#888'}}>{exp.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Experience;
