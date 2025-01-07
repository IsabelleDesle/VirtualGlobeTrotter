<script>
import axios from 'axios'
import { ref, computed } from 'vue' // Import Vue composition API utilities

// Create a reusable speech recognition service
const createSpeechRecognition = () => {
  if (!('webkitSpeechRecognition' in window)) {
    return null
  }
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
  const recognition = new SpeechRecognition()
  recognition.lang = 'en-US'
  recognition.interimResults = false
  recognition.maxAlternatives = 1
  return recognition
}

// API service
const api = {
  async changeBackground(input) {
    try {
      const response = await axios.post('http://127.0.0.1:5000/change-background', { input })
      return response.data.background_image
    } catch (error) {
      console.error('Error changing background:', error)
      throw error
    }
  },
}

export default {
  name: 'BackgroundChanger', // Named component for better debugging

  setup() {
    const userInput = ref('')
    const backgroundImage = ref('https://i.redd.it/8kdbhjg3fza61.jpg')
    const isListening = ref(false)
    const recognition = createSpeechRecognition()

    // Computed property for background style
    const backgroundStyle = computed(() => ({
      backgroundImage: `url(${backgroundImage.value})`,
    }))

    const startListening = () => {
      if (!recognition) {
        alert('Your browser does not support speech recognition. Please use Chrome.')
        return
      }

      recognition.onstart = () => {
        isListening.value = true
        console.log('Voice recognition started...')
      }

      recognition.onresult = async (event) => {
        isListening.value = false
        const transcript = event.results[0][0].transcript
        userInput.value = transcript

        try {
          const newBackground = await api.changeBackground(transcript)
          backgroundImage.value = newBackground
        } catch (error) {
          // Handle error appropriately
          console.error('Failed to change background:', error)
        }
      }

      recognition.onerror = (event) => {
        isListening.value = false
        console.error('Speech recognition error:', event.error)
      }

      recognition.onend = () => {
        isListening.value = false
        console.log('Voice recognition ended.')
      }

      recognition.start()
    }

    return {
      userInput,
      backgroundStyle,
      isListening,
      startListening,
    }
  },
}
</script>

<template>
  <div :style="backgroundStyle" class="background-container">
    <div class="input-container">
      <p v-if="userInput" class="transcript-display">You said: "{{ userInput }}"</p>
      <div class="button-container">
        <button @click="startListening" :disabled="isListening" class="primary-button">
          {{ isListening ? 'Listening...' : 'Start Voice Input' }}
        </button>
        <button @click="$router.push('/')" class="secondary-button">Go Back</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.background-container {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  position: fixed;
  inset: 0; /* Modern alternative to setting top, right, bottom, left */
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-container {
  text-align: center;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 2rem;
  border-radius: 8px;
  backdrop-filter: blur(5px);
}

.button-container {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.transcript-display {
  background-color: #4caf50;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 5px;
  margin-bottom: 1rem;
}

.primary-button,
.secondary-button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  transition:
    transform 0.2s ease,
    opacity 0.2s ease;
}

.primary-button {
  background-color: #4caf50;
  color: white;
}

.secondary-button {
  background-color: #f5f5f5;
  color: #333;
}

.primary-button:hover,
.secondary-button:hover {
  transform: translateY(-2px);
  opacity: 0.9;
}

.primary-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
  transform: none;
}
</style>
