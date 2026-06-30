import { useEffect, useState } from 'react'
import AnalysisHistory from '../components/AnalysisHistory'

export default function HistoryPage() {
  const [history, setHistory] = useState([])

  useEffect(() => {
    // TODO: Fetch history from API
  }, [])

  return (
    <div className="history-page">
      <h1>Analysis History</h1>
      <AnalysisHistory data={history} />
    </div>
  )
}
