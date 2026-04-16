import { useState } from "react";
import { sendMessage } from "./api";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    const userMsg = { role: "user", text: input };
    setMessages([...messages, userMsg]);

    const res = await sendMessage(input);

    const botMsg = { role: "bot", text: res.reply };
    setMessages((prev) => [...prev, botMsg]);

    setInput("");
  };

  return (
    <div>
      <div>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.text}</p>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={handleSend}>
        Send
      </button>
    </div>
  );
}
