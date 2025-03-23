<template>
  <div id="home">
    <transition name="el-fade-in-linear">
      <!--左右分栏 布局-->
      <el-container style="height: 100%;width: 100%">
        <!--          侧边栏-->
        <el-aside style="background-color:#203042;"
                  :width="isCollapse ? '64px' : '240px'">
          <div class="title">
            <h1 v-if="!isCollapse">{{ title }}</h1>
            <img v-else src="../assets/images/logo.png" alt="">
          </div>
          <el-menu background-color="#213042" text-color="#fff"
                   unique-opened
                   :collapse="isCollapse"
                   :default-active="activateIndex"
                   :collapse-transition="false"
                   :router="true">
            <!--          一级菜单-->
            <el-submenu :index="firstItem.id+ ''" v-for="firstItem in menuDataList" :key="firstItem.id">
              <!--            一级菜单的模板区域-->
              <template slot="title">
                <i :class="firstItem.icon"></i>
                <span>{{ firstItem.name }}</span>
              </template>
              <!--            二级菜单-->
              <el-menu-item :index="'/'+ item.path" v-for="item in firstItem.children" :key="item.id">
                <template slot="title">
                  <i :class="item.icon"></i>
                  <span>{{ item.name }}</span>
                </template>
              </el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <!--          右边容器-->
        <el-container style="height: auto;background: #EEF0F8">
          <!--          头部-->
          <el-header>
            <i style="font-size: 20px;margin-left: 15px" :class=" isCollapse ? 'el-icon-s-unfold' : 'el-icon-s-fold' "
               @click="changeCollapse"></i>
            <el-breadcrumb separator="/">
              <el-breadcrumb-item>{{ breadcrumb }}</el-breadcrumb-item>
            </el-breadcrumb>
            <div class="user-info">
              <el-dropdown trigger="click" @command="handleCommand">
                <span class="el-dropdown-link">
                  {{ user.username }}<i style="color: black" class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item command="profile" icon="el-icon-plus">个人中心</el-dropdown-item>
                  <el-dropdown-item command="logout" icon="el-icon-circle-plus">退出登录</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </el-header>
          <!--            主题区域-->
          <el-main style="">
            <!--         路由占位符-->
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>
    </transition>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import {User_info} from "@/api/api";

export default {
  name: "Home",
  data() {
    return {
      isCollapse: false,
      title: process.env.VUE_APP_TITLE,
      activateIndex: '',
      menuDataList: [],
      user: "",
      breadcrumb:''
    }
  },
  created() {
    this.getMenuList()
    this.get_userinfo()
    this.get_breadcrumb()
  },
  methods: {
    get_breadcrumb(){
      this.breadcrumb = this.$route.meta.title
    },
    changeCollapse() {
      this.isCollapse = !this.isCollapse
    },
    // 获取用户信息
    get_userinfo() {
      User_info({}).then(res => {
        this.user = res.data
      });
    },

    // 获取菜单列表
    getMenuList() {
      this.menuDataList = [
        {
          "id": 1,
          "name": "数据列表",
          "path": "welcome",
          "icon": "el-icon-menu",
          "children": [
            {
              "id": 31,
              "name": "水稻列表",
              "path": "rice_list",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 32,
              "name": "农产品列表",
              "path": "product_list",
              "icon": "el-icon-s-data",
              "children": []
            },
          ]
        },
        {
          "id": 2,
          "name": "数据可视化",
          "icon": "el-icon-menu",
          "path": "",
          "children": [
            {
              "id": 21,
              "name": "水稻推荐",
              "path": "rice_recommend",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 22,
              "name": "各省不同农产品价格变化",
              "path": "plot1",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 23,
              "name": "不同农产品的价格对比",
              "path": "plot2",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 24,
              "name": "各农产品产地数量饼图",
              "path": "plot3",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 25,
              "name": "各省份蔬菜数量柱状图",
              "path": "plot4",
              "icon": "el-icon-s-data",
              "children": []
            },
          ]
        },

        {
          "id": 3,
          "name": "农产品价格预测",
          "path": "",
          "icon": "el-icon-menu",
          "children": [

            {
              "id": 31,
              "name": "农产品价格趋势",
              "path": "plot5",
              "icon": "el-icon-s-data",
              "children": []
            },
            {
              "id": 32,
              "name": "农产品价格预测",
              "path": "predict",
              "icon": "el-icon-s-data",
              "children": []
            },
          ]
        },
      ]
    },
    handleCommand(command) {
      if (command === 'logout') {
        this.$message({
          message: '注销成功!',
          type: 'success',
          showClose: true,
        });
        Cookies.remove('user')
        this.$router.push('/login')
      } else if (command === 'profile') {
        this.$router.push('/profile')
      }
    },
  }
}
</script>

<style scoped lang="scss">
#home {
  height: 100vh; /* 设置高度为视口高度 */
  width: 100%;

  .el-aside {
    height: 100%;

    .title {
      color: rgba(255, 255, 255, 0.99);
      font-size: 14px;
      height: 50px;
      line-height: 50px;
      text-align: center;

      img {
        height: 30px;
        width: 30px;
        border-radius: 25%;
        padding: 15px;
      }
    }

    .el-menu {
      border-right: none !important;
    }
  }

  .el-header {
    background-color: #FFFFFF;
    width: 100%;
    display: flex;
    align-items: center;

    i {
      cursor: pointer;
      color: #74B8FD;
    }

    .el-breadcrumb {
      margin-left: 50px;
    }

    .user-info {
      position: absolute;
      right: 0px;
      width: 400px;

      .el-dropdown {
        display: flex;
        justify-content: right;
        align-items: center;
        margin-right: 20px;
      }
    }
  }

  .el-main {
    background-color: #FFFFFF;
    margin: 5px 5px 5px 5px;
    border-radius: 5px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    min-height: 500px;
    padding: 10px;
  }
}
</style>