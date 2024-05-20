import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import { createMovieComment } from '@/apis/commentApi'

export const useCounterStore = defineStore('counter', () => {
  const comments = ref([])

  const addComment = (movieId, newComment) => {
    return createMovieComment(movieId, newComment)
    .then((response) => {
      if (response.status === 201){
        comments.value.push(response.data)
      }
    }).catch((error) => {
      console.log(error)
      throw error
    })

  }

  return {comments, addComment}
})

