import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./views/HomePage.vue"; // Ensure correct component names
import PostDetail from "./views/PostDetail.vue";
import UserLogin from "./views/UserLogin.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/post/:id", component: PostDetail },
  { path: "/login", component: UserLogin },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;