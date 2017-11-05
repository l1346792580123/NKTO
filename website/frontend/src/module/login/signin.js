import Vue from 'vue'
import login from './login'
import iView from 'iview'
import '../../mytheme/dist/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#nkto',
  components: { login }
})
