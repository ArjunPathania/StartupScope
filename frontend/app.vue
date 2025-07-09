<template>
  <div class="min-h-screen flex flex-col bg-gray-50 text-gray-900">
    <DefaultHeader />

    <main class="flex-1 p-6">
      <NuxtPage />
    </main>

    <DefaultFooter />
  </div>
</template>

<script setup>
import DefaultHeader from '~/components/DefaultHeader.vue'
import DefaultFooter from '~/components/DefaultFooter.vue'
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Poppins:wght@600;700&display=swap');
</style>