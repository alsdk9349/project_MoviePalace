
<template>
  <main>
    <h1>ArticleDetail</h1>
    <div class="d-flex" style="border: solid black 5px; margin:20px">
      <img class="img" :src=imgUrl alt="X">
      <div>
        <h1 class="font">제목 : {{ movie.title }}</h1>
        <p class="font">장르 : 
          <span v-for="genre, index in movie.genres"><span v-if="index!== 0">, </span>{{ genre.name }}</span>
        </p>
        <p class="font">개요 : {{ movie.overview }}</p>
        <p class="font">상영시간 : {{ movie.runtime }}분</p>
        <p class="font">개봉일 : {{ movie.release_date }}</p>
        <p class="font">평점 : {{ movie.vote_average }}</p>
        <RouterLink class="linkst" :to="{name : 'moviecommunity', params : {'movieId' : movie.id}, query : {'title': movie.title, 'poster_path':movie.poster_path}}">커뮤니티</RouterLink>
      </div>
    </div>

    <RouterView />
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
  color : black;
  font-weight: bold;
}
.img {
  width : 20rem;
  height : 30rem;
  margin-right: 1rem;
}
.linkst{
  text-decoration: none;
  color : white;
  background-color: olivedrab;
  padding : 0.3rem;

  border : 3px solid olivedrab;
}
</style>