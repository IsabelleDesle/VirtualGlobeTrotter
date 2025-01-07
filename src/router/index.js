import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import NewPage from '../views/NewPage.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/new-page', component: NewPage },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router
