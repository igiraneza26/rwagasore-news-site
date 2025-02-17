<template>
  <div>
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
  </div>
</template>

<script>
import api from "../api.js";

export default {
  name: "UserLogin",
  data() {
    return { username: "", password: "" };
  },
  methods: {
    login() {
      api.post("/login/", { username: this.username, password: this.password })
        .then(response => {
          localStorage.setItem("user", response.data.user);
          this.$router.push("/");
        })
        .catch(() => alert("Invalid credentials"));
    },
  },
};
</script>