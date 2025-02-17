<template>
    <div>
      <h2>{{ post.title }}</h2>
      <p>By {{ post.author }} | {{ post.created_at }}</p>
      <p>{{ post.content }}</p>
  
      <h3>Comments</h3>
      <ul>
        <li v-for="comment in post.comments" :key="comment.id">
          <strong>{{ comment.author }}</strong>: {{ comment.text }}
        </li>
      </ul>
  
      <h3>Add a Comment</h3>
      <textarea v-model="newComment"></textarea>
      <button @click="addComment">Submit</button>
    </div>
  </template>
  
  <script>
  import api from "../api.js";
  
  export default {
    data() {
      return { post: {}, newComment: "" };
    },
    mounted() {
      const postId = this.$route.params.id;
      api.get(`/posts/${postId}/`).then(response => {
        this.post = response.data;
      });
    },
    methods: {
      addComment() {
        api.post(`/posts/${this.post.id}/comment/`, { text: this.newComment })
          .then(() => {
            alert("Comment added!");
            location.reload(); // Reload page to show new comment
          })
          .catch(err => alert("Error: " + err));
      }
    }
  };
  </script>  