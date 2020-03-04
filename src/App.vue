<template>
  <v-app>
    <top-bar/>
    <main-banner attribute="69"/>
    <v-container fluid fill-height style="padding: 0px;">
      <v-layout column>
        <v-flex md4>
          <movie-carousels title="Popular on Servianflix"></movie-carousels>
        </v-flex>
        <v-spacer/>
        <v-flex md3>
          <movie-carousels title="You may also like"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Action & Adventure"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Comedies"></movie-carousels>
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
import MainBanner from './components/MainBanner';
import MovieCarousels from './components/MovieCarousels';

export default {
  name: 'App',
  components: {
    TopBar,
    MainBanner,
    MovieCarousels,
  },
  data: () => ({
    snackbar: true
  }),
};
</script>
