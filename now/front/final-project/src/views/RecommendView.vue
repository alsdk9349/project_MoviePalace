<template>
  <main>
    <div class="wrapst">

      <h1>현재 상영중</h1>
      <div>
        <div class="row row-cols-lg-4 row-cols-md-3 row-cols-sm-2 justify-content-center justify-content-md-around" >
          <NowPlayingCard class="col" v-for="movie in movies" :key="movie.id" :movie="movie"/>
        </div>
      </div>
      <br>
      <br>
      <h1>장르별 추천</h1>
      <!-- <label for="selectedGenre" class="form-label"></label> -->
      <select class="form-select selectbox" aria-label="Default select example" v-model="selectedGenre">
        <option disabled value="">장르를 선택하세요.</option>
        <option class="option" value="80">범죄</option>
        <option class="option" value="35">코미디</option>
        <option class="option" value="12">모험</option>
        <option class="option" value="28">액션</option>
        <option class="option" value="878">SF</option>
        <option class="option" value="16">애니메이션</option>
        <option class="option" value="10751">가족</option>
        <option class="option" value="18">드라마</option>
        <option class="option" value="10749">로맨스</option>
        <option class="option" value="9648">미스터리</option>
        <option class="option" value="14">판타지</option>
        <option class="option" value="53">스릴러</option>
        <option class="option" value="10752">전쟁</option>
        <option class="option" value="10402">음악</option>
        <option class="option" value="37">서부</option>
        <option class="option" value="10770">TV영화</option>
        <option class="option" value="27">공포</option>
        <option class="option" value="36">역사</option>
        <!-- <option class="option" value="99">다큐멘터리</option> -->
      </select>
      <br>
      <div class="row row-cols-lg-4 row-cols-md-3 row-cols-sm-2 justify-content-center justify-content-md-around" >          
        <GenredCard class="col" v-for="genremovie in genred" :key="genremovie.pk" :movie="genremovie"/> 
      </div>
    </div>
      
    </main>
  </template>

<script setup>

import NowPlayingCard from '@/components/NowPlayingCard.vue'
import GenredCard from '@/components/GenredCard.vue'
import { onUpdated } from 'vue'
import axios from 'axios'
import {ref, watch} from 'vue'

const movies = ref([])
axios({
  method : 'get', 
  url : `http://127.0.0.1:8000/movies/recommend`,
  
}).then((response) => {
  movies.value = response.data
})
.catch((error) => {
  console.log(error)
})

const selectedGenre = ref('')

const genred = ref([])
watch(selectedGenre, (newselectedGenre)=>{

  selectedGenre.value = newselectedGenre
  axios({
    method : 'get', 
    url : `http://127.0.0.1:8000/movies/recommend/genred/${selectedGenre.value}`,
    
  }).then((response) => {
    genred.value = response.data
    console.log(genred.value)
  })
  .catch((error) => {
    console.log(error)
  })
})

</script>

<style scoped>
.option{
  color:black;
}
.h1 {
  color:white;
  margin-bottom: 30px;
}
.selectbox {
  margin-top: 3rem;
  width: 80vw;
  padding:0.5rem;
  padding-left: 1rem;
}
.wrapst {
  text-align: center;
  color:white;
  padding : 3rem;
  display: flex;
  flex-direction: column;
}

.wrapst > select {
  align-self: center;
}
</style>
