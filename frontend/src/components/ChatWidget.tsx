import { useState } from "react";
import { askAI } from "../services/api";

interface Message {
  role: "user" | "ai";
  text: string;
}

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", text: input };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await askAI(input);

      const aiMessage = { role: "ai", text: res.answer };
      setMessages(prev => [...prev, aiMessage]);
    } catch {
      setMessages(prev => [
        ...prev,
        { role: "ai", text: "Something went wrong." }
      ])
    }

    setLoading(false)
  };

  return (
    <div>
      {/* Button to open chat widget */}
      <button
        onClick={() => setOpen(!open)}
        className="fixed bottom-20 right-6 w-80 h-96 bg-black border border-gray-700 rounded-lg flex flex-col"
      >
        Ask AI
      </button>

      {open && (
        <div className="fixed bottom-20 right-6 w-80 h-96 bg-black border border-gray-700 rounded-lg flex flex-col">
          <div className="p-3 border-b border-gray-700 font-semibold">AI Resume Assistant</div>

          <div className="flex-1 overflow-y-auto p-3 space-y-3">
            {messages.map((m, i) => (
              <div
                key={i}
                className={
                  m.role === "user"
                    ? "text-right text-blue-300"
                    : "text-left text-green-300"
                }
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
          <div className="text-right">
            <button
              onClick={() => setOpen(false)}
              className="text-sm mt-0.5 p-1 rounded-b-md bg-gray-700 text-gray-400 hover:text-white"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
