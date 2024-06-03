<template>
  <div id="app">
    <nav>
      <router-link to="/actors">Actors</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/reviews">Reviews</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
nav {
  margin-bottom: 1em;
}
nav a {
  margin-right: 1em;
}
</style>
