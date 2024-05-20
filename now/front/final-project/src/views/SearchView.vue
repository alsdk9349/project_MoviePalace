<template>
  <main>
    <h1>Search</h1>
    <input type="text" v-model="searchWord">
    <button @click="searching">검색</button>
    <!-- 밑에 search된 카드 components 띄우기 -->
    <span v-if="searchMovie.length"> 
    <SearchedCard v-for="movie in searchMovie" :key="movie.pk" :movie="movie"/>
    </span>
    <span v-else-if="flag && !searchMovie.length">
      <p>검색 결과가 없습니다.</p>
    </span>
  </main>
</template>

<script setup>
import axios from 'axios'
import {ref} from 'vue'
import SearchedCard from '@/components/SearchedCard.vue';
const searchWord = ref("")
const searchMovie = ref([])
let flag = false
const searching = function(){

  axios ({
    method : 'GET',
    url : `http://127.0.0.1:8000/movies/search/${searchWord.value}`
  }).then((response) =>{
    searchMovie.value = response.data
    console.log(searchMovie.value)
  }).catch((error) => {
    console.log(error)
  })
  flag = true

}

</script>

<style scoped>

</style>