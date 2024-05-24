<template>
  <header>
    <div class="bgc">
  </div>
    <nav class='navbox d-flex'>
      <RouterLink class="pFont link" :to="{name : 'recommend'}">영화추천</RouterLink> 
      <RouterLink class="pFont link" :to="{name : 'community'}">소통창구</RouterLink>
      <RouterLink :to="{name : 'home'}">
        <img src="@/assets/logo.png" alt="" class="img">
      </RouterLink> 
      <RouterLink class="pFont link" :to="{name : 'search'}">영화검색</RouterLink> 
      <RouterLink class="pFont link" :to="{name : 'chat'}">길라잡이</RouterLink>
    </nav>
  </header>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.navbox {
  display: flex;
  width: 100%;
  height: 5rem;
  background-color : rgb(0, 70, 42);
  justify-content: space-around;
  z-index: -1;
}
.link {
  color : darkslategray;
  text-decoration-line: none;
  background-color : rgb(0, 70, 42);
  width: 15vw;
  margin-top: 1rem;
}
.img{
  width:10rem;
  height:7rem;
  border: 5px solid black;
  background-color: white;
}
.nanum-brush-script-regular {
  font-family: "Nanum Brush Script", cursive;
  font-weight: 400;
  font-style: normal;

}
.pFont{
  font-family: "Kirang Haerang", system-ui;
  font-weight: 400;
  font-style:normal;
  font-size: xx-large;
  color: white;
}
</style>
