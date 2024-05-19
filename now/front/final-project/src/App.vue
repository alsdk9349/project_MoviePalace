<template>
  <header>
    <div class="wrapper">
      <nav class='navbox'>
        <RouterLink class="link" :to="{name : 'home'}">logo</RouterLink> 
        <RouterLink class="link" :to="{name : 'recommend'}">영화추천</RouterLink> 
        <RouterLink class="link" :to="{name : 'search'}">영화검색</RouterLink> 
        <RouterLink class="link" :to="{name : 'community'}">커뮤니티</RouterLink>
      </nav>
    </div>
  </header>
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
  background-color: rgb(44, 44, 44);
}
.link {
  margin: 1rem;
  color : white;
  text-decoration-line: none;
  background-color: rgb(44, 44, 44);
}

</style>
