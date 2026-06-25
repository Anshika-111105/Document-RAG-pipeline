"""Main React component."""
import React, { useState } from 'react'
import UploadBox from './components/UploadBox'
import ChatWindow from './components/ChatWindow'
import './App.css'

function App() {
  const [documents, setDocuments] = useState([])
  const [messages, setMessages] = useState([])

  return (
    <div className="app">
      <header className="header">
        <h1>Document RAG Pipeline</h1>
        <p>Upload documents and ask questions</p>
      </header>

      <div className="container">
        <aside className="sidebar">
          <UploadBox onUpload={(doc) => setDocuments([...documents, doc])} />
          <div className="documents-list">
            <h3>Documents ({documents.length})</h3>
            <ul>
              {documents.map((doc) => (
                <li key={doc.id}>{doc.filename}</li>
              ))}
            </ul>
          </div>
        </aside>

        <main className="main">
          <ChatWindow messages={messages} onMessage={(msg) => setMessages([...messages, msg])} />
        </main>
      </div>
    </div>
  )
}

export default App
