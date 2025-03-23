import Vue from 'vue'
import VueRouter from 'vue-router'
import Cookies from "js-cookie"

Vue.use(VueRouter)
// 进度条
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

import Home from "@/views/Home";
import {setAppTitle} from "@/utils/utils";
import Login from "@/views/user/Login";
import Profile from "@/views/user/Profile";
import Register from "@/views/user/Register";
import rice_list from "@/views/rice_list";
import product_list from "@/views/product_list";
import rice_recommend from "@/views/rice_recommend";
import plot1 from "@/views/plot1";
import plot2 from "@/views/plot2";
import plot3 from "@/views/plot3";
import plot4 from "@/views/plot4";
import predict from "@/views/predict";
import plot5 from "@/views/plot5";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: '首页'
        },
        redirect: '/rice_list',
        children:[
            { path:'profile',component:Profile, meta: { title: '个人中心'}},
            { path:'rice_list',component:rice_list, meta: { title: '水稻列表'}},
            { path:'product_list',component:product_list, meta: { title: '农产品列表'}},
            { path:'rice_recommend',component:rice_recommend, meta: { title: '水稻推荐'}},
            { path:'plot1',component:plot1, meta: { title: '各省不同农产品的各种价格变化'}},
            { path:'plot2',component:plot2, meta: { title: '不同农产品的价格对比'}},
            { path:'plot3',component:plot3, meta: { title: '各农产品产地数量饼图'}},
            { path:'plot4',component:plot4, meta: { title: '各省份蔬菜数量柱状图'}},

            { path:'predict',component:predict, meta: { title: '农产品价格预测'}},
            { path:'plot5',component:plot5, meta: { title: '农产品价格趋势'}},


        ]
    },
    { path: '/login',   name: 'login',component: Login, meta: { title: '登录' }},
    { path: '/register',name: 'register',component: Register, meta: {  title: '注册' }},


]

const router = new VueRouter({
    // 设置路由模式为‘history’，去掉默认的#
    mode: 'history',
    routes
})
//路由导航守卫
router.beforeEach((to, from, next) => {
    //  to 将要访问的路径
    //  from  从哪个路径跳转
    //  next 是一个函数  表示放行
    //  next() 放行  next('/login')去登录去
    // 进度条
    NProgress.start()
    console.log(to.path)
    if (to.path == '/login' ) {
        next()
    }else if (to.path == '/register'){
        next()
    }else{
        let isLogin = Cookies.get('user');
        if (!isLogin) next('/login')
        else next()
    }


    // var user = JSON.parse(isLogin)
})

router.afterEach(to => {
    // 进度条
    NProgress.done()
    // 更改标题
    setAppTitle(to.meta.title)
})

export default router
