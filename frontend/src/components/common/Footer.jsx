export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="footer">
      <p>&copy; {currentYear} AI Resume Analyzer. All rights reserved.</p>
    </footer>
  )
}
