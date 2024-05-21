<template>
  <header>
    <div class="d-flex">
      <nav class='navbox'>
        <RouterLink class="link" :to="{name : 'recommend'}">영화추천</RouterLink> 
        <RouterLink class="link" :to="{name : 'community'}">소통창구</RouterLink>
        <RouterLink class="navbox" :to="{name : 'home'}">
          <img src="@/assets/logo.jpg" alt="" class="img">
        </RouterLink> 
        <RouterLink class="link" :to="{name : 'search'}">영화검색</RouterLink> 
        <RouterLink class="link" :to="{name : 'chat'}">채팅</RouterLink>
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
  width: 100%;
  height: 2rem;
  background-color: rgb(157,212,173);
  justify-content: space-around;
  padding-left: 150px;
  padding-right: 150px;
}
.link {
  margin: 10px;
  color : darkslategray;
  font-style:italic;
  font-weight: bold;
  text-decoration-line: none;
  background-color: rgb(157,212,173);
  width: 300px;
  padding: 30px;
}
.img{
  width:10rem;
  height:7rem;
  border: 5px solid black;
}
</style>
