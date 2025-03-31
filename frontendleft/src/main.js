import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import 'echarts-wordcloud'
import ElementUI from 'element-ui'

// 引入Echarts
import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false
Vue.use(ElementUI)
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
