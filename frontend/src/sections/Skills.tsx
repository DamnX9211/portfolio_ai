import type { Skill } from "../types/resume"
import SectionTitle from "../components/SectionTitle"

interface Props {
  skills: Skill[]
}

export default function Skills({ skills }: Props) {

  const grouped = skills.reduce((acc: any, skill) => {
    acc[skill.category] = acc[skill.category] || []
    acc[skill.category].push(skill.name)
    return acc
  }, {})

  return (
    <section className="max-w-5xl mx-auto py-20 px-6">

      <SectionTitle title="Skills" />

      <div className="space-y-6">

        {Object.keys(grouped).map(category => (

          <div key={category}>

            <h3 className="text-lg font-semibold mb-2 text-gray-300">
              {category}
            </h3>

            <div className="flex flex-wrap gap-2">

              {grouped[category].map((skill: string) => (

                <span
                  key={skill}
                  className="px-3 py-1 bg-white/10 rounded-full text-sm"
                >
                  {skill}
                </span>

              ))}

            </div>

          </div>

        ))}

      </div>

    </section>
  )
}