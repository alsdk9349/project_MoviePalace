<template>
  <div>
    <div class="cardst" @click="goDetail()">
      <img class="img" :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" alt="X">
      <p>{{ movie.title }}
</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  movie : Object,
})

const router = useRouter()
const goDetail = function(){
  router.push({name : 'detail', params : {'movieId' : props.movie.id} })
}

</script>


<style scoped>
.cardst {
  color:white;
  border: 2px solid white;
}
.img{
  width: 20rem;
  height: 30rem;
}
</style>