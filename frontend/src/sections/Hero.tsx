import type { ResumeData } from "../types/resume";

interface Props {
    about: ResumeData["about"]
}

export default function Hero({ about }: Props) {
    return (
        <section className="min-h-screen flex items-center justify-center px-6">
            <div className="max-w-3xl text-center mx-auto">
                <h1 className="text-5xl font-bold mb-4">
                    {about.name}
                </h1>
                <p className="text-xl text-gray-400 mb-6">
                    {about.headline}
                </p>
                <p className="text-gray-300 leading-relaxed">
                    {about.summary}
                </p>
            </div>
        </section>
    )
}