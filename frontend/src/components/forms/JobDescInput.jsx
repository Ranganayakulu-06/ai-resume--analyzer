import { useState } from 'react'

export default function JobDescInput({ onSubmit }) {
  const [jobDesc, setJobDesc] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (jobDesc.trim()) {
      onSubmit(jobDesc)
      setJobDesc('')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="job-desc-form">
      <div className="form-group">
        <label htmlFor="job-description">Job Description</label>
        <textarea
          id="job-description"
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          placeholder="Paste the job description here..."
          rows="8"
          required
        />
      </div>
      <button type="submit">Analyze Resume</button>
    </form>
  )
}
