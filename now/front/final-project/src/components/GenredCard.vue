<template>
  <div>
    <div class="cardst">
      <img class="img" :src=imgUrl alt="X">
      <p>{{ movie.title }}
</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  movie : Object,
})
const imgUrl = "https://image.tmdb.org/t/p/original" + props.movie.poster_path

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