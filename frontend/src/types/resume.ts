export interface Project {
    id: string
    title: string
    description: string
    tech_stack?: string[]
    github_link?: string
    live_link?: string
}

export interface Skill {
  id: string
  name: string
  category: string
}

export interface Experience {
  id: string
  company: string
  role: string
  description: string
}

export interface ResumeData {
  about: {
    name: string
    headline: string
    summary: string
  }
  projects: Project[]
  skills: Skill[]
  experience: Experience[]
}