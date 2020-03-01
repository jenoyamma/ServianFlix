import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false
Vue.use(vuetify, {iconfont: 'mdi'})

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
