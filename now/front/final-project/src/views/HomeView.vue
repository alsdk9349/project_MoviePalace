<template>
  <main>
    <div class="video-container">
      <div class="video-background">
        <video autoplay muted loop>
          <source src="@/assets/film.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="carousel-container">
        <div id="carouselExampleIndicators" class="carousel slide ">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img :src="homeimg1" class="d-block img" alt="Firstslide">
            </div>
            <div class="carousel-item">
              <img :src="homeimg2" class="d-block img" alt="...">
            </div>
            <div class="carousel-item">
              <img :src="homeimg3" class="d-block img" alt="...">
            </div>
          <div class="carousel-item">
            <img :src="homeimg4" class="d-block img" alt="...">
          </div>
          <div class="carousel-item">
            <img :src="homeimg5" class="d-block img" alt="...">
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
    </div>
  </main>
</template>



<!-- <template>
  <main>
    <div class="video-container">
      <video autoplay muted loop class="video-background">
        <source src="@/assets/film.mp4" type="video/mp4" />
      </video>
      <div class="carousel-container">
        <div id="carouselExampleIndicators" class="carousel slide ">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img :src="homeimg1" class="d-block img" alt="Firstslide">
            </div>
            <div class="carousel-item">
              <img :src="homeimg2" class="d-block img" alt="...">
            </div>
            <div class="carousel-item">
              <img :src="homeimg3" class="d-block img" alt="...">
            </div>
          <div class="carousel-item">
            <img :src="homeimg4" class="d-block img" alt="...">
          </div>
          <div class="carousel-item">
            <img :src="homeimg5" class="d-block img" alt="...">
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
  </div>
  </main>
</template> -->

<script setup>
import homeimg1 from '@/assets/homeimage1.jpg'
import homeimg2 from '@/assets/homeimage2.jpg'
import homeimg3 from '@/assets/homeimage3.jpg'
import homeimg4 from '@/assets/homeimage4.jpg'
import homeimg5 from '@/assets/homeimage5.png'

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
  width: 90vw;
  height: 60vh;
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