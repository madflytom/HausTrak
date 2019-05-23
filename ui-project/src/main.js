import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import { MdButton, MdContent, MdTabs, MdToolbar, MdCard, MdList, MdDrawer, MdApp, MdRipple, MdIcon} from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(MdToolbar)
Vue.use(MdCard)
Vue.use(MdList)
Vue.use(MdDrawer)
Vue.use(MdApp)
Vue.use(MdRipple)
Vue.use(MdIcon)

Vue.config.productionTip = false
Vue.prototype.$axios = axios

Vue.material.ripple = true
Vue.material.theming = {}


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
