<template>
  <v-app>
    <top-bar/>
    <main-banner/>
  </v-app>
</template>

<style scoped>
  /* #card_btn.v-btn{
      margin-left:20px;
  } */
</style>

<script>
import TopBar from './components/TopBar';
import MainBanner from './components/MainBanner';

export default {
  name: 'App',
  components: {
    TopBar,
    MainBanner
  },
  data: () => ({
  }),
};
</script>
