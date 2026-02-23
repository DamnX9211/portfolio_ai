export default function Contact() {

  return (

    <section className="max-w-4xl mx-auto py-20 px-6 text-center">

      <h2 className="text-3xl font-semibold mb-6">
        Get In Touch
      </h2>

      <p className="text-gray-400 mb-6">
        If you'd like to work together or ask something, feel free to reach out.
      </p>

      <div className="flex justify-center gap-6">

        <a
          href="mailto:rohitkuumar1995@gmail.com"
          className="border border-white/20 px-4 py-2 rounded hover:border-white"
        >
          Email
        </a>

        <a
          href="https://github.com/DamnX9211"
          className="border border-white/20 px-4 py-2 rounded hover:border-white"
        >
          GitHub
        </a>

        <a
          href="https://linkedin.com"
          className="border border-white/20 px-4 py-2 rounded hover:border-white"
        >
          LinkedIn
        </a>
        <a
          href="/resume.pdf"
          className="border border-white/20 px-4 py-2 rounded hover:border-white"
        >
          Download Resume
        </a>

      </div>

    </section>

  )
}