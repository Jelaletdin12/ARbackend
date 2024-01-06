import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/home.vue';
import News from '../components/News_Details.vue';
import Profile_Det from '../components/Profile_Det.vue';
import Search from '../components/Search.vue';
import theme from '../components/theme.vue';
// import content from '../components/content_photos.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/News/:id', name: 'News', component: News },
  { path: '/Profile_Det/:id', name: 'Profile_Det', component: Profile_Det },
  // { path: '/Suratlar', name: 'Suratlar', component: content },
  { path: '/Search/:txt', name: 'Search', component: Search },
];

const router = createRouter({
  mode: 'history',
  history: createWebHistory(), //import.meta.env.BASE_URL
  routes, 
});

export default router;
