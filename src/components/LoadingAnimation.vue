<template>
  <div v-if="isLoading" class="loading-container">
    <!-- Background Slideshow -->
    <div class="loading-animation">
      <transition-group name="fade">
        <img
          v-for="(image, index) in images"
          :key="image"
          :src="image"
          class="slide"
          v-show="currentImageIndex === index"
        />
      </transition-group>
    </div>

    <!-- Progress Bar -->
    <div class="loading-content">
      <div class="loading-text">Processing...</div>
      <div class="progress-bar-container">
        <div class="progress-bar" :style="{ width: `${progress}%` }"></div>
      </div>
    </div>
  </div>
</template>

<script>
import slideshow1 from '@/assets/africa/slideshow1.jpg'
import slideshow2 from '@/assets/africa/slideshow2.jpg'
import slideshow3 from '@/assets/africa/slideshow3.jpg'

export default {
  name: 'LoadingAnimation',
  props: {
    isLoading: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      images: [slideshow1, slideshow2, slideshow3],
      currentImageIndex: 0,
      progress: 0,
      slideshowInterval: null,
      progressInterval: null,
    }
  },
  watch: {
    isLoading(newVal) {
      if (newVal) {
        this.startLoadingAnimation()
      } else {
        this.stopLoadingAnimation()
      }
    },
  },
  methods: {
    startLoadingAnimation() {
      this.slideshowInterval = setInterval(this.nextImage, 2000)

      this.progressInterval = setInterval(() => {
        if (this.progress < 100) {
          const increment = Math.random() * 5 + 1 // Increment by 1-5
          this.progress = Math.min(this.progress + increment, 100)
        }
      }, 500)
    },
    stopLoadingAnimation() {
      clearInterval(this.slideshowInterval)
      clearInterval(this.progressInterval)

      this.progress = 100 // Set progress to 100% when stopping

      setTimeout(() => {
        this.progress = 0
        this.currentImageIndex = 0
      }, 1000)
    },
    nextImage() {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length
    },
  },
  beforeUnmount() {
    this.stopLoadingAnimation()
  },
}
</script>

<style scoped>
.loading-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.8);
  z-index: 9999;
}

.loading-animation {
  position: relative;
  height: 100%;
  width: 100%;
  margin-bottom: 20px;
}

.progress-bar-container {
  width: 100%;
  height: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: #4caf50;
  transition: width 0.3s ease;
}
</style>
