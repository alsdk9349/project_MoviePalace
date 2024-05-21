<template>
  <main>
    <div class="video-container">
      <div class="video-background">
        <video autoplay muted loop>
          <source src="@/assets/film.mp4" type="video/mp4" />
        </video>
      </div>
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item" :class="{ active: currentSlideIndex === index }" v-for="(image, index) in images" :key="index">
            <img :src="image" class="d-block w-100" :alt="'Slide ' + (index + 1)">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

import homeimg1 from '@/assets/homeimage1.jpg'
import homeimg2 from '@/assets/homeimage2.jpg'
import homeimg3 from '@/assets/homeimage3.jpg'
import homeimg4 from '@/assets/homeimage4.jpg'
import homeimg5 from '@/assets/homeimage5.png'


const images = [homeimg1, homeimg2, homeimg3, homeimg4, homeimg5];
const totalSlides = images.length;

const currentSlideIndex = ref(0);

// 자동으로 다음 슬라이드로 이동하는 기능 추가
let timer;

onMounted(() => {
  timer = setInterval(() => {
    nextSlide();
  }, 1000); // 5초마다 슬라이드 전환
});

function nextSlide() {
  currentSlideIndex.value = (currentSlideIndex.value + 1) % totalSlides;
}

// 컴포넌트가 언마운트될 때 타이머 정리
onUnmounted(() => {
  clearInterval(timer);
});
</script>

<style scoped>
.video-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  background-color: rgba(157, 212, 173, 1);
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-item img {
  height: 100vh;
  object-fit: cover;
}

.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.video-background video {
  min-width: 100%;
  min-height: 100%;
}
</style>
