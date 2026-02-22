const API_BASE = "http://127.0.0.1:8000/api"

export async function fetchResume() {
  const res = await fetch(`${API_BASE}/resume`)
  return res.json()
}

export async function askAI(question: string) {
  const res = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  })

  return res.json()
}