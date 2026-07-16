import { useEffect, useRef, useState } from 'react';

const expertise = [
  { area: 'UX Strategy', details: 'Product vision, value propositions and the path from ambiguity to a direction teams can deliver.', focus: 'Direction' },
  { area: 'Service Design', details: 'Ecosystems, journeys and service logic that connect product value, business models and touchpoints.', focus: 'Connection' },
  { area: 'Lean & Agile Practice', details: 'Hypothesis-led discovery, iterative delivery and lightweight rituals that help teams learn, decide and adapt faster.', focus: 'Momentum' },
  { area: 'Design Leadership', details: 'Team growth, design governance and operating models that make quality repeatable.', focus: 'Capability' },
];

const Expertise = () => {
  const sectionRef = useRef(null);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let frameId;

    const updateProgress = () => {
      const section = sectionRef.current;
      if (!section) return;
      if (window.innerWidth <= 768) {
        setProgress(0);
        return;
      }

      const rect = section.getBoundingClientRect();
      const travel = section.offsetHeight - window.innerHeight;
      const nextProgress = travel > 0 ? Math.min(1, Math.max(0, -rect.top / travel)) : 0;
      setProgress(nextProgress);
    };

    const requestUpdate = () => {
      window.cancelAnimationFrame(frameId);
      frameId = window.requestAnimationFrame(updateProgress);
    };

    requestUpdate();
    window.addEventListener('scroll', requestUpdate, { passive: true });
    window.addEventListener('resize', requestUpdate);

    return () => {
      window.cancelAnimationFrame(frameId);
      window.removeEventListener('scroll', requestUpdate);
      window.removeEventListener('resize', requestUpdate);
    };
  }, []);

  return (
    <section
      className="section expertise-section expertise-horizontal-section"
      id="expertise"
    >
      <div className="container expertise-horizontal__header">
        <span className="section-label">Expertise</span>
        <h2>Bridging strategy and delivery.</h2>
          <p>From product and service strategy to meaningful outcomes, through design, business modelling, Lean and Agile practice.</p>
      </div>

      <div ref={sectionRef} className="expertise-horizontal__pin">
        <div className="expertise-horizontal__sticky">
          <div className="expertise-horizontal__track" style={{ transform: `translate3d(${-progress * 75}%, 0, 0)` }}>
            {expertise.map((item, i) => (
              <article key={item.area} className="expertise-horizontal__panel">
                <div className="container expertise-horizontal__panel-inner">
                  <span className="expertise-horizontal__index">0{i + 1} / 0{expertise.length}</span>
                  <h3>{item.area}</h3>
                  <div className="expertise-horizontal__detail">
                    <span>{item.focus}</span>
                    <p>{item.details}</p>
                  </div>
                </div>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Expertise;
