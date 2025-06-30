<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

const message = ref('')

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/api/ping')
  message.value = res.data.message
})
</script>

<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold">Nuxt + FastAPI</h1>
    <p class="mt-4 text-green-600">Response from backend: {{ message }}</p>
  </div>
</template>
