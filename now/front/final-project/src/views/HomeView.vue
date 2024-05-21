<template>
  <main>
    <div class="video-container">
      <div class="video-background">
        <video autoplay muted loop>
          <source src="@/assets/film.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="carousel-container">
        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner d-flex justify-content-h4">
            <span>
              <div class="carousel-item" :class="{ active: currentSlideIndex === index }" v-for="(image, index) in images" :key="index">
                <img :src="image" class="d-block img" :alt="'Slide ' + (index + 1)">
              </div>
            </span>
            <span>
              <div class="carousel-item" :class="{ active: currentSlideIndex2 === index }" v-for="(image, index) in images" :key="index">
                <img :src="image" class="d-block img" :alt="'Slide ' + (index + 1)">
              </div>
            </span>
            <span>
              <div class="carousel-item" :class="{ active: currentSlideIndex3 === index }" v-for="(image, index) in images" :key="index">
                <img :src="image" class="d-block img" :alt="'Slide ' + (index + 1)">
              </div>
            </span>
            <span>
              <div class="carousel-item" :class="{ active: currentSlideIndex4 === index }" v-for="(image, index) in images" :key="index">
                <img :src="image" class="d-block img" :alt="'Slide ' + (index + 1)">
              </div>
            </span>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import poster1 from '@/assets/poster1.jpg'
import poster2 from '@/assets/poster2.jpg'
import poster3 from '@/assets/poster3.jpg'
import poster4 from '@/assets/poster4.jpg'
import poster5 from '@/assets/poster5.jpg'
import poster6 from '@/assets/poster6.jpg'
import poster7 from '@/assets/poster7.jpg'
import poster8 from '@/assets/poster8.jpg'
import poster9 from '@/assets/poster9.jpg'
import poster10 from '@/assets/poster10.jpg'
import poster11 from '@/assets/poster11.jpg'
import poster12 from '@/assets/poster12.jpg'
import poster13 from '@/assets/poster13.jpg'
import poster14 from '@/assets/poster14.jpg'
import poster15 from '@/assets/poster15.jpg'
import poster16 from '@/assets/poster16.jpg'

import { ref, onMounted } from 'vue';
const images = [poster1,poster2,poster3,poster4,poster5,poster6,poster7,poster8,poster9,poster10,poster11,poster12,poster13,poster14,poster15,poster16];
const totalSlides = images.length;
const intervalTime = 1000; // 5초마다 슬라이드 변경
const currentSlideIndex = ref(0);
const currentSlideIndex2 = ref(1);
const currentSlideIndex3 = ref(2);
const currentSlideIndex4 = ref(3);

const changeSlide = () => {
  currentSlideIndex.value = (currentSlideIndex.value + 1) % totalSlides;
};

const changeSlide2 = () => {
  currentSlideIndex2.value = (currentSlideIndex.value + 1) % totalSlides;
};

const changeSlide3 = () => {
  currentSlideIndex3.value = (currentSlideIndex2.value + 1) % totalSlides;
};

const changeSlide4 = () => {
  currentSlideIndex4.value = (currentSlideIndex3.value + 1) % totalSlides;
};

onMounted(() => {
  setInterval(changeSlide, intervalTime);
  setInterval(changeSlide2, intervalTime);
  setInterval(changeSlide3, intervalTime);
  setInterval(changeSlide4, intervalTime);
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

.carousel-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.carousel-item img {
  width: 25rem;
  height: 35rem;
  border: 25px solid black;
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
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>