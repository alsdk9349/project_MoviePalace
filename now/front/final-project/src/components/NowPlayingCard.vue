<template>
  <div>
    <div class="cardst">
      <img class="img" :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" alt="X">
      {{ movie.title }}
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  movie : Object
})

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