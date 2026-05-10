import os

def update_content():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    data_dir = os.path.join(src_dir, "data")
    comp_dir = os.path.join(src_dir, "components")

    # 1. Update Projects Data with full text provided by the user
    projects_data = """
export const projects = [
  {
    id: "clea-ecosystem",
    title: "Clea Ecosystem",
    subtitle: "Designing the experience foundation for SECO’s connected product ecosystem.",
    intro: "Clea is SECO’s software ecosystem for connected products, enabling companies to manage devices, applications, data and services across industrial IoT scenarios. My work contributed to shaping a more coherent and scalable experience across Clea Portal, connected services, customer-facing applications and internal product initiatives.",
    tags: ["IoT Platform", "Service Design", "UX Strategy", "B2B SaaS", "Connected Products"],
    metadata: { 
      company: "SECO", 
      context: "Internal strategic product initiative", 
      role: "UX & Service Design Manager",
      focus_areas: ["Experience strategy", "platform UX", "service logic", "user flows", "stakeholder alignment", "product ecosystem design"],
      main_outputs: ["User journeys", "platform flows", "information architecture", "wireframes", "product experience concepts", "stakeholder alignment materials"]
    },
    context: "SECO’s software ecosystem brings together hardware, connectivity, data, applications and services into a platform designed for industrial and connected product scenarios. Within this context, Clea needed to support different types of users, from internal teams and product stakeholders to customers operating connected devices and services in the field. The challenge was not only to design individual interfaces, but to create a consistent experience foundation across multiple products, workflows and touchpoints.",
    challenge: "The main challenge was to make a complex technological ecosystem easier to understand, adopt and scale. Clea combines IoT infrastructure, device management, data visualization, remote operations, customer-specific applications and service enablement. This creates a high level of complexity across both the user experience and the internal product organization. The design work needed to balance multiple layers: business goals and platform strategy, technical capabilities and constraints, customer-specific requirements, user workflows and operational needs, consistency across different Clea-based applications. The goal was to move from isolated features and custom implementations toward a more coherent ecosystem experience.",
    role_desc: "As UX & Service Design Manager, I led and coordinated design activities across strategic initiatives connected to the Clea ecosystem. My contribution focused on translating business objectives, technical requirements and user needs into clear product experiences. I worked across discovery, journey mapping, UX architecture, interface direction and stakeholder alignment, collaborating with product managers, engineering teams, business stakeholders and customer-facing teams. A key part of my role was helping teams frame the product experience not only as a set of screens, but as a connected service ecosystem.",
    process: "The process combined product discovery, service design and UX/UI design activities. We started by clarifying the role of Clea within SECO’s broader offering, identifying key user groups, recurring workflows and product touchpoints. From there, we mapped journeys, service interactions and platform flows to understand where complexity emerged and where the experience needed stronger structure. The design work then moved into interface architecture, user flows, wireframes and product experience concepts, with continuous alignment across product, engineering and business stakeholders. The process was iterative and collaborative, with the goal of creating a scalable foundation that could support both internal product evolution and customer-specific applications.",
    decisions: [
      { title: "Designing Clea as an ecosystem, not a single product", desc: "One of the core design directions was to treat Clea as a connected ecosystem of products, services and operational workflows. This helped create a broader experience logic that could support platform features, custom applications, device management and service enablement." },
      { title: "Creating consistency across customer-facing applications", desc: "Clea-based solutions often need to adapt to different customer contexts. The design challenge was to preserve flexibility while maintaining a coherent experience across navigation, interaction patterns, data views and operational workflows." },
      { title: "Supporting different levels of user expertise", desc: "Clea serves both technical and non-technical users. The experience needed to support advanced configuration and operational depth without making everyday tasks harder to perform." },
      { title: "Connecting product strategy and UX execution", desc: "The work required translating strategic product goals into concrete UX decisions, helping teams move from high-level platform ambition to actionable flows, interfaces and service models." }
    ],
    outputs: ["user journeys", "service logic maps", "platform flows", "information architecture", "wireframes", "interface concepts", "customer-facing application structures", "product alignment materials", "design direction for Clea-based experiences"],
    outcome: "The work helped consolidate a clearer and more scalable experience foundation for Clea, supporting internal alignment across product, design, engineering and business teams. It also contributed to making the platform easier to communicate, extend and adapt across different industrial use cases and customer-facing solutions.",
    learnings: "This project reinforced the importance of designing platforms as ecosystems. In complex B2B and industrial contexts, the value of UX is not only in simplifying interfaces, but in creating the connective tissue between product strategy, technical architecture, service models and real operational workflows."
  },
  {
    id: "clea-ai-studio",
    title: "Clea AI Studio",
    subtitle: "Designing a visual AI workflow editor for model creation, configuration and deployment.",
    intro: "Clea AI Studio is an AI workflow editor designed to help users create, configure, preview and deploy AI flows across edge and cloud scenarios. The project focused on making complex AI processes more accessible through a visual, block-based experience integrated within the Clea ecosystem.",
    tags: ["AI Experience Design", "Flow Editor", "Edge AI", "No-code / Low-code", "UX Strategy", "IoT"],
    metadata: { 
      company: "SECO", 
      context: "Strategic internal product initiative", 
      role: "UX & Service Design Manager",
      focus_areas: ["AI workflow design", "visual editor UX", "interaction models", "information architecture", "flow logic", "product experience strategy"],
      main_outputs: ["User flows", "editor interaction model", "block logic", "wireframes", "UX concepts", "product requirements support", "interface direction"]
    },
    context: "AI workflows are often technically complex, involving data sources, preprocessing, models, outputs, integrations, deployment targets and hardware requirements. Clea AI Studio was designed as part of SECO’s broader software ecosystem to make the creation and deployment of AI-based flows more accessible, structured and scalable. The product needed to support both technical users and users who required a more guided approach to building AI-enabled applications.",
    challenge: "The main challenge was to translate complex AI pipeline logic into an experience that users could understand, configure and trust. The editor needed to support several layers of complexity: different types of blocks, input and output compatibility, model configuration, preview and validation, deployment on compatible devices, edge and cloud execution scenarios, simplified and advanced usage modes. The experience had to reduce cognitive load without hiding the technical logic required to build valid and deployable AI flows.",
    role_desc: "As UX & Service Design Manager, I contributed to shaping the product experience and coordinated design activities across the editor experience. My role included defining user flows, interaction principles, block behavior, editor logic, interface structure and design direction. I worked with product and technical stakeholders to align user needs, platform capabilities and implementation constraints. A key part of the work was making sure the editor experience could scale over time, supporting new blocks, presets, integrations, deployment options and advanced configuration needs.",
    process: "The process started from the analysis of the AI flow creation experience, identifying the main steps users would need to perform: starting from a preset or a blank flow, adding blocks, connecting them, configuring settings, running previews, validating results and deploying the final output. We then translated this logic into a visual editor model, defining how users could interact with the whiteboard, add compatible blocks, connect inputs and outputs, inspect block details, manage settings and understand the state of the flow. The design process also explored different levels of guidance, from simplified wizard-like experiences to advanced editing capabilities for more technical users.",
    decisions: [
      { title: "Moving from technical pipelines to visual flows", desc: "The core interaction model translated AI pipelines into visual flows made of connected blocks. This helped users understand relationships between inputs, processing steps, models, outputs and integrations." },
      { title: "Designing compatibility as part of the experience", desc: "Block compatibility became a key design constraint. The experience needed to guide users toward valid connections by filtering compatible blocks and making input and output logic easier to understand." },
      { title: "Supporting preview before deployment", desc: "Previewing flows before deployment was central to the experience. It allowed users to validate intermediate or final results, understand whether the flow was working as expected and reduce uncertainty before moving to production scenarios." },
      { title: "Balancing simplicity and advanced control", desc: "The product needed to support different user profiles. The design direction combined guided flows and presets for faster adoption with advanced configuration capabilities for users who needed more control." },
      { title: "Connecting AI creation with device deployment", desc: "A key experience requirement was connecting flow creation with deployment on compatible devices. The interface needed to make hardware compatibility visible and support a smoother transition from design to execution." }
    ],
    outputs: ["editor user flows", "flow creation logic", "block categories and interaction rules", "whiteboard interaction patterns", "compatibility logic concepts", "preview experience flows", "deployment flow concepts", "wireframes and interface structures", "UX requirements and product alignment materials"],
    outcome: "The work helped define a structured experience model for Clea AI Studio, creating a foundation for a scalable AI workflow editor within the Clea ecosystem. It supported clearer alignment between product, design and engineering teams and helped translate a technically complex product vision into a more accessible user experience.",
    learnings: "This project highlighted the importance of designing AI tools around clarity, guidance and trust. In AI-enabled products, users need to understand not only what they can do, but also why something works, what is compatible and what happens when a flow is executed or deployed."
  },
  {
    id: "daikin",
    title: "Daikin Applied Europe",
    subtitle: "Designing an embedded HMI and companion app for professional HVAC workflows.",
    intro: "For Daikin Applied Europe, the project focused on the UX/UI design of a next-generation Room Controller and a companion smartphone app supporting installers during setup, troubleshooting and configuration activities.",
    tags: ["Embedded UX", "Industrial HMI", "Mobile App", "HVAC", "Professional Workflows", "UX/UI Design"],
    metadata: { 
      client: "Daikin Applied Europe", 
      context: "Customer-facing project", 
      role: "UX & Service Design Team Leader",
      focus_areas: ["Embedded HMI UX", "mobile companion experience", "interaction flows", "usability", "interface design", "installer workflows", "stakeholder alignment"],
      main_outputs: ["Functional analysis", "user flows", "wireframes", "UI concepts", "interaction patterns", "prototype support", "interface specifications"]
    },
    context: "Daikin Applied Europe needed to design the user experience and interface for a new Room Controller, together with a smartphone app supporting professional installation and configuration workflows. The Room Controller operated in a constrained embedded environment, with a 4.3” display powered by a microcontroller. This required a tailored design approach, where usability, clarity, responsiveness and technical feasibility had to be balanced from the beginning.",
    challenge: "The main challenge was to design a clear and efficient experience within a non-standard hardware environment. The interface had to support real HVAC use cases while respecting display size, hardware performance and interaction constraints. At the same time, the companion app needed to simplify the work of installers by supporting setup, troubleshooting and system configuration. The project required designing across two connected touchpoints: the embedded controller and the mobile app. Each had a different context of use, but both needed to feel coherent and operationally effective.",
    role_desc: "As UX & Service Design Team Leader, I led the design work while actively contributing hands-on across the UX/UI process. I coordinated the design activities, aligned the team with client stakeholders and technical counterparts, and directly worked on user flows, interaction logic, wireframes, UI definition and design refinement. My role combined design leadership and operational execution, ensuring that strategic decisions, usability requirements and implementation constraints were translated into a coherent experience across both the embedded Room Controller and the companion app.",
    process: "The project started with user and functional analysis to understand the main use cases, system requirements and interaction constraints. We then defined key workflows for the Room Controller, identifying how users would navigate, configure and interact with the device. The embedded interface was designed iteratively, with attention to clarity, hierarchy, feedback and performance constraints. For the companion app, the design process focused on installer workflows, including setup guidance, configuration support and troubleshooting. The goal was to reduce friction in field operations and create a more efficient connection between hardware and software.",
    decisions: [
      { title: "Designing for a constrained embedded environment", desc: "The Room Controller required an interface specifically designed for a small HMI display and microcontroller-based system. This influenced information density, interaction patterns, visual hierarchy and feedback mechanisms." },
      { title: "Supporting professional workflows", desc: "The experience was designed around real operational tasks, not generic app patterns. Setup, configuration and troubleshooting needed to be fast, clear and reliable for users working in professional contexts." },
      { title: "Creating continuity between HMI and mobile app", desc: "The controller and the companion app served different purposes, but they were part of the same product experience. The design aimed to create coherence across touchpoints while respecting the specific constraints of each device." },
      { title: "Reducing friction for installers", desc: "The companion app was designed to support installers through guided workflows, helping them perform configuration and troubleshooting activities with greater clarity." }
    ],
    outputs: ["user and functional analysis", "HMI user flows", "mobile app flows", "wireframes", "UI mockups", "interaction patterns", "prototype support", "design specifications for implementation"],
    outcome: "The project delivered a more structured and coherent experience across the embedded Room Controller and its companion app. The design helped translate complex HVAC configuration workflows into clearer interactions, supporting usability, implementation feasibility and professional field use.",
    learnings: "This project reinforced the importance of designing from real constraints. In embedded and industrial products, successful UX depends on understanding not only users and tasks, but also hardware limits, performance requirements and the physical context in which the interface is used."
  },
  {
    id: "quanta",
    title: "Quanta Systems",
    subtitle: "Shaping IoT and AI service concepts for medical and aesthetic applications.",
    intro: "For Quanta Systems, the project focused on strategic service design activities aimed at exploring new IoT and AI-driven service opportunities in the medical and aesthetic sectors.",
    tags: ["Service Design", "Strategic Research", "IoT Services", "AI Services", "Business Design", "Medical & Aesthetic"],
    metadata: { 
      client: "Quanta Systems", 
      context: "Customer-facing strategic design project", 
      role: "UX & Service Design Team Leader",
      focus_areas: ["Market research", "service concept definition", "business model exploration", "value proposition design", "user and industry needs", "stakeholder alignment"],
      main_outputs: ["Research insights", "opportunity areas", "service concepts", "business model directions", "value proposition materials", "strategic design materials"]
    },
    context: "Quanta Systems operates in medical and aesthetic technology contexts, where connected products, data and AI can open new opportunities for service innovation. The project explored how IoT and AI could support new value propositions, service models and business opportunities beyond the physical product itself. The goal was to identify service concepts that could align technology potential with user needs, market expectations and business strategy.",
    challenge: "The main challenge was to move from technological opportunity to service value. IoT and AI can enable many possible scenarios, but not every scenario becomes a meaningful service. The design work needed to identify where connected capabilities, data and automation could create relevant value for users, professionals and the business. The project required balancing innovation, feasibility, market relevance and strategic positioning.",
    role_desc: "As UX & Service Design Team Leader, I led the strategic design activities while actively contributing hands-on throughout the service design process. I coordinated the project work, supported stakeholder alignment and directly contributed to research synthesis, opportunity framing, service concept definition, value proposition design and business model exploration. My role was to connect strategic direction with concrete service design outputs, helping translate market insights, user needs and technology opportunities into structured service scenarios for IoT and AI-driven applications.",
    process: "The process combined market research, service design methodologies and business design activities. We explored industry trends, user needs, technology opportunities and possible service models. From this analysis, we identified opportunity areas where IoT and AI could create value within medical and aesthetic workflows. The work then moved into concept definition, where potential services were structured around target users, value propositions, touchpoints, operational implications and business opportunities.",
    decisions: [
      { title: "Starting from service value, not technology", desc: "The project did not treat IoT and AI as standalone innovations. The design process focused on identifying where these technologies could support real user needs, operational improvement or business differentiation." },
      { title: "Exploring new business models", desc: "A key part of the work was understanding how connected services could extend the value of products over time, opening opportunities for recurring value, service-based offerings and stronger customer relationships." },
      { title: "Connecting market insights and user needs", desc: "The service concepts were shaped by combining market analysis with user and industry needs, helping ensure that proposed directions were strategically relevant and not only technologically possible." },
      { title: "Framing AI as part of a service ecosystem", desc: "AI was considered as part of a broader service experience, connected to data, workflows, decision points and customer value." }
    ],
    outputs: ["market research synthesis", "opportunity areas", "service scenarios", "value proposition concepts", "business model directions", "strategic design materials", "presentation materials for stakeholder alignment"],
    outcome: "The work helped define scalable service concepts that connected IoT and AI opportunities with user value and business strategy. It provided a structured foundation for exploring new service directions in medical and aesthetic applications, supporting strategic alignment and future development opportunities.",
    learnings: "This project reinforced the role of service design as a bridge between innovation and business value. When working with emerging technologies, the strongest opportunities often come from understanding how technology can become part of a service model, not just a product feature."
  }
];
"""
    with open(os.path.join(data_dir, "projects.js"), "w") as f:
        f.write(projects_data)

    # 2. Update CaseStudy.jsx template to handle lists and detailed snapshot
    case_study_template = """
import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { projects } from '../data/projects';

const CaseStudy = () => {
  const { id } = useParams();
  const project = projects.find(p => p.id === id);

  if (!project) return <div>Project not found.</div>;

  return (
    <div className="case-study-page">
      <header className="cs-hero section">
        <div className="container">
          <Link to="/" className="back-link">← Back to Overview</Link>
          <div style={{marginTop: '60px'}}>
            <h1 className="hero-title">{project.title}</h1>
            <p className="hero-subtitle">{project.subtitle}</p>
            <p className="cs-intro" style={{marginTop: '30px', maxWidth: '800px', fontSize: '1.2rem', color: 'var(--text-secondary)'}}>
              {project.intro}
            </p>
            <div className="tag-list" style={{marginTop: '40px'}}>
              {project.tags.map(t => <span key={t} className="tag" style={{fontSize: '0.8rem', padding: '6px 15px'}}>{t}</span>)}
            </div>
          </div>
        </div>
      </header>

      <section className="section cs-snapshot" style={{background: 'var(--surface-color)'}}>
        <div className="container grid-3" style={{gap: '40px'}}>
          <div>
            <label className="section-label">Entity</label>
            <p>{project.metadata.company || project.metadata.client}</p>
            <label className="section-label" style={{marginTop: '20px'}}>Context</label>
            <p>{project.metadata.context}</p>
            <label className="section-label" style={{marginTop: '20px'}}>My Role</label>
            <p>{project.metadata.role}</p>
          </div>
          <div>
            <label className="section-label">Focus Areas</label>
            <ul style={{paddingLeft: '20px', color: 'var(--text-secondary)', fontSize: '0.9rem'}}>
              {project.metadata.focus_areas.map((item, i) => <li key={i}>{item}</li>)}
            </ul>
          </div>
          <div>
            <label className="section-label">Main Outputs</label>
            <ul style={{paddingLeft: '20px', color: 'var(--text-secondary)', fontSize: '0.9rem'}}>
              {project.metadata.main_outputs.map((item, i) => <li key={i}>{item}</li>)}
            </ul>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container grid-2">
          <div>
            <h2 className="cs-heading">Context</h2>
            <p className="cs-body">{project.context}</p>
          </div>
          <div>
            <h2 className="cs-heading">The Challenge</h2>
            <p className="cs-body">{project.challenge}</p>
          </div>
        </div>
      </section>

      <section className="section" style={{borderTop: '1px solid var(--border-color)'}}>
        <div className="container">
          <h2 className="cs-heading">My Role</h2>
          <p className="cs-body" style={{maxWidth: '900px'}}>{project.role_desc}</p>
        </div>
      </section>

      <section className="section" style={{background: 'var(--surface-color)'}}>
        <div className="container">
          <h2 className="cs-heading">Process</h2>
          <p className="cs-body" style={{maxWidth: '900px'}}>{project.process}</p>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2 className="cs-heading">Key Design Decisions</h2>
          <div className="grid-2" style={{marginTop: '40px'}}>
            {project.decisions.map((decision, i) => (
              <div key={i} style={{marginBottom: '30px'}}>
                <h4 style={{fontSize: '1.2rem', marginBottom: '10px', color: '#fff'}}>{decision.title}</h4>
                <p className="cs-body" style={{fontSize: '1rem'}}>{decision.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section" style={{background: 'var(--surface-color)'}}>
        <div className="container grid-2">
          <div>
            <h2 className="cs-heading">Outputs</h2>
            <ul className="cs-body" style={{paddingLeft: '20px'}}>
              {project.outputs.map((out, i) => <li key={i}>{out}</li>)}
            </ul>
          </div>
          <div>
            <h2 className="cs-heading">Outcome</h2>
            <p className="cs-body">{project.outcome}</p>
          </div>
        </div>
      </section>

      <section className="section" style={{borderBottom: 'none'}}>
        <div className="container">
          <h2 className="cs-heading">Learning</h2>
          <p className="cs-body" style={{maxWidth: '900px'}}>{project.learnings}</p>
          <div style={{marginTop: '120px', textAlign: 'center'}}>
            <Link to="/" className="back-link" style={{fontSize: '1.2rem', border: '1px solid var(--border-color)', padding: '15px 40px', borderRadius: '30px'}}>Back to Overview</Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default CaseStudy;
"""
    with open(os.path.join(comp_dir, "CaseStudy.jsx"), "w") as f:
        f.write(case_study_template)

    print("Case study contents and template updated successfully!")

if __name__ == "__main__":
    update_content()
