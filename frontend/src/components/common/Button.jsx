export default function Button({
  text,
  onClick,
  disabled = false,
  className = '',
  type = 'button',
}) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`btn ${className}`}
    >
      {text}
    </button>
  )
}
