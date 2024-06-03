<template>
  <div>
    <h1>Reviews</h1>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        Review for {{ review.movie.title }}: {{ review.grade }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      reviews: []
    };
  },
  created() {
    axios.get('reviews/')
      .then(response => {
        this.reviews = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
