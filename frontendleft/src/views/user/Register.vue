<template>
  <div class="container">
    <el-row type="flex" justify="center" align="middle" style="height: 100%">
      <div class="login">
        <el-col :span="12" style="height: 100%">
          <el-row type="flex" justify="center" align="bottom" style="height: 50%">
            <div class="welcome-text">欢迎进入</div>
          </el-row>
          <el-row type="flex" justify="center" align="top" style="height: 50%">
            <div class="title-text">{{ title }}</div>
          </el-row>
        </el-col>
        <el-col :span="12" style="height: 100%;background: #FFFFFF; border-radius: 10px; padding: 20px;">
          <el-row type="flex" justify="center" align="middle" style="height: 100%">
            <el-form ref="loginRef" :model="loginForm" :rules="loginRules" label-width="100px" style="width: 80%">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username" prefix-icon="el-icon-user" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input v-model="loginForm.password" type="password" show-password prefix-icon="el-icon-lock" placeholder="请输入密码"></el-input>
              </el-form-item>
              <el-form-item>
                <div style="float: right">
                  <router-link :to="{ path:'/login' }">登录</router-link>
                </div>
              </el-form-item>
              <el-form-item style="text-align: center">
                <el-button type="primary" round @click="loginBtn" style="width: 100%; transition: background-color 0.3s ease;">注册</el-button>
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
import { User_register } from "@/api/api";

export default {
  name: "Register",
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
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 11, message: '用户名长度在3 - 11之间', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 3, max: 11, message: '密码长度在3 - 11之间', trigger: 'blur' },
        ],
      },
      title: process.env.VUE_APP_TITLE
    };
  },
  methods: {
    // 注册按钮
    loginBtn() {
      this.$refs.loginRef.validate((valid) => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '输入不符合要求，请认真填写信息!',
            type: 'warning',
          });
          return;
        }
        User_register(this.loginForm).then((res) => {
          if (res.code != 200) {
            this.$message({
              showClose: true,
              message: '该用户名已经注册，请修改!',
              type: 'error',
            });
            return;
          }
          this.$message({
            message: '注册成功!',
            type: 'success',
            showClose: true,
          });
        });
      });
    },
    // 重置注册表单
    resetRegisterForm() {
      this.$refs.loginRef.resetFields();
    }
  }
};
</script>

<style scoped>
.login {
  background: rgba(255, 255, 255, 0.68);
  height: 70%;
  width: 70%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  border-radius: 10px;
  display: flex;
  overflow: hidden;
}

.container {
  background: linear-gradient(45deg, #1abc9c, #3498db, #9b59b6, #e74c3c);
  background-size: 400% 400%;
  height: 100vh;
  width: 100vw;
  animation: gradientAnimation 15s ease infinite;
}

@keyframes gradientAnimation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.welcome-text {
  font-size: 36px;
  margin-bottom: 10px;
  color: #ffffff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  font-family: "Microsoft YaHei", sans-serif;
  letter-spacing: 2px;
}

.title-text {
  font-size: 24px;
  margin-top: 10px;
  color: #ffffff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  font-family: "Microsoft YaHei", sans-serif;
  letter-spacing: 1px;
}

.el-button[type="primary"]:hover {
  background-color: #2980b9;
}
</style>