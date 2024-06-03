import Vue from 'vue';
import VueRouter from 'vue-router';
import ActorList from '../views/ActorList.vue';
import MovieList from '../views/MovieList.vue';
import ReviewList from '../views/ReviewList.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/actors',
    name: 'Actors',
    component: ActorList
  },
  {
    path: '/movies',
    name: 'Movies',
    component: MovieList
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: ReviewList
  }
];

const router = new VueRouter({
  routes
});

export default router;
