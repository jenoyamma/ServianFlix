<template>
  <v-app>
    <top-bar/>
    <main-banner-FP attribute="69"/>
    <v-container fluid fill-height style="padding: 0px;">
      <v-layout column>
        <v-flex md4>
          <movie-carousels title="You may also like" attribute="Animation"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Action & Adventure" attribute="Adventure"></movie-carousels>
        </v-flex>   
        <v-flex md3>
          <movie-carousels title="Animation" attribute="Animation"></movie-carousels>
        </v-flex>              
        <v-flex md3>
          <movie-carousels title="Romance" attribute="Romance"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Sci-Fi" attribute="Sci-Fi"></movie-carousels>
        </v-flex>
      </v-layout>
    </v-container>
    <v-snackbar v-model="snackbar" timeout=10000> 
      <b>Resize browser slightly if movies doesn't load</b>
      <v-btn color="red" text @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </v-app>
</template>

<style>
</style>

<script>
import TopBar from './components/TopBar';
import MainBannerFP from './components/MainBannerFP';
import MovieCarousels from './components/MovieCarousels';

export default {
  name: 'App',
  components: {
    TopBar,
    MainBannerFP,
    MovieCarousels,
  },
  data: () => ({
    snackbar: true
  }),
};
</script>
