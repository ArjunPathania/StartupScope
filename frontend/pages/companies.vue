<script setup>
const { data: companies, error, refresh } = await useFetch(
  'http://localhost:8000/api/v1/companies/', {
    method: 'GET',
  }
)
</script>

<template>
  <div>
    <h1>Companies</h1>
    <div v-if="companies">
      <ul>
        <li v-for="c in companies" :key="c.id">
          {{ c.name }}
        </li>
      </ul>
    </div>
    <div v-if="error">Error: {{ error }}</div>
  </div>
</template>