<template>
  <div>
    <h1>Movies</h1>
    <v-row>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
      <v-card>
      <v-card-item>
        <v-card-title>{{ movie.title }}</v-card-title>
        <v-card-subtitle>{{ movie.description }}</v-card-subtitle>
      </v-card-item>
      <v-card-text>
        <h3>actors</h3>
        <ul>
          <li v-for="actor in movie.actors" :key="actor.id">
            {{ actor.first_name }} {{ actor.last_name }}
          </li>
        </ul>
        <h3>Reviews</h3>
        <ul>
          <li v-for="review in movie.reviews" :key="review.id">
            {{ review.grade }}
          </li>
        </ul>
        </v-card-text>
        </v-card>
     </li>
    </ul>
    </v-row>
  </div>
</template>

<script>
import axios from './axios';

export default {
  data() {
    return {
      movies: []
    };
  },
  created() {
    axios.get('movies/')
      .then(response => {
        this.movies = response.data.results;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
