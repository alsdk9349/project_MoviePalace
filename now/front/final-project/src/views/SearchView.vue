<template>
  <main>
    <h1>search</h1>
    <input type="text" v-model="searchWord">
    <button @click="searching">검색</button>
    <!-- 밑에 search된 카드 components 띄우기 -->
    <SearchedCard />
  </main>
</template>

<script setup>
import axios from 'axios'
import {ref} from 'vue'
import SearchedCard from '@/components/SearchedCard.vue';
const searchWord = ref("")
const searchMovie = ref([])
const searching = function(){

  axios ({
    method : 'GET',
    url : `http://127.0.0.1:8000/movies/search/${searchWord.value}`
  }).then((response) =>{
    console.log(response.data)
    searchMovie.value = response.data
  }).catch((error) => {
    console.log(error)
  })


}

</script>

<style scoped>

</style>