
import { useParams, Link } from 'react-router-dom';
import { projects } from '../data/projects';
import useReveal from '../hooks/useReveal';

const CaseStudy = () => {
  const { id } = useParams();
  const project = projects.find(p => p.id === id);
  useReveal();

  if (!project) return <div>Project not found.</div>;

  return (
    <div className="case-study-page">
      <header className="cs-hero section">
        <div className="container">
          <Link to="/" className="back-link">← Back to Overview</Link>
          <div className="cs-hero-header">
            <h1 className="hero-title reveal">{project.title}</h1>
            <p className="hero-subtitle reveal" style={{ '--reveal-delay': '100ms' }}>{project.subtitle}</p>
            {project.heroImage && (
              <div className="cs-hero-image reveal" style={{ '--reveal-delay': '180ms' }}>
                <img src={project.heroImage} alt={project.title} style={{width: '100%', borderRadius: '4px', border: '1px solid var(--border-color)'}} />
              </div>
            )}
            <p className="cs-intro reveal" style={{ '--reveal-delay': '240ms' }}>
              {project.intro}
            </p>
            <div className="tag-list cs-tags reveal" style={{ '--reveal-delay': '300ms' }}>
              {project.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
          </div>
        </div>
      </header>

      <section className="cs-snapshot section reveal">
        <div className="container">
          <div className="grid-3 cs-snapshot-grid">
            <div>
              <span className="section-label">Organisation &amp; context</span>
              <p style={{fontSize: '0.9rem', }}>{project.metadata.company || project.metadata.client}</p>
              <p style={{fontSize: '0.8rem', opacity: 0.6}}>{project.metadata.context}</p>
            </div>
            <div>
              <span className="section-label">My role</span>
              <p style={{fontSize: '0.9rem', }}>{project.metadata.role}</p>
            </div>
            <div>
              <span className="section-label">Focus</span>
              <div className="tag-list" style={{marginTop: '10px'}}>
                {project.metadata.focus_areas.map(f => <span key={f} className="tag" style={{fontSize: '0.6rem'}}>{f}</span>)}
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="section reveal">
        <div className="container">
          <div className="grid-2">
            <div>
              <h2 className="cs-heading">The context</h2>
              <p className="cs-body">{project.context}</p>
            </div>
            <div>
              <h2 className="cs-heading">The design challenge</h2>
              <p className="cs-body">{project.challenge}</p>
            </div>
          </div>
        </div>
      </section>

      <section className="section cs-contribution reveal">
        <div className="container grid-2">
          <div>
            <span className="section-label">My contribution</span>
            <h2 className="cs-heading">What I led and shaped</h2>
            <p className="cs-body">{project.role_desc}</p>
          </div>
          <div>
            <span className="section-label">Approach</span>
            <h2 className="cs-heading">How the work progressed</h2>
            <p className="cs-body">{project.process}</p>
          </div>
        </div>
      </section>

      <section className="section is-light reveal" style={{background: '#f5f5f7'}}>
        <div className="container">
          <h2 className="cs-heading">How I shaped the experience</h2>
          
          {project.additionalImage && (
            <div className="cs-hero-image" style={{marginTop: '40px', marginBottom: '60px'}}>
              <img src={project.additionalImage} alt="Project Detail" style={{width: '100%', borderRadius: '4px', border: '1px solid var(--border-color)'}} />
            </div>
          )}

          <div className="grid-2" style={{marginTop: '40px', gap: '40px'}}>
            {project.decisions.map((d, i) => (
              <div key={i} className="cs-decision-card">
                <h4 style={{fontSize: '1.1rem', marginBottom: '10px'}}>{d.title}</h4>
                <p style={{fontSize: '0.9rem', lineHeight: '1.6'}}>{d.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section reveal">
        <div className="container">
          <div className="grid-2">
            <div>
              <h2 className="cs-heading">What I delivered</h2>
              <ul style={{padding: 0, listStyle: 'none'}}>
                {project.outputs.map((o, i) => (
                  <li key={i} style={{padding: '10px 0', borderBottom: '1px solid var(--border-color)', fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'capitalize'}}>
                    — {o}
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h2 className="cs-heading">Value created</h2>
              <p className="cs-body" style={{fontSize: '1.3rem', fontWeight: 300}}>{project.outcome}</p>
            </div>
          </div>
        </div>
      </section>

      <section className="section reveal" style={{borderBottom: 'none'}}>
        <div className="container">
          <h2 className="cs-heading">Design takeaway</h2>
          <p className="cs-body" style={{maxWidth: '900px'}}>{project.learnings}</p>
          
          {(() => {
            const currentIndex = projects.findIndex(p => p.id === id);
            const nextProject = projects[(currentIndex + 1) % projects.length];
            return (
              <div style={{marginTop: '120px', textAlign: 'center', borderTop: '1px solid var(--border-color)', paddingTop: '80px'}}>
                <span className="section-label">Continue exploring</span>
                <Link to={`/case-study/${nextProject.id}`} style={{fontSize: '2.5rem', fontWeight: 700, display: 'block', marginTop: '20px'}}>
                  {nextProject.title} →
                </Link>
                <div style={{marginTop: '40px'}}>
                  <Link to="/" className="back-link">Back to Overview</Link>
                </div>
              </div>
            );
          })()}
        </div>
      </section>
    </div>
  );
};

export default CaseStudy;
