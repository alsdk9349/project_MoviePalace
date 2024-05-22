<template>
  <main>
    <div class="title">
      <h1 class="h1Tagst dokdo-regular">영화 검색</h1>
    </div>
    <div class="col-6 offset-3 mt-3">
      <div class="input-group mb-3 ">
        <input @keyup.enter="searching" type="text" class="form-control" placeholder="검색어를 입력하세요." aria-label="Recipient's username" aria-describedby="basic-addon2" v-model="searchWord">
        <button @click="searching" class="btn btn-success">검색</button>
      </div>  
    </div>


    <!-- 밑에 search된 카드 components 띄우기 -->
    <span v-if="searchMovie.length"> 
      <div class="pTagst">{{searchMovie.length}}개의 검색 결과가 있습니다.</div>
      <div class="row row-cols-lg-4 row-cols-md-3 row-cols-sm-2 justify-content-center justify-content-md-around">
          <SearchedCard class="col" v-for="movie in searchMovie" :key="movie.pk" :movie="movie"/>
      </div>
    </span>
    <span v-else-if="flag && !searchMovie.length">
      <div class="pTagst">검색 결과가 없습니다.</div>
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
.title {
  text-align: center; 
  margin-top: 30px; 
  margin-left: 100px;
  margin-right: 100px;
  color: white; 
  background-color: rgba(100, 100, 100, 1);
}
.pTagst{
  display: flex;
  width:80vw;
  margin-left: 10vw;
}
.dokdo-regular {
  font-family: "Dokdo", system-ui;
  font-weight: 400;
  font-style: normal;
  font-size:10vh;
  color: #3f4040;
}
</style>