

import { Link } from 'react-router-dom';

const About = () => (
  <section className="section" id="about">
    <div className="container grid-2 about-layout">
      <div className="about-heading">
        <span className="section-label">Profile</span>
        <h2>I build the design clarity complex products need to grow.</h2>
      </div>
      <div className="about-copy">
        <p>
          I am a UX &amp; Service Design Manager with more than nine years of experience across industrial products, connected services and embedded interfaces. I lead teams across product, service and business strategy to make technology clear, useful and scalable.
        </p>
        <Link className="about-link" to="/about">More about me <span aria-hidden="true">↗</span></Link>
      </div>
    </div>
  </section>
);

export default About;
