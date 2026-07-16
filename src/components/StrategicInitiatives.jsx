import { Link } from 'react-router-dom';
import { projects } from '../data/projects';

const StrategicInitiatives = () => {
  // Filter the specific strategic projects
  const initiativesIds = ["clea-ecosystem", "clea-ai-studio", "app-hub", "oobe", "dev-center"];
  const filteredInitiatives = projects.filter(p => initiativesIds.includes(p.id));

  return (
    <section className="section section-light" id="initiatives" style={{overflow: 'hidden'}}>
      <div className="container">
        <span className="section-label reveal">Strategic Initiatives</span>
        <h2 className="dynamic-title reveal">Orchestrating internal platforms.</h2>
        <p className="section-intro reveal">Platform initiatives that connect SECO’s software, hardware and AI offering into clearer product and service value that customers can adopt and the business can scale.</p>
        <div className="grid-2 project-grid">
          {filteredInitiatives.map(item => (
            <Link key={item.id} to={`/case-study/${item.id}`} className="card portfolio-card reveal" style={{ '--reveal-delay': `${(filteredInitiatives.indexOf(item) % 2) * 90}ms` }}>
              {item.heroImage && (
                <div className="card-bg">
                  <img src={item.heroImage} alt={item.title} />
                  <div className="card-overlay"></div>
                </div>
              )}
              <div className="card-content">
                <span className="project-card__eyebrow">{item.metadata.context}</span>
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

export default StrategicInitiatives;
