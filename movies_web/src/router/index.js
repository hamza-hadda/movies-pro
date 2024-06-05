import { createRouter, createWebHistory } from 'vue-router';
import MovieDetails from '../views/MovieDetails.vue';

const routes = [
  {
    path: '/movies/:id',
    name: 'movie-details',
    component: MovieDetails,
  },
];
console.log(routes)

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
