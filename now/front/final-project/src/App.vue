<template>
  <header>
    <div class="wrapper">
      <nav class='navbox'>
        <RouterLink class="" :to="{name : 'home'}">
          <img src="@/assets/logo.jpg" alt="" class="img">
        </RouterLink> 
        <RouterLink class="link" :to="{name : 'recommend'}">영화추천</RouterLink> 
        <RouterLink class="link" :to="{name : 'search'}">영화검색</RouterLink> 
        <RouterLink class="link" :to="{name : 'community'}">커뮤니티</RouterLink>
      </nav>
    </div>
  </header>
  <h1> <br></h1>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

.navbox {

  display: flex;
  width: 100vw;
  height: 3rem;
  background-color: rgb(157,212,173);
}
.link {
  margin: 1rem;
  color : darkslategray;
  font-style:italic;
  font-weight: bold;
  text-decoration-line: none;
  background-color: rgb(157,212,173);
}
.img{
  width:8rem;
  height:6rem;
  border: 5px solid black;
}
</style>
