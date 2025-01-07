<template>
  <div>
    <!-- Render the loading animation -->
    <LoadingAnimation :is-loading="isLoading" />
  </div>
</template>

<script>
import LoadingAnimation from '@/components/LoadingAnimation.vue'
import axios from 'axios'

export default {
  components: {
    LoadingAnimation,
  },
  data() {
    return {
      isLoading: false,
      dataToPost: '',
    }
  },
  created() {
    // Retrieve the data to post from the route
    this.dataToPost = this.$route.query.dataToPost || ''
    this.handleRequest() // Trigger the API request and loading animation
  },
  methods: {
    async handleRequest() {
      this.isLoading = true // Start the loading animation
      try {
        await axios.post('http://127.0.0.1:5000/process-request', {
          data: this.dataToPost,
        })
        this.$router.push('/new-page') // Redirect on success
      } catch (error) {
        console.error('API request failed:', error)
      } finally {
        this.isLoading = false // Stop the loading animation
      }
    },
  },
}
</script>
