"""File upload component."""
import React, { useState } from 'react'
import { uploadDocument } from '../api/client'
import '../styles/UploadBox.css'

function UploadBox({ onUpload }) {
  const [uploading, setUploading] = useState(false)
  const [error, setError] = useState(null)

  const handleFileChange = async (event) => {
    const file = event.target.files[0]
    if (!file) return

    setUploading(true)
    setError(null)

    try {
      const response = await uploadDocument(file)
      onUpload({
        id: Date.now(),
        filename: file.name,
        status: 'processing'
      })
    } catch (err) {
      setError(err.message)
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="upload-box">
      <h3>Upload Document</h3>
      <input
        type="file"
        onChange={handleFileChange}
        disabled={uploading}
        accept=".pdf,.txt,.docx"
      />
      {uploading && <p>Uploading...</p>}
      {error && <p className="error">{error}</p>}
    </div>
  )
}

export default UploadBox
