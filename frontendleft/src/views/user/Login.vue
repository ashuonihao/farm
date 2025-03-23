<template>
  <div class="container">
    <el-row type="flex" justify="center" align="middle" style="height: 100%">
      <div class="login">
        <el-col :span="12" style="height: 100%">
          <el-row type="flex" justify="center" align="bottom" style="height: 50%">
            <div style="font-size: 70px;margin-bottom: 10px">欢迎进入</div>
          </el-row>
          <el-row type="flex" justify="center" align="top" style="height: 50%">
            <div style="font-size: 40px;margin-top: 10px">{{ title }}</div>
          </el-row>
        </el-col>
        <el-col :span="12" style="height: 100%;background: #FFFFFF">
          <el-row type="flex" justify="center" align="middle" style="height: 100%">
            <el-form ref="loginRef" :model="loginForm" :rules="loginRules" label-width="100px" style="width: 80%">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username" prefix-icon="el-icon-user" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input v-model="loginForm.password" type="password" show-password prefix-icon="el-icon-lock" placeholder="请输入密码"></el-input>
              </el-form-item>
              <el-form-item>
                <el-checkbox checked>3天免登录</el-checkbox>
                <div style="float: right">
                  <router-link :to="{ path:'/register' }">注册</router-link>
                </div>
              </el-form-item>
              <el-form-item style="text-align: center">
                <el-button type="primary" round @click="loginBtn" style="width: 100%">登录</el-button>
              </el-form-item>
            </el-form>
          </el-row>
        </el-col>
      </div>
    </el-row>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import {User_login} from "@/api/api";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      // 表单
      loginForm: {
        username: '',
        password: '',
      },
      // 验证规则
      loginRules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 3, max: 11, message: '密码长度在3-11之间', trigger: 'blur'}
        ]
      },
      title: process.env.VUE_APP_TITLE
    }
  },
  methods: {
    // 登录按钮
    loginBtn() {
      //验证表单是否有效
      this.$refs.loginRef.validate((valid) => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '输入不符合要求，请认真填写信息!',
            type: 'warning'
          });
          return
        }
        User_login(this.loginForm).then(res => {
          if (res.code != 200) {
            this.$message({
              showClose: true,
              message: '用户信息不正确，请检查!',
              type: 'error'
            });
            return
          }
          this.$message({
            message: '登录成功!',
            type: 'success',
            showClose: true,
          });
          Cookies.set('user', JSON.stringify(res.data), {expires: 3})
          Cookies.set('uid', res.data.id, {expires: 3})
          this.$router.push('/')
        });
      })
    },
    // 重置登录表单
    resetLoginForm() {
      this.$refs.loginRef.resetFields()
    }
  }
}
</script>

<style scoped>
.login {
  background: rgba(255, 255, 255, 0.68);
  height: 60%;
  width: 60%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
}

.container {
  background: url("~@/assets/images/loginBackImg.jpg");
  height: 100%;
  width: 100%;
}
</style>