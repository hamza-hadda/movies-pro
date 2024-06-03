<template>
  <div>
    <h1>Movies</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        {{ movie.title }} - {{ movie.description }}
        <ul>
          <li v-for="actor in movie.actors" :key="actor.id">
            {{ actor.first_name }} {{ actor.last_name }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      movies: []
    };
  },
  created() {
    axios.get('movies/')
      .then(response => {
        this.movies = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
