<template>
  <div>
    <h2>Latest News</h2>
    <NewsPost v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import api from "../api.js";
import NewsPost from "../components/NewsPost.vue";

export default {
  name: "HomePage",
  components: { NewsPost },
  data() {
    return { posts: [] };
  },
  mounted() {
    api.get("/posts/").then(response => {
      this.posts = response.data;
    });
  },
};
</script>
