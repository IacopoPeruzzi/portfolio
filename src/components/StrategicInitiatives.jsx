import React from 'react';
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
        <div className="grid-2" style={{marginTop: '100px'}}>
          {filteredInitiatives.map(item => (
            
            <Link key={item.id} to={`/case-study/${item.id}`} className="card reveal">
              {item.heroImage && (
                <div className="card-bg">
                  <img src={item.heroImage} alt={item.title} />
                  <div className="card-overlay"></div>
                </div>
              )}
              <div className="card-content">
                <h3 style={{fontSize: '2rem'}}>{item.title}</h3>
                <p style={{fontSize: '1.1rem'}}>{item.subtitle}</p>
                <div className="tag-list">
                  {item.tags.slice(0, 3).map(t => <span key={t} className="tag">{t}</span>)}
                </div>
              </div>
            </Link>
    
          ))}
        </div>
      </div>
    </section>
  );
};

export default StrategicInitiatives;
