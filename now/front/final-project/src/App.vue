<template>
  <header>
      <nav class='navbox d-flex'>
        <RouterLink class="link" :to="{name : 'recommend'}"><p>영화추천</p></RouterLink> 
        <RouterLink class="link" :to="{name : 'community'}"><p>소통창구</p></RouterLink>
        <RouterLink :to="{name : 'home'}">
          <img src="@/assets/logo.png" alt="" class="img">
        </RouterLink> 
        <RouterLink class="link" :to="{name : 'search'}"><p>영화검색</p></RouterLink> 
        <RouterLink class="link" :to="{name : 'chat'}"><p>길라잡이</p></RouterLink>
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
  background: linear-gradient( #cff09e, #79bd9a);
  /* background-color : rgb(157,212,173); */
  justify-content: space-around;
}
.link {
  color : darkslategray;
  text-decoration-line: none;
  background-color:#a8dba8, ;
  width: 15vw;
  margin-top: 2rem;
}
.img{
  width:10rem;
  height:7rem;
  border: 5px solid black;
}
.nanum-brush-script-regular {
  font-family: "Nanum Brush Script", cursive;
  font-weight: 400;
  font-style: normal;

}
p{
  font-family: "Kirang Haerang", system-ui;
  font-weight: 400;
  font-style:normal;
  font-size: xx-large;
}
</style>
