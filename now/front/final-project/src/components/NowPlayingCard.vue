<template>
    <div class="cardst">
      <div class="centerst"  @click="goDetail()">
        <h4 class="textst">{{ movie.title }}</h4>
        <img class="img" :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`" alt="X">
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
  movie : Object
})

const router = useRouter()
const goDetail = function(){
  router.push({name : 'detail', params : {'movieId' : props.movie.id} })
}
</script>

<style scoped>
.cardst {
  color:black;
  border: 2px solid white;
  width : 20rem;
  height: 30rem;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin : 1rem;
}
.centerst{
  margin : 1rem;
  display: grid;
  justify-content: center;

}
.img{
  width: 95%;
  height: 100%;
}
.textst{
  text-align: center;
  /* font; */
  background-color: rgba(157, 212, 173, 0);
}
</style>