<template>
  <main>
    <h1>영화 검색</h1>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input @keyup.enter="searching" type="text" class="form-control" placeholder="검색어를 입력하세요." aria-label="Recipient's username" aria-describedby="basic-addon2" v-model="searchWord">
        <button @click="searching" class="btn btn-success">검색</button>
      </div>  
    </div>


    <!-- 밑에 search된 카드 components 띄우기 -->
    <span v-if="searchMovie.length"> 
      <p>{{ searchMovie.length }}개의 검색결과가 있습니다.</p>
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