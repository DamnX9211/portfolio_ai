import type { Project } from "../types/resume";
import SectionTitle from "../components/SectionTitle";

interface Props {
  projects: Project[];
}

export default function Projects({ projects }: Props) {
  return (
    <section className="max-w-5xl mx-auto py-20 px-6">
      <SectionTitle title="Projects" />
      <div className="grid grid-cols-2 md:grid-cols-2 gap-6">
        {projects.map((project) => (
          <div key={project.id} className="bg-white/5 backdrop-blur-sm border border-white/10 p-6 rounded-xl hover:border-white/30 hover:scale-[1.02] transition-transform duration-300 ease-in-out">
            <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
            <p className="text-gray-400 mb-4">{project.description}</p>
            <p className="text-sm text-gray-500">
              {project.tech_stack}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
