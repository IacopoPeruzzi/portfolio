import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';

const HorizontalProjects = ({ id, label, title, intro, items, eyebrow }) => {
  const pinRef = useRef(null);
  const [progress, setProgress] = useState(0);
  const [pinWidth, setPinWidth] = useState(0);
  const [viewportWidth, setViewportWidth] = useState(() => window.innerWidth);
  const projectPairs = items.reduce((pairs, item, index) => {
    if (index % 2 === 0) pairs.push([item]);
    else pairs[pairs.length - 1].push(item);
    return pairs;
  }, []);
  const trackWidth = projectPairs.length * 38;
  const menuInset = Math.max(viewportWidth * 0.025, (viewportWidth - 1200) / 2);
  const trackPixels = viewportWidth * (trackWidth / 100) + menuInset * 2;
  const translate = trackPixels > 0 ? Math.max(0, ((trackPixels - pinWidth) / trackPixels) * 100) : 0;

  useEffect(() => {
    let frameId;

    const updateProgress = () => {
      const pin = pinRef.current;
      if (!pin || window.innerWidth <= 768) {
        setProgress(0);
        return;
      }

      const rect = pin.getBoundingClientRect();
      setPinWidth(currentWidth => currentWidth === pin.clientWidth ? currentWidth : pin.clientWidth);
      setViewportWidth(currentWidth => currentWidth === window.innerWidth ? currentWidth : window.innerWidth);
      const travel = pin.offsetHeight - window.innerHeight;
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
    <section className="section section-light horizontal-projects" id={id}>
      <div className="container horizontal-projects__header">
        <span className="section-label">{label}</span>
        <h2 className="dynamic-title">{title}</h2>
        <p className="section-intro">{intro}</p>
      </div>

      <div
        ref={pinRef}
        className="horizontal-projects__pin"
        style={{ '--horizontal-travel': `${Math.max(0, trackPixels - pinWidth) * 1.1}px` }}
      >
        <div className="horizontal-projects__sticky">
          <div
            className="horizontal-projects__track"
            style={{
              width: `${trackWidth}vw`,
              transform: `translate3d(${-progress * translate}%, 0, 0)`,
            }}
          >
            {projectPairs.map((pair, index) => (
              <article key={pair[0].id} className="horizontal-projects__panel">
                <div className="container horizontal-projects__panel-inner">
                  <span className="horizontal-projects__index">{String(index * 2 + 1).padStart(2, '0')}–{String(Math.min(index * 2 + 2, items.length)).padStart(2, '0')} / {String(items.length).padStart(2, '0')}</span>
                  <div className={`horizontal-projects__pair${pair.length === 1 ? ' horizontal-projects__pair--solo' : ''}${index % 2 === 1 ? ' horizontal-projects__pair--offset' : ''}`}>
                    {pair.map(item => (
                      <Link key={item.id} to={`/case-study/${item.id}`} className="card portfolio-card horizontal-projects__card">
                        {item.heroImage && (
                          <div className="card-bg">
                            <img src={item.heroImage} alt={item.title} />
                            <div className="card-overlay" />
                          </div>
                        )}
                        <div className="card-content">
                          <span className="project-card__eyebrow">{eyebrow(item)}</span>
                          <h3>{item.title}</h3>
                          <p>{item.subtitle}</p>
                          <div className="tag-list">
                            {item.tags.slice(0, 3).map(tag => <span key={tag} className="tag">{tag}</span>)}
                          </div>
                          <span className="project-card__link">View case study <b aria-hidden="true">↗</b></span>
                        </div>
                      </Link>
                    ))}
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

export default HorizontalProjects;
