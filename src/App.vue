<template>
  <v-app>
    <top-bar/>
    <main-banner/>
    <v-container fluid fill-height style="padding: 0px;">
      <v-layout column>
        <v-flex md3>
          <movie-carousels title="Popular on Servianflix"></movie-carousels>
        </v-flex>
        <v-spacer/>
        <v-flex md3>
          <movie-carousels title="Action & Adventure"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Comedies"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Romance"></movie-carousels>
        </v-flex>
      </v-layout>
    </v-container>
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
  }),
};
</script>
