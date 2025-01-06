import { createRouter, createWebHistory } from "vue-router";

import NewPage from "../views/NewPage.vue";
import HomeView from "@/views/HomeView.vue";

const routes = [
  { path: "/", component: HomeView },
  { path: "/new-page", component: NewPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
