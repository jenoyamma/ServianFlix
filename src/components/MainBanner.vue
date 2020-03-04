<template>
    <v-content>
      <v-container fluid fill-height style="padding-top: 0px; padding-bottom: 0px">
        <v-layout column>
          <v-layout row>
            <v-flex md3 style="background-color:black;">
              <v-layout column fill-height>
                <v-flex md2/>
                <v-flex md10>
                  <v-card height="100%" color="black" dark>
                    <v-card-title style="font-size: 2vw; font-size: 40px;">{{movieTitle}}</v-card-title>
                    <v-spacer></v-spacer>
                    <v-card-text>
                      <v-rating color="blue" v-model="rating"></v-rating>
                      {{overview}}
                    </v-card-text>
                    <v-card-text id="card_btn">
                        <v-btn color="blue" dark tile><v-icon>mdi-play</v-icon>Play</v-btn>&nbsp;
                        <v-btn text tile dark outlined><v-icon>mdi-video</v-icon>Trailer</v-btn> &nbsp;
                        <v-btn text fab outlined small><v-icon>mdi-emoticon-happy</v-icon></v-btn> &nbsp;
                        <v-btn text fab outlined small><v-icon>mdi-emoticon-sad</v-icon></v-btn>
                    </v-card-text>
                    <v-card-text>
                      <p>Genres: {{genre}}</p>
                      <p>This movie is: Exciting</p>
                      <p>Chance that you will like this: 63%</p>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex md9>
              <img src="../assets/forest_gump_faded.jpg" style="height: 100%; width: 100%;">
            </v-flex>
          </v-layout>
        </v-layout>
      </v-container>
    </v-content>
</template>

<script>

export default {
    name: 'MainBanner',
    props: {
      attribute: String
    },
    data: () => ({
      req_type: 'single',
      movieTitle: '',
      overview: '',
      moviePoster: '',
      vote_count: '',
      vote_average: '',
      genre: '',
      movieReleaseYear: ''

  }), 
  mounted() {
        this.$http.get("https://3e8hjsabsj.execute-api.us-east-2.amazonaws.com/prod/get-movies", {
        params: {
            req_type: this.req_type, 
            attribute: this.attribute
        }
        }).then(response => {
            this.movieTitle = response.data.body.Items[0].movieTitle;
            this.overview = response.data.body.Items[0].overview;
            this.moviePoster = response.data.body.Items[0].moviePoster;
            this.vote_count = response.data.body.Items[0].vote_count;
            this.vote_average = response.data.body.Items[0].vote_average;
            this.genre = response.data.body.Items[0].genre;
            this.movieReleaseYear = response.data.body.Items[0].movieReleaseYear;
        })
    }
}

</script>

<style>

</style>