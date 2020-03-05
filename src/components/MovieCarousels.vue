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
    <v-carousel-item v-for="image in images" :key="image">
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
              <v-flex v-for="img in image" :key="img" md1 class="mx-4">
                <v-card tile>
                  <v-img
                    :src="`${img.moviePoster}`"
                    @click.stop="dialog = true; movieId=img.movieId;"
                  >
                  </v-img>
                </v-card>
              </v-flex>
          </v-layout>
        </v-row>
      </v-sheet>
    </v-carousel-item>
    </v-carousel>
    <v-dialog v-model="dialog" overlay-opacity=0.9>
      <v-btn absolute right small fab color="red" dark @click="dialog = false">
          <v-icon>mdi-close</v-icon>
      </v-btn>
      <main-banner style="padding:15px !important" :attribute="movieId" :sm_fm_endpoint="endpoint"/>
    </v-dialog>
  </v-content>
</template>

<script>
import MainBanner from './MainBanner';
export default {
    name: 'MovieCarousels',
    props: {
      title: String,
      attribute: String,
      endpoint: String
    },
    components: {
      MainBanner
    },
    data: () => ({
      images: null,
      dialog: false,
      req_type: 'genre',
      movieId: "",
  }),
  methods: {
    clickMethod(){
      console.log("HI")
    }
  },
  mounted() {
      this.$http.get("https://3e8hjsabsj.execute-api.us-east-2.amazonaws.com/prod/get-movies", {
      params: {
          req_type: this.req_type, 
          attribute: this.attribute
      }
      }).then(response => {
          this.images = response.data.body
      })
  },
  watch: {
    attribute: function(newattribute){
        this.$http.get("https://3e8hjsabsj.execute-api.us-east-2.amazonaws.com/prod/get-movies", {
            params: {
                req_type: this.req_type, 
                attribute: newattribute
            }
        }).then(response => {
          this.images = response.data.body
        })
    }
  }
}
</script>

<style>

</style>