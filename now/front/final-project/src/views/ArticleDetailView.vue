
<template>
  <main>
    <h1>ArticleDetail</h1>
    <img class="img" :src=imgUrl alt="X">
    <p class="font">title:{{ movie.title }}</p>
    <p class="font">adult:{{ movie.adult }}</p>
    <p class="font">genre:
      <span v-for="genre in movie.genres">{{ genre.name }},</span>
    </p>
    <p class="font">overview:{{ movie.overview }}</p>
    <p class="font">poster:{{ movie.poster_path }}</p>
    <p class="font">runtime:{{ movie.runtime }}</p>
    <p class="font">release_date:{{ movie.release_date }}</p>
    <p class="font">video:{{ movie.video }}</p>
    <p class="font">vote:{{ movie.vote_average }}</p>
    <RouterLink :to="moviecommunity"><button>커뮤니티</button></RouterLink>
    
  </main>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'
import axios from 'axios'
import { ref } from 'vue'
const route = useRoute()
const movieId = route.params.movieId
const API_KEY = 'f4df733efebe407d57d6b27c0bb68169'



const movie = ref([])
const imgUrl = ref("https://image.tmdb.org/t/p/original") 
axios({
  method : 'GET',
  url : 'https://api.themoviedb.org/3/movie/' + movieId,
  params : {language : 'ko-KR', api_key : API_KEY},
  headers : {
    accept : 'applictaion/json'
  }
}).then((response) => {
  movie.value = response.data
  imgUrl.value += movie.value.poster_path
})
.catch((error) => {
  console.log(error)
})

</script>

<style scoped>
.font{
  color : white;
}
.img {
  width : 20rem;
  height : 30rem;
}
</style>