<template>
  <main>
    <h1>Community</h1>
    <ArticleCard v-for="movie in movies" :movie="movie" :key="movie.pk"/>
    <nav aria-label="Page navigation example">
      <ul class="pagination">
        <li class="page-item page-link" @click="minus()">Previous</li>
          <li v-for="num in 10" class="page-item page-link" @click="pageChange(num + pageValue)">{{num + pageValue}}</li>
        <li class="page-item page-link" @click="plus()">Next</li>
      </ul>
    </nav>
  </main>
</template>

<script setup>
import axios from 'axios'
import ArticleCard from '@/components/ArticleCard.vue'
import { ref } from 'vue'

const movies = ref([])
const pageNum = ref(1)
const pageValue = ref(0)

function minus(){
  if (pageValue.value > 0){
    pageValue.value -= 10}
}
function plus(){
  if(pageValue.value < 460){
    pageValue.value += 10
  }
}
function pageChange(num){
  pageNum.value = num
  console.log(pageNum.value)
  axios({
  method : 'get', 
  url : `http://127.0.0.1:8000/movies/?page=${pageNum.value}`,
  }).then((response) => {
    console.log(response.data)
    movies.value=response.data
  })
  .catch((error) => {
    console.log(error)
  })
}
axios({
  method : 'get', 
  url : `http://127.0.0.1:8000/movies/?page=1`,
  }).then((response) => {
    console.log(response.data)
    movies.value=response.data
  })
  .catch((error) => {
    console.log(error)
  })


</script>

<style scoped>

</style>