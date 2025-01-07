<template>
  <div class="world-map-container">
    <!-- World Map Background -->
    <div class="map">
      <img src="@/assets/world-map.png" alt="World Map" class="map-image" />

      <!-- Continent Buttons -->
      <button class="continent-button north-america" @click="handleContinentClick('North America')">
        North America
      </button>
      <button class="continent-button south-america" @click="handleContinentClick('South America')">
        South America
      </button>
      <button class="continent-button europe" @click="handleContinentClick('Europe')">
        Europe
      </button>
      <button class="continent-button africa" @click="handleContinentClick('Africa')">
        Africa
      </button>
      <button class="continent-button asia" @click="handleContinentClick('Asia')">Asia</button>
      <button class="continent-button australia" @click="handleContinentClick('Australia')">
        Australia
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handleContinentClick(continent) {
      alert(`You clicked on ${continent}`)
      this.$router.push('/new-page')
    },
  },
}
</script>

<style>
.world-map-container {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.map {
  position: relative;
  width: 100%; /* Adjust the map size */
}

.map-image {
  width: 100%;
  height: auto;
  display: block;
}

.continent-button {
  position: absolute;
  background-color: rgba(0, 123, 255, 0.418); /* Semi-transparent blue */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
  font-size: 1.2rem;
  text-align: center;
  transform: translate(-50%, -50%);
}

.continent-button:hover {
  background-color: rgba(0, 123, 255, 1); /* Fully opaque blue on hover */
}

/* Button positions (adjust these values to fit your map) */
.north-america {
  top: 34%;
  left: 20%;
}

.south-america {
  top: 67%;
  left: 30%;
}

.europe {
  top: 35%;
  left: 52%;
}

.africa {
  top: 55%;
  left: 53%;
}

.asia {
  top: 35%;
  left: 70%;
}

.australia {
  top: 76%;
  left: 86%;
}
</style>
