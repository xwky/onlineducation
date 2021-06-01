// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { Swipe, SwipeItem, Form } from 'vant';
import { Lazyload } from 'vant';
import {Search} from 'vant';
import Vant from 'vant';
import 'vant/lib/index.css';
import Router from 'vue-router';
import axios from 'axios';
import './assets/iconfont/iconfont.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// 引入store.js
import store from './vuex/store' 
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import VideoPlayer from 'vue-video-player'
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.use(VideoPlayer)


Vue.use(iView) 

Vue.use(ElementUI)


Vue.config.productionTip = false

Vue.use(Swipe);
Vue.use(SwipeItem);

Vue.use(Lazyload);
Vue.use(Vant);
Vue.use(Router)
Vue.use(Search)
Vue.prototype.axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // 相当于store:store ，注册之后，子组件中可以使用this.$store访问
  store,
  components: { App },
  template: '<App/>'
})
