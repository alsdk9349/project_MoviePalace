<template>
  <div>
    {{ movie.title }}
    <img class="img" :src=imgUrl alt="X">
  </div>
  
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref} from 'vue'

const movie = ref({})
const route = useRoute()
movie.value = {
  'title': route.query.title,
  'poster_path' : route.query.poster_path
}
const imgUrl = "https://image.tmdb.org/t/p/original" + movie.value.poster_path

</script>
<style scoped>

*{
  color : white
}
.img {
  width : 20rem;
  height: 30rem;
}
</style>