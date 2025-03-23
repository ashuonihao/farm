<template>
  <div id="profile">
    <el-tabs v-model="activeName">
      <el-tab-pane label="个人资料" name="info">
        <!--    表单    -->
        <el-form ref="Ref" :model="Form" :rules="Rules" label-width="100px" style="width: 80%">
          <el-form-item label="手机号" prop="tel">
            <el-input v-model="Form.tel" prefix-icon="el-icon-phone" placeholder="请输入手机号"></el-input>
          </el-form-item>
          <el-form-item label="用户名" prop="username">
            <el-input v-model="Form.username" prefix-icon="el-icon-user" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="sex">
            <el-radio v-model="Form.sex" label="男">男</el-radio>
            <el-radio v-model="Form.sex" label="女">女</el-radio>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="Btn">修改</el-button>
            <el-button type="danger" @click="resetForm">重置</el-button>
          </el-form-item>
        </el-form>

      </el-tab-pane>
      <el-tab-pane label="修改密码" name="password">
        <!--    表单    -->
        <el-form ref="PRef" :model="PForm" :rules="PRules" label-width="100px" style="width: 80%">
          <el-form-item label="旧密码" prop="oldpassword">
            <el-input v-model="PForm.oldpassword" type="password"  show-password  prefix-icon="el-icon-lock"  placeholder="请输入旧密码"></el-input>
          </el-form-item>
          <el-form-item label="新密码" prop="password">
            <el-input v-model="PForm.password" type="password" show-password prefix-icon="el-icon-lock" placeholder="请输入新密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="PBtn">修改</el-button>
            <el-button type="danger" @click="PresetForm">重置</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import {User_info,User_update,User_password} from "@/api/api";

export default {
  name: "Profile",
  data() {
    //3.配置自定义规则
    let validate_phone = (rule, value, callback) => {
      if (!value) {
        callback(new Error('手机号不能为空！'));
      }
      //使用正则表达式进行验证手机号码
      if (!/^1[3456789]\d{9}$/.test(value)) {
        callback(new Error('手机号不正确！'));
      }
      callback()
    };
    return {
      activeName: 'info',
      // 表单
      Form: {},
      // 验证规则
      Rules: {
        tel: [
          {required: true, message: '请输入手机号码', trigger: 'blur'},
          {min: 11, max: 11, message: '请输11位手机号码', trigger: 'blur'},
          {validator: validate_phone, trigger: 'blur'}
        ],
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 1, max: 11, message: '请输1-11位名字', trigger: 'blur'},
        ],
        sex: [
          {required: true, message: '请选择性别', trigger: 'blur'},
        ],
      },
      // 表单
      PForm: {
        oldpassword:"",
        password:""
      },
      // 验证规则
      PRules: {
        oldpassword: [
          {required: true, message: '请输入旧的密码', trigger: 'blur'},
          {min: 1, max: 11, message: '密码1-11位', trigger: 'blur'},
        ],
        password: [
          {required: true, message: '请输入新的密码', trigger: 'blur'},
          {min: 1, max: 11, message: '密码1-11位', trigger: 'blur'},
        ],
      },
    }
  },
  methods: {
    // 确定
    Btn() {
      //验证表单是否有效
      this.$refs.Ref.validate((valid) => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '输入不符合要求，请认真填写信息!',
            type: 'warning'
          });
          return
        }
        User_update(this.Form).then(res => {
          this.$message({
            message: '修改个人信息成功!',
            type: 'success',
            showClose: true,
          });
          // //  1 把登录成功的uid,username保存到sessionStorage中
          Cookies.set('user', JSON.stringify(res.data), {expires: 3})
        });

      })
    },
    // 重置登录表单
    resetForm() {
      this.$refs.Ref.resetFields()
    },

    // 确定
    PBtn() {
      //验证表单是否有效
      this.$refs.PRef.validate((valid) => {
        if (!valid) {
          this.$message({
            showClose: true,
            message: '输入不符合要求，请认真填写信息!',
            type: 'warning'
          });
          return
        }
        User_password(this.PForm).then(res => {

          if (res.code != 200){
            this.$message({
              message: '旧的密码不正确!',
              type: 'error',
              showClose: true,
            });
            return
          }
          this.$message({
            message: '修改密码成功!',
            type: 'success',
            showClose: true,
          });
          // //  1 把登录成功的uid,username保存到sessionStorage中
          Cookies.remove('user')
          this.$router.push("/login")
        });

      })
    },
    // 重置登录表单
    PresetForm() {
      this.$refs.PRef.resetFields()
    },
    // 获取用户信息
    get_userinfo() {
      User_info({}).then(res => {
        this.Form = res.data
      });
    },
  },
  created() {
    this.get_userinfo()
  }
}
</script>

<style scoped>

</style>
