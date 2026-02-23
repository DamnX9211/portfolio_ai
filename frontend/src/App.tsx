import { useState, useEffect } from 'react'
import { fetchResume } from './services/api'
import type { ResumeData } from './types/resume'

import Hero from './sections/Hero'
import Projects from './sections/Projects'
import ChatWidget from './components/ChatWidget'
import Skills from './sections/Skills'
import Experience from './sections/Experience'
import Contact from './sections/Contact'


function App() {
  const [data, setData] = useState<ResumeData | null>(null)

  useEffect(() => {
    let mounted = true
    fetchResume().then(data => {
      if(!mounted) return
      setData(data)
    }).catch(err => {
      console.error(err)
    })
  
    return () => {
      mounted = false
    }
  }, [])

  if(!data) {
    return (
      <div className="flex items-center justify-center h-screen">
        Loading Portfolio...
      </div>
    )
  }

  return (
   <div>
    {data?.about && <Hero about={data.about} />}
    {data?.projects && <Projects projects={data.projects} />}
    {data?.skills && <Skills skills={data.skills} />}
    {data?.experience && <Experience experience={data.experience} />}
    <Contact />             
    <ChatWidget />
   </div>
  )
}

export default App
