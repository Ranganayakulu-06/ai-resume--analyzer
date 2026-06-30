import { useState } from 'react'

export const useAnalysis = () => {
  const [analysis, setAnalysis] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const analyzeResume = async (resumeFile, jobDescription) => {
    setLoading(true)
    setError(null)

    try {
      const result = {}
      setAnalysis(result)
      return result
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return { analysis, loading, error, analyzeResume }
}
