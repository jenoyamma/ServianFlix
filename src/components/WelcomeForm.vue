<template>
    <v-dialog
      v-model="dialog"
      max-width="100%"
      max-height="70%"
      overlay-opacity="0.9"
    >
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">Name of step 1</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step :complete="e1 > 2" step="2">Name of step 2</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="3">Name of step 3</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn
              color="primary"
              @click="e1 = 2"
            >
              OK, Next
            </v-btn>
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn
              color="primary"
              @click="e1 = 3"
            >
              yep, next
            </v-btn>
          </v-stepper-content>

          <v-stepper-content step="3">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn
              color="primary"
              @click="dialog = false"
            >
              I am ready, save
            </v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
  </v-dialog>
</template>

<script>
  export default {
    name: 'WelcomeForm',
    props: {
    },
    data: () => ({
      e1: 1,
      dialog: true
    }),
  }
</script>
