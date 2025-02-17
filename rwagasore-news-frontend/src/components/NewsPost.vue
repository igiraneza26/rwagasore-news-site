<template>
  <div class="post">
    <h3><router-link :to="'/post/' + post.id">{{ post.title }}</router-link></h3>
    <p>By {{ post.author__username }} | {{ post.created_at }}</p>
    <p>{{ post.content.substring(0, 100) }}...</p>
    <button @click="vote('up')">👍 {{ upvotes }}</button>
    <button @click="vote('down')">👎 {{ downvotes }}</button>
  </div>
</template>

<script>
import api from "../api.js";

export default {
  name: "NewsPost",
  props: ["post"],
  data() {
    return {
      upvotes: this.post.upvotes, // Create a local copy
      downvotes: this.post.downvotes,
    };
  },
  methods: {
    vote(type) {
      api.post(`/posts/${this.post.id}/vote/`, { vote: type }).then(response => {
        this.upvotes = response.data.upvotes;
        this.downvotes = response.data.downvotes;
      });
    },
  },
};
</script>