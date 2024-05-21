<template>
  <div class="cardst" @click="goDetail()">
    <img class="img" :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" alt="X">
    <p>{{ props.movie.title }}</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
  movie:Object
})
const router = useRouter()
const goDetail = function(){
  router.push({name : 'detail', params : {'movieId' : props.movie.id} })
}
</script>

<style scoped>
.img {
  width : 10rem;
  height: 17rem;
}
.cardst {
  border : 2px solid white;
}
</style>