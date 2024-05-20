import axios from 'axios'

export const createMovieComment = (movieId, payload) => {
  const token = window.localStorage.getItem('token')

    return axios
    .post(`http://127.0.0.1:8000/movies/${movieId}/community/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}


