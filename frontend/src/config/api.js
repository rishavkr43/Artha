/**
 * Central API configuration
 * In development: uses localhost:8000
 * In production: uses VITE_API_BASE_URL env variable
 */
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const API_BASE = `${API_BASE_URL}/api`

export default API_BASE_URL
