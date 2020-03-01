<template>
  <v-content style="padding-top: 10px; padding-bottom: 10px; background-color:#141414;">
    <v-carousel
      height="200"
      hide-delimiter-background
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
                    <v-img :src="`${image}`"></v-img>
                  </v-card>
                </v-flex>
            </v-layout>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </v-content>
</template>

<script>
export default {
    name: 'MovieCarouselsMini',
    props: {
    },
    data: () => ({
      images: [
        'https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BNDc1ZTlmOWUtNDY2YS00OGU5LTg2MTYtYTk2MmQzMGE2NzUwXkEyXkFqcGdeQXVyODkzNTgxMDg@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BMzQ3NTQxMjItODBjYi00YzUzLWE1NzQtZTBlY2Y2NjZlNzkyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BZjU0Yzk2MzEtMjAzYy00MzY0LTg2YmItM2RkNzdkY2ZhN2JkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
        'https://m.media-amazon.com/images/M/MV5BOTdmNTFjNDEtNzg0My00ZjkxLTg1ZDAtZTdkMDc2ZmFiNWQ1XkEyXkFqcGdeQXVyNTAzNzgwNTg@._V1_UX182_CR0,0,182,268_AL_.jpg',
      ],
  }),
  methods: {
  }
}
</script>

<style>

</style>