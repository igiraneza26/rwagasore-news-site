<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/login" v-if="!user">Login</router-link>
    <button v-if="user" @click="logout">Logout</button>
  </nav>
</template>

<script>
import api from "../api.js";

export default {
  data() {
    return { user: localStorage.getItem("user") };
  },
  methods: {
    logout() {
      api.get("/logout/").then(() => {
        localStorage.removeItem("user");
        this.user = null;
        this.$router.push("/");
      });
    },
  },
};
</script>

<style>
nav {
  background: #d60d0d;
  color: white;
  padding: 15px;
  display: flex;
  justify-content: space-around;
}
</style>