import { projects } from '../data/projects';
import HorizontalProjects from './HorizontalProjects';

const StrategicInitiatives = () => {
  // Filter the specific strategic projects
  const initiativesIds = ["clea-ecosystem", "clea-ai-studio", "app-hub", "oobe", "dev-center"];
  const filteredInitiatives = projects.filter(p => initiativesIds.includes(p.id));

  return <HorizontalProjects
    id="initiatives"
    label="Strategic Initiatives"
    title="Orchestrating internal platforms."
    intro="Platform initiatives that connect SECO’s software, hardware and AI offering into clearer product and service value that customers can adopt and the business can scale."
    items={filteredInitiatives}
    eyebrow={item => item.metadata.context}
  />;
};

export default StrategicInitiatives;
