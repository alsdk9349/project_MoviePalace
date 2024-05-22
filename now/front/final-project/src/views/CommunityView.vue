<template>
  <main>
    <h1>Community</h1>
    <div class="container row row-cols-1 row-cols-sm-2 row-cols-md-3">
      <ArticleCard class="boxst col" v-for="movie in movies" :movie="movie" :key="movie.pk"/>
    </div>

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
.container{
  margin : 2px

}
.boxst{
  box-sizing: border-box;
  border :2px solid white;
  margin :5px;
}



</style>