"""API client for frontend."""
import axios from 'axios'

const API_BASE = '/api'

const apiClient = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const uploadDocument = async (file) => {
  const formData = new FormData()
  formData.append('file', file)
  return apiClient.post('/upload', formData)
}

export const queryDocuments = async (query, topK = 5) => {
  return apiClient.post('/query', { query, top_k: topK })
}

export const listDocuments = async () => {
  return apiClient.get('/documents')
}

export const deleteDocument = async (docId) => {
  return apiClient.delete(`/documents/${docId}`)
}

export const healthCheck = async () => {
  return apiClient.get('/health')
}

export default apiClient
