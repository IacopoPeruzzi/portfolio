import { Link } from 'react-router-dom';
import { projects } from '../data/projects';

const ClientProjects = () => {
  const clientIds = ["daikin", "quanta", "snam", "fastweb", "riello", "rhea", "ciam", "zoppas"];
  const filteredProjects = projects.filter(p => clientIds.includes(p.id));

  return (
    <section className="section section-light" id="projects">
      <div className="container">
        <span className="section-label reveal">Client Projects</span>
        <h2 className="dynamic-title">Industry-defining solutions.</h2>
        <p className="section-intro reveal">From embedded control to industrial operations, these projects translate specialist workflows, technical requirements and service opportunities into experiences people can trust.</p>
        <div className="grid-2 project-grid">
          {filteredProjects.map(item => (
            <Link key={item.id} to={`/case-study/${item.id}`} className="card portfolio-card reveal" style={{ '--reveal-delay': `${(filteredProjects.indexOf(item) % 2) * 90}ms` }}>
              {item.heroImage && (
                <div className="card-bg">
                  <img src={item.heroImage} alt={item.title} />
                  <div className="card-overlay"></div>
                </div>
              )}
              <div className="card-content">
                <span className="project-card__eyebrow">{item.metadata.client}</span>
                <h3>{item.title}</h3>
                <p>{item.subtitle}</p>
                <div className="tag-list">
                  {item.tags.slice(0, 3).map(t => <span key={t} className="tag">{t}</span>)}
                </div>
                <span className="project-card__link">View case study <b aria-hidden="true">↗</b></span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ClientProjects;
