<template>
    <v-content>
      <v-container fluid fill-height>
        <v-layout column>
          <v-layout row>
            <v-flex md3 style="background-color:black;">
              <v-layout column fill-height>
                <v-flex md2/>
                <v-flex md10>
                  <v-card height="100%" color="black" dark>
                    <v-card-title style="font-size: 5em;" color="white"> Avengers </v-card-title>
                    <v-spacer></v-spacer>
                    <v-card-text>
                      Nick Fury is compelled to launch the Avengers Initiative when Loki poses a threat to planet Earth. His squad of superheroes put their minds together to accomplish the task.
                    </v-card-text>
                    <v-card-text id="card_btn">
                        <v-btn color="red" dark tile><v-icon>mdi-play</v-icon>Play</v-btn>&nbsp;
                        <v-btn text tile dark outlined><v-icon color="white">mdi-plus</v-icon>My List</v-btn> &nbsp;
                        <v-btn text fab outlined small><v-icon color="white">mdi-thumb-up-outline</v-icon></v-btn> &nbsp;
                        <v-btn text fab outlined small><v-icon color="white">mdi-thumb-down-outline</v-icon></v-btn>
                    </v-card-text>
                    <v-card-text>
                      <p>Starring: Jeno Yamma, Jeno Yamma, Jeno Yamma</p>
                      <p>Genres: Action, Adventure</p>
                      <p>This movie is: Exciting</p>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex md9>
              <img src="../assets/avenger_main_faded.jpg" style="height: 100%; width: 100%;">
            </v-flex>
          </v-layout>
        </v-layout>
      </v-container>
    </v-content>
</template>

<script>
export default {
    name: 'MainBanner',
    data: () => ({
  })
}
</script>

<style>

</style>