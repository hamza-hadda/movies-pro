<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movie in movies" :key="movie.id">
          <td>{{ movie.title }}</td>
          <td>{{ movie.description }}</td>
          <td><v-btn small @click="viewMovie(movie.id)">Details</v-btn> </td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <button @click="fetchMovies(page - 1, 'previous')" :disabled="!prev">Previous</button>
      <button @click="fetchMovies(page + 1, 'next')" :disabled="!next">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      movies: [],
      page: 1,
      next: null,
      prev: null,
    };
  },
  mounted() {
    this.fetchMovies(this.page);
  },
  methods: {
    fetchMovies(page, action="") {
      let page_link = ""
      if(action == "next"){
         page_link = this.next
      }
      else if(action == "previous"){
         page_link = this.prev
         console.log(page_link)
      }
      else{
      page_link  = `http://localhost:8000/api/movies/?page=${page}`
      }
      if (page < 1) return;

      axios.get(page_link)
        .then(response => {
          this.movies = response.data.results;
          this.next = response.data.next;
          this.prev = response.data.previous;
          this.page = page;
        })
        .catch(error => {
          console.error(error);
        });
    },

    viewMovie(id) {
     console.log( this.$router.push({ name: 'movie-details', params: { id } }, () => {}))
    },
  },
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
.pagination {
  margin-top: 10px;
}
button {
  margin: 0 5px;
}
</style>
