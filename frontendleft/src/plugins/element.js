import Vue from 'vue'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element)

import {
  Button,
  Select,
  Col,
  Row,
  Form,
  FormItem,
  Card,
  Option,
  Message
} from 'element-ui'

Vue.use(Button)
Vue.use(Select)
Vue.use(Col)  // 对应<el-col>
Vue.use(Row)  // 对应<el-row>
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Card)
Vue.use(Option)

// 挂载消息提示组件
Vue.prototype.$message = Message