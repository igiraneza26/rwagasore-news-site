import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Ensure router is imported

const app = createApp(App);
app.use(router); // Use the router
app.mount("#app");