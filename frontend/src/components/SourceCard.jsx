"""Source card component."""
import React from 'react'
import '../styles/SourceCard.css'

function SourceCard({ source }) {
  return (
    <div className="source-card">
      <div className="source-header">
        <h4>{source.filename}</h4>
        <span className="score">{(source.score * 100).toFixed(1)}%</span>
      </div>
      {source.page && <p className="page">Page {source.page}</p>}
      <p className="content">{source.content.substring(0, 150)}...</p>
    </div>
  )
}

export default SourceCard
