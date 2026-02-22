import type { ResumeData } from "../types/resume";

interface Props {
  about: ResumeData["about"];
}

export default function Hero({ about }: Props) {
  return (
    <section className="min-h-screen flex items-center justify-center px-6">
      <div className="max-w-3xl text-center mx-auto">
        <h1 className="text-6xl md:text-7xl font-bold mb-6 tracking-tight">
          {about.name}
        </h1>
        <p className="text-2xl text-gray-400 mb-8">{about.headline}</p>
        <p className="text-gray-300 leading-relaxed">{about.summary}</p>
        <div className="mt-10 border border-white/10 rounded-lg p-4 bg-white/5 text-sm text-gray-300">
          💬 Ask my AI assistant anything about my experience, projects, or
          skills.
        </div>
      </div>
    </section>
  );
}
