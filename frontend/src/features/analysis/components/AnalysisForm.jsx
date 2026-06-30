import ResumeUpload from '../../../components/forms/ResumeUpload'
import JobDescInput from '../../../components/forms/JobDescInput'

export default function AnalysisForm({ onSubmit, loading }) {
  return (
    <form className="analysis-form">
      <div className="form-section">
        <ResumeUpload onUpload={(file) => console.log(file)} />
      </div>
      <div className="form-section">
        <JobDescInput onSubmit={(desc) => console.log(desc)} />
      </div>
    </form>
  )
}
