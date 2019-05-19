import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueMDCAdapter from 'vue-mdc-adapter'
import router from './router'

Vue.use(VueMDCAdapter)

Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
