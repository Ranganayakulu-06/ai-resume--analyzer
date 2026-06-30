import { useState } from 'react'
import AnalysisForm from '../components/AnalysisForm'
import AnalysisReport from '../components/AnalysisReport'

export default function AnalysisPage() {
  const [analysis, setAnalysis] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleAnalysis = async (data) => {
    setLoading(true)
    try {
      setAnalysis(data)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="analysis-page">
      <h1>Resume Analysis</h1>
      <AnalysisForm onSubmit={handleAnalysis} loading={loading} />
      {analysis && <AnalysisReport data={analysis} />}
    </div>
  )
}
