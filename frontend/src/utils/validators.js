export const isValidEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return re.test(email)
}

export const isValidFileSize = (file, maxSize) => {
  return file.size <= maxSize
}

export const isValidFileType = (file, allowedTypes) => {
  return allowedTypes.includes(file.type)
}
