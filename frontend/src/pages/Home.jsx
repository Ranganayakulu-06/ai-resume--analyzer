import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="home-page">
      <div className="hero">
        <h1>AI Resume Analyzer</h1>
        <p>Improve your resume and increase your chances of passing ATS</p>
        <Link to="/dashboard" className="cta-button">
          Get Started
        </Link>
      </div>
      <section className="features">
        <h2>Features</h2>
        <div className="features-grid">
          <div className="feature">
            <h3>📄 Resume Analysis</h3>
            <p>Upload your resume and get detailed analysis</p>
          </div>
          <div className="feature">
            <h3>🎯 ATS Compatibility</h3>
            <p>Check how well your resume passes ATS systems</p>
          </div>
          <div className="feature">
            <h3>💡 Smart Suggestions</h3>
            <p>Get actionable recommendations to improve your resume</p>
          </div>
        </div>
      </section>
    </div>
  )
}
