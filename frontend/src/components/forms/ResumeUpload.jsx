import { useState } from 'react'

export default function ResumeUpload({ onUpload }) {
  const [file, setFile] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (file) {
      onUpload(file)
      setFile(null)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="resume-upload-form">
      <div className="form-group">
        <label htmlFor="resume">Upload Resume (PDF or DOCX)</label>
        <input
          id="resume"
          type="file"
          accept=".pdf,.docx"
          onChange={handleFileChange}
          required
        />
      </div>
      <button type="submit" disabled={!file}>
        Upload Resume
      </button>
    </form>
  )
}
