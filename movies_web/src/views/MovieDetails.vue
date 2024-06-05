<template>
  <v-container>
    <v-card>
      <v-card-title>{{ movie.title }}</v-card-title>
      <v-card-text>{{ movie.description }}</v-card-text>
      <v-subheader>Actors</v-subheader>
      <v-list>
        <v-list-item v-for="actor in movie.actors" :key="actor.id">{{ actor.name }}</v-list-item>
      </v-list>
      <v-subheader>Reviews</v-subheader>
      <v-list>
        <v-list-item v-for="review in movie.reviews" :key="review.id">
          {{ review.review_text }}
        </v-list-item>
      </v-list>
      <v-form @submit.prevent="submitReview">
        <v-textarea v-model="newReview" label="Add a review"></v-textarea>
        <v-btn type="submit">Submit</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      movie: null,
      newReview: '',
    };
  },
  created() {
    this.fetchMovie();
  },
  methods: {
    fetchMovie() {
      const id = this.$route.params.id;
      axios.get(`http://localhost:8000/api/movies/${id}/`)
        .then(response => {
          this.movie = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    submitReview() {
      axios.post('http://localhost:8000/api/reviews/', {
        movie: this.movie.id,
        review_text: this.newReview,
      })
      .then(response => {
        this.movie.reviews.push(response.data);
        this.newReview = '';
      })
      .catch(error => {
        console.error(error);
      });
    },
  },
};
</script>
