import { useState, useEffect } from 'react'
import { fetchResume } from './services/api'
import type { ResumeData } from './types/resume'

import Hero from './sections/Hero'
import Projects from './sections/Projects'
import ChatWidget from './components/ChatWidget'


function App() {
  const [data, setData] = useState<ResumeData | null>(null)

  useEffect(() => {
    fetchResume().then(setData)
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
    <Hero about={data.about} />
    <Projects projects={data.projects} />
    <ChatWidget />
   </div>
  )
}

export default App
