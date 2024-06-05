<!-- src/App.vue -->
<template>
  <div id="app">
    <Movies />
  </div>
</template>

<script>
import Movies from './views/MovieList.vue';

export default {
  name: 'App',
  components: {
    Movies,
  },
};
</script>