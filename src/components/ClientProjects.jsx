import { projects } from '../data/projects';
import HorizontalProjects from './HorizontalProjects';

const ClientProjects = () => {
  const clientIds = ["daikin", "quanta", "snam", "fastweb", "riello", "rhea", "ciam", "zoppas"];
  const filteredProjects = projects.filter(p => clientIds.includes(p.id));

  return <HorizontalProjects
    id="projects"
    label="Client Projects"
    title="Industry-defining solutions."
    intro="From embedded control to industrial operations, these projects translate specialist workflows, technical requirements and service opportunities into experiences people can trust."
    items={filteredProjects}
    eyebrow={item => item.metadata.client}
  />;
};

export default ClientProjects;
