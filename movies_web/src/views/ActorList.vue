<template>
  <div>
    <h1>Actors</h1>
    <ul>
      <li v-for="actor in actors" :key="actor.id">
        {{ actor.first_name }} {{ actor.last_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      actors: []
    };
  },
  created() {
    axios.get('actors/')
      .then(response => {
        this.actors = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
