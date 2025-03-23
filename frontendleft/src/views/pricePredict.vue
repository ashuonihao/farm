<template>
  <div id="">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>卡片名称</span>
        <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
      </div>
      <div class="clearfix">
        <el-form :model="form" label-width="80px">
          <el-form-item label="电影名字">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="国家">
            <el-select v-model="form.region" placeholder="请选择国家">
              <el-option label="中国" value="1"></el-option>
              <el-option label="非中国" value="0"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="上架年份">
            <el-input type="number" v-model="form.year"></el-input>
          </el-form-item>
          <el-form-item label="时长">
            <el-input type="number" v-model="form.pianchang"></el-input>
          </el-form-item>
          <el-form-item type="number" label="评分">
            <el-input v-model="form.score"></el-input>
          </el-form-item>
          <el-form-item type="number" label="评分人数">
            <el-input v-model="form.comNum"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">预测</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-card>

  </div>

</template>

<script>
import {Movie_list, Movie_price} from "@/api/api";

export default {
  name: "pricePredict",
  data: function () {
    return {
      form: {
        name: '我爱中国',
        region: "1",
        year: 2023,
        pianchang: 120,
        score: 5,
        comNum: 10000000,
      }
    }
  },
  methods: {
    onSubmit() {
      this.get_movie_rice()
    },
    get_movie_rice() {
      Movie_price(this.form).then(res => {
        if (res.code == 200) {
          this.$message({
            type: "success",
            message: "获取数据成功,预测票房为："+res.data,
          })
        } else {
          this.$message({
            type: "error",
            message: "数据输入不正确",
          })
        }
      });
    },
  }

}
</script>

<style scoped lang="scss">

</style>