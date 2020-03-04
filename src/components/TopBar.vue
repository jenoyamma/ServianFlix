<template>
    <v-app-bar app color="black" dark>
      <v-container fluid>
        <v-layout row wrap align-center>
          <v-flex md8>
            <v-img
              alt="SERVIANFLIX"
              src="https://company-profile-images.s3.amazonaws.com/images/814520/1182509/logo/servian-logo.png"
              width="300"
            />
          </v-flex>
          <v-flex md4> 
            <v-layout row justify-end>
              <v-btn 
                @click.stop="search = !search" 
                large
                style="padding: 0px"
                icon
                tile
              >
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
              <v-text-field 
                label="Titles, people, genres" 
                single-line 
                hide-details 
                solo
                clearable
                v-if="search"
              />
              <v-btn large icon tile>WE</v-btn>
              <v-btn large text icon tile><v-icon color="red">mdi-heart</v-icon></v-btn>
              <v-btn large text icon tile><v-icon>mdi-database</v-icon></v-btn>
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn large text icon tile v-on="on">
                    <v-avatar tile>
                      <img
                        src="https://pbs.twimg.com/profile_images/766411362440323072/rI2LGExV_400x400.jpg"
                        alt="SageMaker"
                      >
                    </v-avatar>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item
                    v-for="(item, index) in items"
                    :key="index"
                  >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
    </v-app-bar>
</template>

<script>
export default {
    name: 'TopBar',
    data: () => ({
        items: [
            { title: 'OUR SERVICES' },
            { title: 'Cloud + Technology' },
            { title: 'Data + Analytics' },
            { title: 'Artificial Intelligence' },
            { title: 'Digital' },
            { title: 'Customer Engagement' },
        ],
        search: false
  })
}
</script>

<style>

</style>