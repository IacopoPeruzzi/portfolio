import React from 'react';
import { Link } from 'react-router-dom';
import { projects } from '../data/projects';

const ClientProjects = () => {
  const clientIds = ["daikin", "quanta", "snam", "fastweb", "riello", "rhea", "ciam", "zoppas"];
  const filteredProjects = projects.filter(p => clientIds.includes(p.id));

  return (
    <section className="section section-light" id="projects">
      <div className="container">
        <span className="section-label reveal">Client Projects</span>
        <h2 className="dynamic-title reveal">Industry-defining solutions.</h2>
        <div className="grid-2" style={{marginTop: '100px'}}>
          {filteredProjects.map(item => (
            <Link key={item.id} to={`/case-study/${item.id}`} className="card reveal">
              {item.heroImage && (
                <div className="card-bg">
                  <img src={item.heroImage} alt={item.title} />
                  <div className="card-overlay"></div>
                </div>
              )}
              <div className="card-content">
                <h3 style={{fontSize: '2rem', fontWeight: 400}}>{item.title}</h3>
                <p style={{fontSize: '1.1rem', marginTop: '10px'}}>{item.subtitle}</p>
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

export default ClientProjects;
