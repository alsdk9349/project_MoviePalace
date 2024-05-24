<template>
  <main>
    <div class="title">
      <h1 class="dokdo-regular">소통 창구</h1>
    </div>
    <ArticleCard class="pointer" v-for="movie in movies" :movie="movie" :key="movie.pk"/>
    <nav class="pagination" aria-label="Page navigation example">
      <ul class="pagination">
        <li class="page-shift page-link" @click="start()">처음으로</li>
        <li class="page-btn page-link" @click="minus()">이전</li>
          <li v-for="num in 10" class="page-item page-link" @click="pageChange(num + pageValue)">{{num + pageValue}}</li>
        <li class="page-btn page-link" @click="plus()">다음</li>
        <li class="page-shift page-link" @click="end()">끝으로</li>
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
function start(){
  pageValue.value = 0 
}
function end(){
    pageValue.value = 460
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
.title {
  text-align: center; 
  margin-top: 30px; 
  margin-left: 100px;
  margin-right: 100px;
  color: white; 
  background-color: white;
}
.pagination{
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: white;
}
.page-item{
  color: ivory;
  font-weight: bold;
  background-color: #afb3af;
}
.pagination .page-item{
  cursor: pointer;
}
.pointer{
  cursor: pointer;
  margin-top: 2rem;
  margin-bottom: 2rem;
}
.page-btn{
  cursor: pointer;
  color: ivory;
  font-weight: bold;
  background-color:#464d49a6;

}
.page-shift{
  cursor: pointer;
  color: ivory;
  font-weight: bold;
  background-color:  #29322d77;
}
.dokdo-regular {
  font-family: "Dokdo", system-ui;
  font-weight: 400;
  font-style: normal;
  font-size:10vh;
  color: #3f4040;
}

</style>