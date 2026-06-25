"""Chat window component."""
import React, { useState } from 'react'
import { queryDocuments } from '../api/client'
import '../styles/ChatWindow.css'

function ChatWindow({ messages, onMessage }) {
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSend = async () => {
    if (!input.trim()) return

    setLoading(true)
    try {
      const response = await queryDocuments(input)
      onMessage({
        type: 'user',
        content: input,
        timestamp: new Date()
      })
      onMessage({
        type: 'assistant',
        content: response.data.answer,
        sources: response.data.sources,
        timestamp: new Date()
      })
      setInput('')
    } catch (error) {
      onMessage({
        type: 'error',
        content: error.message,
        timestamp: new Date()
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-window">
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message message-${msg.type}`}>
            <p>{msg.content}</p>
            {msg.sources && (
              <div className="sources">
                {msg.sources.map((src, i) => (
                  <div key={i} className="source">
                    <strong>{src.filename}</strong> - {src.content.substring(0, 100)}...
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask a question..."
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  )
}

export default ChatWindow
