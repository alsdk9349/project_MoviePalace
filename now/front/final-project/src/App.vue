<template>
  <header>
    <div class="bgc">
  </div>
      <nav class='navbox d-flex'>
        <RouterLink class="link" :to="{name : 'recommend'}">영화추천</RouterLink> 
        <RouterLink class="link" :to="{name : 'community'}">소통창구</RouterLink>
        <RouterLink :to="{name : 'home'}">

            
            <img src="@/assets/logo.png" alt="" class="img">
        </RouterLink> 
        <RouterLink class="link" :to="{name : 'search'}">영화검색</RouterLink> 
        <RouterLink class="link" :to="{name : 'chat'}">길라잡이</RouterLink>
      </nav>

  </header>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.bgc{
  position : fixed;
  top :0;
  left : 40vw;
  background-color: white;
  z-index: -1;
  width:10rem;
  height: 7rem;
}
.navbox {
  display: flex;
  width: 100%;
  height: 5rem;
  /* background: linear-gradient( #cff09e, #79bd9a); */
  background-color : rgb(0, 70, 42);
  justify-content: space-around;
  z-index: -1;
}
.link {
  margin: 10px;
  color : white;
  font-style:italic;
  font-weight: bold;
  text-decoration-line: none;
  background-color : rgb(0, 70, 42);
  /* background-color:#a8dba8 ; */
  width: 15vw;
  margin-top: 2rem;
}
.img{
  width:10rem;
  height:7rem;
  border: 5px solid black;
  background-color: white;
  /* opacity: 100%; */
}

</style>
