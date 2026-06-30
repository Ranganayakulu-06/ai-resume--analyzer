export default function AnalysisHistory({ data }) {
  return (
    <div className="analysis-history">
      {data.length === 0 ? (
        <p>No analysis history yet.</p>
      ) : (
        <table className="history-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Job Title</th>
              <th>ATS Score</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item) => (
              <tr key={item.id}>
                <td>{new Date(item.created_at).toLocaleDateString()}</td>
                <td>{item.job_title}</td>
                <td>{item.ats_score}/100</td>
                <td>
                  <button>View</button>
                  <button>Download</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}
