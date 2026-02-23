import { useState } from "react";
import { askAI } from "../services/api";

interface Message {
  role: "user" | "ai";
  text: string;
}

const suggestedQuestions = [
  "What backend technologies does Rohit use?",
  "Tell me about Rohit's projects",
  "Explain the architecture of Rohit's Car Rental Platform",
  "What experience does Rohit have?"
]

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user" as const, text: input };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await askAI(input);

      const aiMessage = { role: "ai" as const, text: res.answer };
      setMessages((prev) => [...prev, aiMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "ai", text: "Something went wrong." },
      ]);
    }

    setLoading(false);
  };

  return (
    <div>
      {/* Button to open chat widget */}
      <button
        onClick={() => setOpen(!open)}
        className="fixed bottom-6 right-6 bg-white text-black px-4 py-2 rounded-full shadow-lg hover:bg-gray-100"
      >
        Ask AI
      </button>

      {open && (
        <div className="fixed bottom-20 right-6 w-80 h-96 bg-black border border-gray-700 rounded-lg flex flex-col">
          <div className="p-3 border-b border-gray-700 font-semibold">
            AI Resume Assistant
          </div>

          <div className="flex-1 overflow-y-auto p-3 space-y-3">
            {messages.length === 0 && (
              <div className="space-y-2">
                <p className="text-sm text-gray-400">Try asking:</p>

                {suggestedQuestions.map((q, i) => (
                  <button
                    key={i}
                    onClick={() => setInput(q)}
                    className="block text-left text-sm border border-gray-700 px-3 py-2 rounded hover:border-gray-500 w-full"
                  >
                    {q}
                  </button>
                ))}
              </div>
            )}
            {messages.map((m, i) => (
              <div
                key={i}
                className={`max-w-[80%] p-2 rounded text-sm ${
                  m.role === "user"
                    ? "ml-auto bg-white text-black"
                    : "bg-gray-800 text-gray-200"
                }`}
              >
                {m.text}
              </div>
            ))}
            {loading && (
              <div className="text-gray-500 text-sm">AI is thinking...</div>
            )}
          </div>
          <div className="p-3 border-t border-gray-700 flex gap-2">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") sendMessage();
              }}
              placeholder="Ask something..."
              className="flex-1 bg-gray-900 p-2 rounded text-sm outline-none"
            />
            <button
              onClick={sendMessage}
              className="bg-white text-black px-3 rounded"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
