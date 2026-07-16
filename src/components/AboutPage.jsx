import { Link } from 'react-router-dom';

const experience = [
  {
    period: '2024 — present',
    role: 'UX & Service Design Manager',
    company: 'SECO SpA',
    detail: 'Leading the UX and Service Design team across strategic company projects and customer-facing initiatives, with a focus on innovation, AI and IoT solutions.',
  },
  {
    period: '2022 — 2024',
    role: 'UX & Service Design Team Leader',
    company: 'SECO SpA',
    detail: 'Coordinated a multidisciplinary team designing digital experiences and services for industrial contexts, helping evolve a user-centred approach across the company.',
  },
  {
    period: '2021 — 2022',
    role: 'Senior UX & Service Designer',
    company: 'SECO Mind Srl',
    detail: 'Defined design vision and developed complex digital solutions across UX and service strategy for clients and internal products.',
  },
  {
    period: '2017 — 2021',
    role: 'UX & Service Designer',
    company: 'Aidilab Srl / University of Siena',
    detail: 'Designed digital interfaces and services, from user research and interaction flows to wireframes and prototypes for industrial solutions.',
  },
];

const AboutPage = () => (
  <article className="about-page">
    <section className="section about-page__hero">
      <div className="container">
        <Link to="/" className="back-link">← Back to portfolio</Link>
        <span className="section-label">About me</span>
        <h1>UX &amp; Service Design Manager.</h1>
        <p className="about-page__lede">
          More than nine years designing digital products, innovative services and connected experiences, with a focus on IoT, AI and embedded interfaces for industrial contexts.
        </p>
      </div>
    </section>

    <section className="section about-page__story">
      <div className="container about-page__story-grid">
        <h2>A designer by craft. A manager by practice.</h2>
        <div>
          <p>
          I grew professionally within SECO, moving from hands-on design roles to leading a multidisciplinary UX and Service Design team across strategic internal initiatives, customer-facing programmes and product-service opportunities.
          </p>
          <p>
            My work spans the Clea platform, Clea AI Studio, SECO Application Hub, SECO Developer Center and Out-of-the-box Experience, alongside custom solutions for companies including Daikin Applied Europe, Fastweb, Zoppas Industries and Quanta Systems.
          </p>
        </div>
      </div>
    </section>

    <section className="section about-page__career">
      <div className="container">
        <span className="section-label">Career</span>
        <h2>From making interfaces to leading design.</h2>
        <div className="about-page__timeline">
          {experience.map((item) => (
            <article className="career-entry" key={`${item.period}-${item.role}`}>
              <span className="career-entry__period">{item.period}</span>
              <div>
                <h3>{item.role}</h3>
                <span className="career-entry__company">{item.company}</span>
                <p>{item.detail}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>

    <section className="section about-page__focus">
      <div className="container about-page__focus-grid">
        <div>
          <span className="section-label">Current focus</span>
          <h2>Connected products, services and the systems behind them.</h2>
        </div>
        <div className="about-page__focus-copy">
          <p>
            Today I shape product and service strategy across strategic internal initiatives and customer-facing projects: from framing opportunities and business models to defining the experience direction teams can act on.
          </p>
          <p>
            The contexts are often industrial and technical: connected devices, embedded interfaces, IoT platforms, AI-enabled workflows and the operational tools that make them useful day to day.
          </p>
          <span>Product strategy · Service strategy · Business modelling · Research · Interaction design · Design leadership</span>
        </div>
      </div>
    </section>

    <section className="section about-page__education">
      <div className="container about-page__education-grid">
        <span className="section-label">Education</span>
        <div>
          <article className="education-entry">
            <span>2024</span>
            <p><strong>Master in Innovation Management</strong><br />Talent Garden — focused on innovation management.</p>
          </article>
          <article className="education-entry">
            <span>2020</span>
            <p><strong>Service Design for Business</strong><br />Advanced training course, POLI.design.</p>
          </article>
          <article className="education-entry">
            <span>2018</span>
            <p><strong>User Experience Design</strong><br />Advanced training course, POLI.design.</p>
          </article>
        </div>
        <div>
          <article className="education-entry">
            <span>2014 — 2017</span>
            <p><strong>Master’s Degree in Communication Strategies and Techniques</strong><br />University of Siena. Technologies and methods for experience design. Final grade: 110 with honours.</p>
          </article>
          <article className="education-entry">
            <span>2010 — 2014</span>
            <p><strong>Bachelor’s Degree in Communication Sciences</strong><br />University of Siena. Final grade: 106.</p>
          </article>
          <p className="about-page__languages"><strong>Languages</strong><br />Italian, native speaker · English, B2.</p>
        </div>
      </div>
    </section>
  </article>
);

export default AboutPage;
