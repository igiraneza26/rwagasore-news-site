<template>
  <AppNavbar />
  <router-view></router-view>
</template>

<script>
import AppNavbar from './components/AppNavbar.vue';
export default { components: { AppNavbar } };
</script>