<template>
  <div id="header" class="relative overflow-hidden h-[50vh]">
    <!-- Blurred Background -->
    <div class="absolute top-0 left-0 right-0 bottom-0 h-full w-full bg-cover bg-center bg-no-repeat blur-md scale-110"
      style="background-image: url('/img/headerbg3.avif');">
    </div>
    <!-- Content Container -->
    <div class="relative z-10 flex flex-col min-h-[60vh]">
      <!-- Top Navigation -->
      <header class="w-full px-4 sm:px-6 py-4">
        <div class="flex flex-col sm:flex-row justify-between items-center">
          <!-- Logo -->
          <div class="mb-4 sm:mb-0">
            <img src="/img/rocket.png" class="logo" alt="StartupStack" />
          </div>

          <!-- Navigation -->
          <nav class="flex space-x-4 sm:space-x-6 text-white font-medium py-8">
            <NuxtLink to="/"
              class="px-3 py-2 rounded-md  hover:underline link">
              Features
            </NuxtLink>
            <NuxtLink to="/"
              class="px-3 py-2 rounded-md hover:underline link">
              Extension
            </NuxtLink>
            <NuxtLink to="/startups"
              class="px-3 py-2 rounded-md hover:underline link">
              Tech Mail
            </NuxtLink>
            <NuxtLink to="/startups"
              class="px-3 py-2 rounded-md hover:underline link">
              Add Startup
            </NuxtLink>
          </nav>
        </div>
      </header>


      <!-- Main Content Area -->
      <div class="flex-1 flex items-center justify-center px-4 sm:px-6 py-8">
        <div class="text-center max-w-4xl w-full">
          <!-- Tagline -->
          <h2 class="text-4xl sm:text-5xl md:text-6xl lg:text-6xl font-bold text-white mb-4 leading-tight font-heading brand">
            Startup<span class="text-blue-600 stack">Stack</span>
          </h2>

          <p class="text-lg sm:text-xl md:text-2xl text-gray-200 mb-8 sm:mb-12 leading-relaxed font-sans">
            Explore startups, track funding, and find your perfect opportunity
          </p>

          <!-- Search Section -->
          <div
            class="bg-white bg-opacity-10 backdrop-blur-md rounded-2xl p-6 sm:p-8 border border-white border-opacity-20">
            <div class="flex flex-col sm:flex-row gap-4 max-w-3xl mx-auto">
              <!-- Search Input -->
              <div class="flex-1">
                <input type="text" placeholder="Search startups, roles, or industries..."
                  class="w-full px-4 py-3 sm:py-4 text-gray-900 bg-white rounded-xl border-0 focus:ring-2 focus:ring-blue-400 focus:outline-none placeholder-gray-500 text-sm sm:text-base" />
              </div>
  
              <!-- Search Button -->
              <button
                class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 sm:px-8 py-3 sm:py-4 rounded-xl transition-colors duration-200 flex items-center justify-center gap-2 text-sm sm:text-base">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                Search
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>