<script>
export default {
  methods: {
    start() {
      this.$router.push('/new-page')
    },
  },
}
</script>

<template>
  <div class="background-container1">
    <div class="content">
      <button @click="start">START</button>
    </div>
  </div>
</template>

<style>
.background-container1 {
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content {
  text-align: center;
}

h2 {
  padding: 15px 30px;
  font-size: 1.5rem;
  color: #fff;
  cursor: pointer;
}

button {
  padding: 4vh 8vw; /* Use viewport units for responsive sizing */
  font-size: 2vh; /* Adjust font size based on viewport height */
  color: #fff;
  background-color: #007bff;
  cursor: pointer;
  border: none;
  border-radius: 10px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>
