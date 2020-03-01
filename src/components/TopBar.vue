<template>
    <v-app-bar app color="black" dark>
      <v-container fluid>
        <v-layout row wrap align-center>
          <v-flex md8>
            <v-img
              alt="SERVIANFLIX"
              src="https://fontmeme.com/permalink/200229/e71b14311747c3fa1621222554f017f3.png"
              width="200"
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
              <v-btn large icon tile>KIDS</v-btn>
              <v-btn large text icon tile><v-icon>mdi-gift</v-icon></v-btn>
              <v-btn large text icon tile><v-icon>mdi-bell</v-icon></v-btn>
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn large text icon tile v-on="on">
                    <v-avatar tile>
                      <img
                        src="https://m-square.com.au/wp-content/uploads/2018/04/IconOnly.png"
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
            { title: 'Click Me' },
            { title: 'Click Me' },
            { title: 'Click Me' },
            { title: 'Click Me 2' },
        ],
        search: false
  })
}
</script>

<style>

</style>