<template>
  <v-app>
    <welcome-form @dat="test"></welcome-form>
    <top-bar/>
    <main-banner-FP attribute="69"/>
    <v-container fluid fill-height style="padding: 0px;">
      <v-layout column>
        <v-flex md3>
          <v-lazy v-model="isActive">
            <movie-carousels title="You may also like" :attribute="username" :endpoint="endpoint"></movie-carousels>
          </v-lazy>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Action & Adventure" attribute="Adventure" :endpoint="endpoint"></movie-carousels>
        </v-flex>   
        <v-flex md3>
          <movie-carousels title="Animation" attribute="Animation" :endpoint="endpoint"></movie-carousels>
        </v-flex>              
        <v-flex md3>
          <movie-carousels title="Romance" attribute="Romance" :endpoint="endpoint"></movie-carousels>
        </v-flex>
        <v-flex md3>
          <movie-carousels title="Sci-Fi" attribute="Sci-Fi" :endpoint="endpoint"></movie-carousels>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<style>
</style>

<script>
import TopBar from './components/TopBar';
import MainBannerFP from './components/MainBannerFP';
import MovieCarousels from './components/MovieCarousels';
import WelcomeForm from './components/WelcomeForm';

export default {
  name: 'App',
  components: {
    TopBar,
    MainBannerFP,
    MovieCarousels,
    WelcomeForm
  },
  data: () => ({
    username: "",
    endpoint: "",
    isActive: false
  }),
  methods: {
    test(event) {
      this.username = event.username
      this.endpoint = event.endpoint
      console.log(this.username)
    }
  }
};
</script>
