<template>
    <v-dialog
      v-model="dialog"
      max-width="70%"
      height="1000"
      overlay-opacity="0.9"
    >
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">And a 1</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step :complete="e1 > 2" step="2">Then a 2</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="3">Off we go</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card height="200px">
              <v-card-title>Welcome to Servian's AWS AI/ML Workshop</v-card-title>
                <v-card-text>
                  In this hands-on part of the workshop you will be building, training and deploying a Movie Recommendation. 
                  At Servian, we have empowered many businesses through the use of Artificial Intelligence and Machine Learning. 
                  We believe that Artificial Intelligence is fueled by the combination of data, advanced analytics and cognitive services. 
                  That's why our digital capability together with our applied machine learning and deep learning experience will produces synergy to your innovation success.
                </v-card-text>
              <v-btn color="primary" @click="e1 = 2">I got it!</v-btn>
            </v-card>

          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card height="200px">
              <v-card-title>Building Servianflix - Movie Recommendation System</v-card-title>
              <v-card-text>
                This is a hands-on workshop so you will need access to a computer. You will be using the MovieLens dataset which contains movies
                that you may have watched many years ago. You will be required to explore the data and use <b>Factorization Machines</b> to build your model. Once you're done with building and training the model, 
                you will deploy it as an endpoint and use that endpoint to drive your own Movie Recommendation website, or Servianflix. Be sure to keep note of the endpoint name and your defined user name - you will know what
                this is once you go through the notebook.   
              </v-card-text>
              <v-btn color="primary" @click="e1 = 3"> Yep, next</v-btn>
            </v-card>
          </v-stepper-content>
          <v-stepper-content step="3">
            <v-card height="200px">
              <v-text-field v-model="username" label="Paste your user name here" required></v-text-field>
              <v-text-field v-model="endpoint" label="Paste your endpoint name here" required></v-text-field>

              <v-btn :disabled="isComplete" color="primary" @click="click">
                I am ready, save
              </v-btn>
            </v-card>
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
      dialog: true,
      username: "",
      endpoint: "",
    }),
    methods: {
      click() {
        this.dialog = false
        let dat = {"username": this.username, "endpoint": this.endpoint}
        this.$emit('dat', dat)
    },
      computed: {
        isComplete() {
          return !(this.username && this.endpoint);
        }
      }
    }
  }
</script>
