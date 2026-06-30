import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const api = axios.create({
  baseURL: API_URL,
  timeout: import.meta.env.VITE_API_TIMEOUT || 30000,
})

export const analyzeResume = async (resumeFile, jobDescriptionId) => {
  const formData = new FormData()
  formData.append('resume_file', resumeFile)
  formData.append('job_description_id', jobDescriptionId)

  const response = await api.post('/api/v1/analysis/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return response.data
}

export const getAnalysis = async (analysisId) => {
  const response = await api.get(`/api/v1/analysis/${analysisId}`)
  return response.data
}

export default api
