import { createWebHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import NewPage from '../views/NewPage.vue'
import WorldMap from '../views/WorldMap.vue'
import Loading from '../views/Loading.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/new-page', component: NewPage },
  { path: '/map', component: WorldMap },
  { path: '/loading', component: Loading },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
