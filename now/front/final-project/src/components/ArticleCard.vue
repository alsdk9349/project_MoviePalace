`<template>
  <div class="d-flex justify-content-center" @click = "goDetail(movie.id)">

    <div class="d-flex align-items-center justify-content-between">
      <div class="ticket d-flex align-items-center" style="width: 1200px">
        <img class="img" :src="`https://image.tmdb.org/t/p/original/${prop.movie.poster_path}`" alt="X">
        <div class="col-md-6 offset-md-1" style="margin: 0; width:750px">
          <h2>영화 관람권</h2>
          <p>{{ movie.title }}</p>
          <p>{{ movie.released_date }}</p>
        </div>
        <!-- <div class="barcode-container justify-content-center align-items-center" >
          <img :src="qrcode" alt="X" style="max-width: 100%; height: 40%; display: block; margin: auto;">
        </div> -->
        <div class="barcode-container col-md-3 offset-md-10" style="margin: 0; width:200px;">
          <img :src="barcode" class="d-block" alt="X" style="margin: 0; width: 100%;">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import barcode from '@/assets/Barcode.jpg'
import qrcode from '@/assets/QRcode.png'
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

.barcode-container {
  /* background-color: green; */
  margin: 0;
  width : 90%;
  height: 90%;
  background-color: lightgoldenrodyellow;
  display: flex;
  justify-content: center;
  text-align: center;
}

.borderst{
  display: flex;
  background-color: white;
  justify-content: center;
  width: 15vw;
  height: 20rem;
  border : 2px solid white; 
  text-align: center;
}
</style>