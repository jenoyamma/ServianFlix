<template>
  <v-content style="padding-top: 10px; padding-bottom: 10px; background-color:#141414;">
  <v-card style="background-color:#141414;" dark><v-card-title>{{title}}</v-card-title></v-card>
  <v-carousel
    height="200"
    hide-delimiter-background
    :show-arrows="showarrows"
    show-arrows-on-hover
    hide-delimiters
  >
    <v-carousel-item v-for="n in 3" :key="n">
      <v-sheet
        color="#141414"
        height="100%"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-layout row justify-center>
              <v-flex v-for="image in images" :key="image" md2 class="mx-4">
                <v-card tile>
                  <v-img
                    :src="`${image}`"
                    @click="overlay = true; test={image}; showarrows = false"
                  >
                  </v-img>
                </v-card>
                <v-overlay :value="overlay" absolute opacity="0.30">
                  <v-btn absolute right fab icon @click="overlay = false">
                    <v-icon large>mdi-close</v-icon>
                  </v-btn>
                  <movie-carousels-mini></movie-carousels-mini>
                </v-overlay>
              </v-flex>
          </v-layout>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
  </v-content>
</template>

<script>
import MovieCarouselsMini from './MovieCarouselsMini';
export default {
    name: 'MovieCarousels',
    props: {
      title: String
    },
    components: {
      MovieCarouselsMini
    },
    data: () => ({
      images: [
        'https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BNDc1ZTlmOWUtNDY2YS00OGU5LTg2MTYtYTk2MmQzMGE2NzUwXkEyXkFqcGdeQXVyODkzNTgxMDg@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BMzQ3NTQxMjItODBjYi00YzUzLWE1NzQtZTBlY2Y2NjZlNzkyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BZjU0Yzk2MzEtMjAzYy00MzY0LTg2YmItM2RkNzdkY2ZhN2JkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BOTdmNTFjNDEtNzg0My00ZjkxLTg1ZDAtZTdkMDc2ZmFiNWQ1XkEyXkFqcGdeQXVyNTAzNzgwNTg@._V1_UX182_CR0,0,182,268_AL_.jpg',
      ],
      overlay: false,
      test: "",
      showarrows: true
  }),
  methods: {
  }
}
</script>

<style>

</style>