<template>
  <h1>Hello App!</h1>
  <p>
    <strong>Current route path:</strong> {{ $route.fullPath }}
  </p>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/new-page">START</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>
