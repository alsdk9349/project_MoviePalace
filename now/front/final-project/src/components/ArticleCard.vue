<template>
  <div class="" @click = "goDetail(movie.id)">
    <!-- movie.id = {{ movie.id }} -->
    <div class="divfont">
      <img class="img" :src="`https://image.tmdb.org/t/p/original/${prop.movie.poster_path}`" alt="X">
      <p>{{ movie.title }}</p>
      <p class="ptag">{{ movie.overview }}</p>
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
.divfont {
  color : white;
  width : 30vw;
}
.img{
  width: 20%;
  height: 30%;
}
.ptag{
  width : 80%;
}
</style>