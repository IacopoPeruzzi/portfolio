import os

def clean_text(text):
    return text.replace("[Non verificato] ", "").replace("[Non verificato]", "")

def update_all_data():
    src_dir = "/Users/iacopoperuzzi/Documents/projects/portfolio/web-app/src"
    data_dir = os.path.join(src_dir, "data")
    comp_dir = os.path.join(src_dir, "components")

    # 1. Full Projects Database (9 Projects)
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
    id: "app-hub",
    title: "SECO Application Hub",
    subtitle: "Designing a developer-oriented hub to simplify the discovery, evaluation and deployment of AI applications.",
    intro: "SECO Application Hub is a platform initiative designed to support developers, product teams and customers in exploring ready-to-use AI applications, software resources and deployment assets for edge devices. The project focused on making AI experimentation and adoption easier by connecting applications, models, documentation, hardware compatibility and onboarding resources into a more structured experience.",
    tags: ["Developer Experience", "Edge AI", "Application Marketplace", "Product Enablement", "IoT", "UX Strategy"],
    metadata: { 
      company: "SECO", 
      context: "Strategic internal product initiative", 
      role: "UX & Service Design Manager",
      focus_areas: ["Developer experience", "product discovery", "application browsing", "onboarding", "hardware compatibility", "information architecture", "go-to-market enablement"],
      main_outputs: ["User flows", "platform structure", "application detail logic", "information architecture", "UX concepts", "product requirements support", "content structure"]
    },
    context: "SECO Application Hub was designed to support the discovery and evaluation of software resources for edge AI scenarios. The initiative aimed to create a more accessible entry point for users who need to understand which applications, models, containers and guides are available, how they relate to specific hardware platforms and how they can be used to accelerate experimentation or solution development.",
    challenge: "The main challenge was to reduce the friction between interest in edge AI and practical adoption. Users need to quickly understand what is available, which resources are compatible with their hardware, how applications can be evaluated and what steps are required to move from exploration to implementation. The experience had to support different needs: discovering ready-to-use applications, understanding compatibility with SECO hardware, accessing technical resources and guides, browsing applications by vendor or use case, supporting experimentation with AI models and components, connecting product exploration with business and technical adoption.",
    role_desc: "As UX & Service Design Manager, I led the experience design activities related to Application Hub, supporting the definition of its role within SECO’s broader product ecosystem. My work focused on structuring the experience around discovery, evaluation and activation. I contributed to information architecture, user flows, application browsing logic, content models and the relationship between Application Hub, hardware products, documentation and go-to-market initiatives.",
    process: "The process started by mapping the expected user needs around AI application discovery, hardware evaluation and technical onboarding. We identified the main content types and product objects that users would interact with, including applications, containers, models, guides, vendors, compatible devices and technical requirements. The design work then focused on structuring navigation, filtering, application detail pages and user journeys from discovery to evaluation. Particular attention was given to how users could understand whether a resource was relevant, compatible and actionable.",
    decisions: [
      { title: "Designing for discovery and activation", desc: "The experience was not designed only as a catalog. It needed to help users move from browsing resources to understanding how to use them in real edge AI scenarios." },
      { title: "Making compatibility visible", desc: "Hardware and software compatibility were central to the experience. The design needed to make compatibility information easy to find and understand, reducing uncertainty during evaluation." },
      { title: "Structuring applications around use value", desc: "Applications needed to be presented not only as technical assets, but as solutions connected to use cases, requirements, vendors and implementation paths." },
      { title: "Supporting a self-service adoption model", desc: "Application Hub was designed to reduce dependency on manual support by making resources, guides and application information more accessible and actionable." }
    ],
    outputs: ["user flows", "information architecture", "application browsing logic", "application detail structure", "filtering and grouping concepts", "vendor grouping logic", "compatibility information models", "onboarding and guide structure", "UX concepts and product alignment materials"],
    outcome: "The work contributed to defining Application Hub as a structured experience for discovering and evaluating AI applications in the SECO ecosystem. It helped connect technical resources, hardware compatibility and product adoption into a clearer user journey.",
    learnings: "This project reinforced the importance of designing developer-oriented platforms around clarity, relevance and actionability. In technical ecosystems, users do not only need access to resources, they need to understand what those resources are for, whether they fit their context and how to start using them."
  },
  {
    id: "oobe",
    title: "Out-of-the-box Experience",
    subtitle: "Reducing friction from first setup to product activation across touchpoints.",
    intro: "The Out-of-the-box Experience initiative focused on improving the first-use journey for SECO products, helping users move from receiving a device to understanding, activating and using it more effectively. The goal was to connect hardware, software, documentation and onboarding into a smoother product experience.",
    tags: ["Onboarding", "Product Experience", "Developer Experience", "Hardware UX", "Service Design", "Customer Experience"],
    metadata: { 
      company: "SECO", 
      context: "Strategic internal product initiative", 
      role: "UX & Service Design Manager",
      focus_areas: ["First-use journey", "onboarding", "setup experience", "documentation touchpoints", "product activation", "ecosystem alignment"],
      main_outputs: ["User journey maps", "onboarding flows", "touchpoint mapping", "experience principles", "content structure", "service logic", "product activation concepts"]
    },
    context: "In industrial and embedded technology contexts, the product experience does not start when users open a digital interface. It starts when they receive the hardware, unbox it, connect it, search for documentation, configure software and try to understand how to reach the first meaningful result. The Out-of-the-box Experience initiative addressed this critical transition between product delivery and product activation.",
    challenge: "The main challenge was to reduce the complexity users experience during initial setup and activation. SECO products often involve several layers: physical hardware, operating systems, software tools, technical documentation, development resources, connectivity, product-specific configuration, support channels. For users, the challenge is not only understanding each individual component, but understanding how they fit together and what to do first.",
    role_desc: "As UX & Service Design Manager, I led the design activities focused on the first-use journey and product activation experience. My contribution included mapping the onboarding flow, identifying friction points, structuring key touchpoints and aligning stakeholders around a more user-centered view of product setup.",
    process: "The process started by mapping the user journey from product reception to first successful use. We analyzed the touchpoints users encounter during setup, including packaging, printed or digital instructions, documentation, software access, product configuration and support resources. From this mapping, we identified gaps, ambiguities and opportunities to create a more guided and coherent experience.",
    decisions: [
      { title: "Treating onboarding as a service journey", desc: "The first-use experience was treated as a cross-touchpoint journey, not as a single setup screen. This allowed us to consider the relationship between hardware, software, documentation and support." },
      { title: "Reducing uncertainty during first use", desc: "The design focused on helping users understand what they have, what they need, what to do first and where to find the right resources." },
      { title: "Connecting physical and digital touchpoints", desc: "A key direction was to create continuity between the product received by the user and the digital ecosystem that supports its activation." },
      { title: "Supporting different user profiles", desc: "The experience needed to work for developers, product teams, system integrators and customers with different levels of technical expertise." }
    ],
    outputs: ["first-use journey maps", "touchpoint mapping", "onboarding flows", "setup experience principles", "content structure", "service logic", "product activation concepts", "stakeholder alignment materials"],
    outcome: "The work helped frame the Out-of-the-box Experience as a strategic component of product adoption. It provided a clearer foundation for improving the transition from product delivery to product activation.",
    learnings: "This project reinforced that onboarding is not only a usability problem, but a business-critical experience. The first moments after receiving a product can shape trust, adoption and perceived value across the entire customer relationship."
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
    challenge: "The main challenge was to design a clear and efficient experience within a non-standard hardware environment. The interface had to support real HVAC use cases while respecting display size, hardware performance and interaction constraints. At the same time, the companion app needed to simplify the work of installers by supporting setup, troubleshooting and system configuration. The project required designing across two connected touchpoints: the embedded controller and the mobile app.",
    role_desc: "As UX & Service Design Team Leader, I led the design work while actively contributing hands-on across the UX/UI process. I coordinated the design activities, aligned the team with client stakeholders and technical counterparts, and directly worked on user flows, interaction logic, wireframes, UI definition and design refinement.",
    process: "The project started with user and functional analysis to understand the main use cases, system requirements and interaction constraints. We then defined key workflows for the Room Controller, identifying how users would navigate, configure and interact with the device. The embedded interface was designed iteratively, with attention to clarity, hierarchy, feedback and performance constraints.",
    decisions: [
      { title: "Designing for a constrained embedded environment", desc: "The Room Controller required an interface specifically designed for a small HMI display and microcontroller-based system. This influenced information density, interaction patterns, visual hierarchy and feedback mechanisms." },
      { title: "Supporting professional workflows", desc: "The experience was designed around real operational tasks, not generic app patterns. Setup, configuration and troubleshooting needed to be fast, clear and reliable for users working in professional contexts." },
      { title: "Creating continuity between HMI and mobile app", desc: "The controller and the companion app served different purposes, but they were part of the same product experience. The design aimed to create coherence across touchpoints." }
    ],
    outputs: ["user and functional analysis", "HMI user flows", "mobile app flows", "wireframes", "UI mockups", "interaction patterns", "prototype support", "design specifications for implementation"],
    outcome: "The project delivered a more structured and coherent experience across the embedded Room Controller and its companion app. The design helped translate complex HVAC configuration workflows into clearer interactions.",
    learnings: "This project reinforced the importance of designing from real constraints. In embedded and industrial products, successful UX depends on understanding not only users and tasks, but also hardware limits, performance requirements and the physical context."
  },
  {
    id: "snam",
    title: "SNAM",
    subtitle: "Designing operational applications for methane leak detection and prevention.",
    intro: "For SNAM, the project focused on designing Clea Portal applications supporting methane leak detection and prevention workflows in industrial facilities. The applications were conceived as digital companions for laser cameras used to detect methane leaks, helping users access operational information and support prevention-oriented activities.",
    tags: ["Industrial Monitoring", "Safety", "Clea Portal", "IoT Applications", "Operational UX", "Energy"],
    metadata: { 
      client: "SNAM", 
      context: "Customer-facing project", 
      role: "UX & Service Design contribution",
      focus_areas: ["Operational workflows", "industrial monitoring", "methane leak detection", "data visualization", "Clea Portal applications", "safety-related use cases"],
      main_outputs: ["User flows", "application structure", "operational views", "UX/UI concepts", "data visualization logic", "stakeholder alignment materials"]
    },
    context: "The project was connected to the use of laser camera technology for methane leak detection within industrial plants. Within this scenario, Clea Portal applications were designed to support the monitoring and prevention workflow, giving users a digital layer to access relevant operational information and interact with detection-related data. The broader context was highly sensitive, involving safety, environmental risk and industrial operations.",
    challenge: "The main challenge was to design an operational experience around critical detection workflows. Methane leak detection involves complex field conditions, specialized hardware and information that must be clear, timely and actionable. The experience needed to support users in understanding what was happening, where attention was required and how detection data could contribute to prevention activities.",
    role_desc: "My role focused on contributing to the UX and service design definition of Clea-based applications for SNAM. The work involved translating operational needs and detection workflows into application structures, user flows and interface concepts aligned with Clea Portal. The goal was to make technical and safety-related information easier to access, interpret and use within an industrial monitoring context.",
    process: "The design process started from understanding the operational scenario, the role of the laser cameras and the type of information users needed to access through the digital application. We then structured key user flows and application views to support monitoring, inspection and prevention-related activities. The design work was developed within the Clea Portal ecosystem, balancing customer-specific requirements with platform consistency.",
    decisions: [
      { title: "Designing around operational clarity", desc: "The experience needed to make critical information easy to identify and interpret, especially in a context where users may need to act based on detection events or risk-related data." },
      { title: "Connecting hardware signals with digital workflows", desc: "The applications acted as a digital layer around detection hardware, translating sensor and camera outputs into operationally useful views." },
      { title: "Maintaining consistency with Clea Portal", desc: "Since the solution was part of the Clea ecosystem, the design needed to remain consistent with platform patterns while adapting to SNAM’s specific use case." },
      { title: "Supporting prevention, not only monitoring", desc: "The product experience was framed around prevention and operational awareness, not simply data visualization." }
    ],
    outputs: ["user flows", "application structure", "operational views", "monitoring logic", "UX/UI concepts", "data visualization patterns", "Clea Portal alignment materials"],
    outcome: "The work contributed to the definition of operational applications supporting methane leak detection and prevention workflows within industrial environments. It helped translate a specialized hardware and safety scenario into a more accessible digital experience.",
    learnings: "This project reinforced the importance of designing industrial monitoring experiences around clarity, trust and operational relevance. In safety-related contexts, UX must help users understand data quickly and support informed action."
  },
  {
    id: "fastweb",
    title: "Fastweb",
    subtitle: "Designing monitoring and alerting tools for distributed telecom infrastructure.",
    intro: "For Fastweb, the project focused on Clea Portal applications supporting a custom SECO hardware solution installed inside underground fiber infrastructure. The system was designed to detect access events in the field and trigger alerts, improving visibility, monitoring and operational control across distributed telecom assets.",
    tags: ["Field Operations", "Telecom Infrastructure", "Monitoring", "Alerts", "IoT Applications", "Clea Portal"],
    metadata: { 
      client: "Fastweb", 
      context: "Customer-facing project", 
      role: "UX & Service Design contribution",
      focus_areas: ["Field operations", "monitoring workflows", "alerting experience", "distributed infrastructure", "Clea Portal applications", "operational visibility"],
      main_outputs: ["Workflow analysis", "user flows", "application structure", "monitoring views", "alerting logic", "UX/UI concepts"]
    },
    context: "Fastweb needed a digital experience to support a custom SECO hardware solution installed inside underground fiber enclosures. The system detects access events and triggers alerts when field activity is identified, helping improve infrastructure security and situational awareness. A dedicated research phase was carried out to understand installation and monitoring workflows.",
    challenge: "The main challenge was to design a monitoring and alerting experience for distributed infrastructure assets. The solution needed to support users who manage field events across physical locations, where visibility, response time and reliability are critical. The design work needed to make event detection understandable and actionable, while supporting the operational workflow of technicians and monitoring teams.",
    role_desc: "I contributed to the UX and service design activities for the Fastweb project, supporting the translation of field monitoring needs into application flows and interface structures. The work involved understanding operational workflows, defining how access events and alerts should be represented and ensuring that the experience could support technicians and operations teams in real use contexts.",
    process: "The process started with research and workflow analysis to understand the installation and monitoring context. We mapped how users would interact with the system, what information they needed to access and how alerts should support operational decision-making. The design work then focused on application structure, monitoring views, alert logic and user flows.",
    decisions: [
      { title: "Designing for distributed infrastructure", desc: "The experience needed to represent events across multiple field locations, supporting users in understanding where activity was detected and what required attention." },
      { title: "Making alerts actionable", desc: "Alerts were designed not only as notifications, but as operational triggers connected to monitoring and response workflows." },
      { title: "Supporting technician and operations workflows", desc: "The design was shaped around real installation and monitoring activities, ensuring that the application supported the needs of users working across field and control environments." },
      { title: "Connecting hardware events with platform visibility", desc: "The system needed to translate physical access detection into a digital monitoring experience inside Clea Portal." }
    ],
    outputs: ["workflow analysis", "monitoring user flows", "application structure", "alerting experience concepts", "event visualization logic", "UX/UI concepts", "Clea Portal application structures"],
    outcome: "The project delivered a field-ready monitoring and alerting experience designed to improve visibility, reduce response times and increase control across distributed telecom assets.",
    learnings: "This project reinforced the importance of designing alerting systems around operational context. In distributed infrastructure scenarios, the value of an alert depends on how clearly it helps users understand what happened and where."
  },
  {
    id: "riello",
    title: "Riello UPS",
    subtitle: "Migrating and redesigning custom applications within Clea Portal.",
    intro: "For Riello UPS, the project focused on migrating and enhancing existing applications by integrating them into Clea Portal. The design work aimed to ensure a smoother transition, improve usability and expand the applications’ capabilities within a scalable platform environment.",
    tags: ["Clea Portal", "Application Redesign", "Platform Integration", "Enterprise UX", "IoT Services", "B2B"],
    metadata: { 
      client: "Riello UPS", 
      context: "Customer-facing project", 
      role: "UX & Service Design contribution",
      focus_areas: ["Application migration", "UX redesign", "platform integration", "Clea Portal customization", "usability improvement", "service scalability"],
      main_outputs: ["Application analysis", "user flows", "redesigned application structures", "UX/UI concepts", "platform integration logic"]
    },
    context: "Riello UPS needed to migrate and enhance existing applications by integrating them into Clea Portal. The project involved adapting legacy applications, optimizing their usability within Clea and expanding their capabilities to better leverage the platform’s potential. This required balancing continuity with the existing application logic and the opportunity to improve the experience.",
    challenge: "The main challenge was to redesign and integrate existing applications without losing functional continuity. Legacy applications often carry established workflows, user expectations and business-specific logic. Moving them into Clea Portal required a careful balance between preserving what worked and improving usability, consistency and scalability.",
    role_desc: "I contributed to the UX and service design work for the Riello UPS applications within Clea Portal. My contribution focused on understanding the existing application logic, supporting the redesign of flows and interface structures and aligning the solution with the Clea platform experience.",
    process: "The process started with analysis of the existing applications and their core workflows. We identified what needed to be preserved, what could be improved and how the applications could be adapted to Clea Portal. The design work then focused on restructuring the experience, optimizing usability and defining application flows and interface concepts.",
    decisions: [
      { title: "Preserving continuity while improving usability", desc: "The redesign needed to respect existing workflows while simplifying interaction patterns and improving overall clarity." },
      { title: "Integrating customer-specific logic into Clea Portal", desc: "The applications had to remain tailored to Riello UPS needs while aligning with Clea Portal’s broader platform structure." },
      { title: "Designing for scalability", desc: "The experience was structured to support future extensions, helping the customer benefit from the platform’s broader capabilities." },
      { title: "Turning migration into product improvement", desc: "The project was not treated as a simple technical migration, but as an opportunity to improve user experience and service value." }
    ],
    outputs: ["application analysis", "user flow redesign", "application structure definition", "UX/UI concepts", "platform integration logic", "platform integration materials", "stakeholder alignment materials"],
    outcome: "The project supported a smooth integration of Riello UPS applications into Clea Portal, improving usability and creating a more powerful and scalable solution aligned with the customer’s business objectives.",
    learnings: "This project reinforced that migration projects are not only technical transitions. When approached through UX and service design, they can become opportunities to simplify workflows and improve adoption."
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
    challenge: "The main challenge was to move from technological opportunity to service value. IoT and AI can enable many possible scenarios, but not every scenario becomes a meaningful service. The design work needed to identify where connected capabilities, data and automation could create relevant value for users, professionals and the business.",
    role_desc: "As UX & Service Design Team Leader, I led the strategic design activities while actively contributing hands-on throughout the service design process. I coordinated the project work, supported stakeholder alignment and directly contributed to research synthesis, opportunity framing, service concept definition, value proposition design and business model exploration.",
    process: "The process combined market research, service design methodologies and business design activities. We explored industry trends, user needs, technology opportunities and possible service models. From this analysis, we identified opportunity areas where IoT and AI could create value within medical and aesthetic workflows.",
    decisions: [
      { title: "Starting from service value, not technology", desc: "The project did not treat IoT and AI as standalone innovations. The design process focused on identifying where these technologies could support real user needs, operational improvement or business differentiation." },
      { title: "Exploring new business models", desc: "A key part of the work was understanding how connected services could extend the value of products over time, opening opportunities for recurring value, service-based offerings and stronger customer relationships." },
      { title: "Connecting market insights and user needs", desc: "The service concepts were shaped by combining market analysis with user and industry needs, helping ensure that proposed directions were strategically relevant and not only technologically possible." },
      { title: "Framing AI as part of a service ecosystem", desc: "AI was considered as part of a broader service experience, connected to data, workflows, decision points and customer value." }
    ],
    outputs: ["market research synthesis", "opportunity areas", "service scenarios", "value proposition concepts", "business model directions", "strategic design materials", "presentation materials for stakeholder alignment"],
    outcome: "The work helped define scalable service concepts that connected IoT and AI opportunities with user value and business strategy. It provided a structured foundation for exploring new service directions.",
    learnings: "This project reinforced the role of service design as a bridge between innovation and business value. When working with emerging technologies, the strongest opportunities often come from understanding how technology can become part of a service model."
  }
];
"""
    with open(os.path.join(data_dir, "projects.js"), "w") as f:
        f.write(projects_data)

    # 2. Update StrategicInitiatives.jsx to link ALL projects
    si_code = """
import React from 'react';
import { Link } from 'react-router-dom';

const initiatives = [
  {
    id: "clea-ecosystem",
    title: "Clea Ecosystem",
    desc: "Designing the experience foundation for SECO’s connected product ecosystem.",
    tags: ["Ecosystem Design", "Platform Strategy"],
    hasCaseStudy: true
  },
  {
    id: "clea-ai-studio",
    title: "Clea AI Studio",
    desc: "Making AI workflows accessible through a visual editor for model creation and deployment.",
    tags: ["AI Tools", "Visual Programming"],
    hasCaseStudy: true
  },
  {
    id: "app-hub",
    title: "SECO Application Hub",
    desc: "Simplifying discovery and deployment of AI applications on edge devices.",
    tags: ["Marketplace", "Edge Computing"],
    hasCaseStudy: true
  },
  {
    id: "oobe",
    title: "Out-of-the-box Experience",
    desc: "Reducing friction from first setup to product activation across touchpoints.",
    tags: ["Onboarding", "CX"],
    hasCaseStudy: true
  }
];

const StrategicInitiatives = () => (
  <section className="section" id="initiatives">
    <div className="container">
      <span className="section-label">Strategic Product Initiatives</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Orchestrating internal platforms.</h2>
      <div className="grid-2">
        {initiatives.map(item => (
          <div key={item.id} className="card">
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
            <div className="tag-list">
              {item.tags.map(t => <span key={t} className="tag">{t}</span>)}
            </div>
            {item.hasCaseStudy && <Link to={`/case-study/${item.id}`} style={{marginTop: '20px', display: 'block', color: 'var(--accent-color)', fontWeight: 600}}>Read Case Study →</Link>}
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default StrategicInitiatives;
"""
    with open(os.path.join(comp_dir, "StrategicInitiatives.jsx"), "w") as f:
        f.write(si_code)

    # 3. Update ClientProjects.jsx to link ALL projects
    cp_code = """
import React from 'react';
import { Link } from 'react-router-dom';

const projects = [
  {
    id: "daikin",
    client: "Daikin Applied Europe",
    title: "Professional HVAC Workflows",
    desc: "Embedded HMI and companion app for mission-critical environmental control.",
    hasCaseStudy: true
  },
  {
    id: "quanta",
    client: "Quanta Systems",
    title: "Strategic Service Design",
    desc: "Transitioning to AI-driven services in medical and aesthetic applications.",
    hasCaseStudy: true
  },
  {
    id: "snam",
    client: "SNAM",
    title: "Methane Detection Systems",
    desc: "Operational applications for industrial leak prevention.",
    hasCaseStudy: true
  },
  {
    id: "fastweb",
    client: "Fastweb",
    title: "Infrastructure Monitoring",
    desc: "Monitoring and alerting tools for distributed telecom infrastructure.",
    hasCaseStudy: true
  },
  {
    id: "riello",
    client: "Riello UPS",
    title: "Application Migration",
    desc: "Migrating and redesigning custom applications within Clea Portal.",
    hasCaseStudy: true
  }
];

const ClientProjects = () => (
  <section className="section" id="projects">
    <div className="container">
      <span className="section-label">Client Projects</span>
      <h2 style={{fontSize: '3rem', marginBottom: '60px'}}>Industry-defining solutions.</h2>
      <div className="grid-3">
        {projects.map(p => (
          <div key={p.id} className="card" style={{padding: '30px'}}>
            <span style={{fontSize: '0.7rem', color: 'var(--accent-color)'}}>{p.client}</span>
            <h3 style={{fontSize: '1.2rem', marginTop: '10px'}}>{p.title}</h3>
            <p style={{fontSize: '0.85rem'}}>{p.desc}</p>
            {p.hasCaseStudy && <Link to={`/case-study/${p.id}`} style={{marginTop: '15px', display: 'block', color: 'var(--accent-color)', fontSize: '0.8rem', fontWeight: 600}}>Case Study →</Link>}
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default ClientProjects;
"""
    with open(os.path.join(comp_dir, "ClientProjects.jsx"), "w") as f:
        f.write(cp_code)

    print("All 9 case studies integrated and Home Page links activated successfully!")

if __name__ == "__main__":
    update_all_data()
