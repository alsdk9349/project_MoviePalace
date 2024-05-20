`<template>
  <div class="d-flex justify-content-center" @click = "goDetail(movie.id)">

    <div class="d-flex align-items-center justify-content-between">
      <div class="ticket d-flex align-items-center justify-content-between">
        <img class="img" :src="`https://image.tmdb.org/t/p/original/${prop.movie.poster_path}`" alt="X">
        <div>
          <h2>영화 관람권</h2>
          <p>{{ movie.title }}</p>
          <p>{{ movie.released_date }}</p>
        </div>
      </div>
      <div class="borderst">
        <div class="barcode">
          바코드
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'
const prop = defineProps({
  movie:Object
})

const router = useRouter()

function goDetail(movieId){
  router.push({name : 'detail', params : {'movieId':movieId}})
}

</script>

<style scoped>
.ticket {
  color : black;

  border : 2px solid lightgoldenrodyellow;
  background-color: lightgoldenrodyellow;
  width: 80vw;
  height: 20rem;
  margin-top: 2rem;
  margin-bottom : 2rem;
}

.img{
  margin : 1rem;
  width: 13rem;
  height: 18rem;
}

.barcode{
  /* background-color: green; */
  margin: 1rem;
  width : 90%;
  height: 90%;
}

.borderst{
  display: flex;
  background-color: white;
  justify-content: center;
  width: 15vw;
  height: 20rem;
 
  border : 2px solid white; 
}
</style>