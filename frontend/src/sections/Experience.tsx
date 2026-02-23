import type { Experience } from "../types/resume"
import SectionTitle from "../components/SectionTitle"

interface Props {
  experience: Experience[]
}

export default function ExperienceSection({ experience }: Props) {

  return (
    <section className="max-w-5xl mx-auto py-20 px-6">

      <SectionTitle title="Experience" />

      <div className="space-y-8">

        {experience.map(exp => (

          <div
            key={exp.id}
            className="border border-white/10 p-5 rounded-lg bg-white/5"
          >

            <h3 className="text-lg font-semibold">
              {exp.role}
            </h3>

            <p className="text-gray-400 mb-2">
              {exp.company}
            </p>

            <p className="text-gray-300 text-sm">
              {exp.description}
            </p>

          </div>

        ))}

      </div>

    </section>
  )
}