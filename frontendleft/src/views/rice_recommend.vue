<template>
  <div id="welcome">
    <!--    数据筛选-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>推荐选择</span>
      </div>
      <div class="clearfix">
        <el-col :span="24">
          <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item label="省份">
              <el-select v-model="formInline.kind" placeholder="省份">
                <el-option v-for="kind in kind_list" :label="kind" :value="kind"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="属性">
              <el-select v-model="formInline.type" placeholder="省份">
                <el-option v-for="kind in type_list" :label="kind" :value="kind"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </div>

    </el-card>

    <!--    可视化-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>数据可视化</span>
      </div>
      <div class="clearfix">
        <div id="main" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>
  </div>
</template>

<script>
import {get_rice_recommed} from "@/api/api";

export default {
  name: "rice_list",
  created() {
    this.get_data()
  },
  data() {
    return {
      // 搜索表单
      formInline: {
        kind: '河南',
        type: '类型'
      },
      // 类别数据
      kind_list: [],
      type_list: ['类型', '母本', '审定公司']
    }
  },
  methods: {
    // 获取数据
    get_data() {
      get_rice_recommed(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })
        this.kind_list = res.kind_list
        var x_data = res.x_data
        var y_data = res.y_data
        console.log(x_data)
        console.log(y_data)
        // 基于准备好的dom，初始化echarts实例  这个和上面的main对应
        let myChart = this.$echarts.init(document.getElementById("main"));
        // 指定图表的配置项和数据
        let option = {
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          tooltip: {
            trigger: 'axis'
          },
          xAxis: {
            type: 'category',
            data: x_data
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name: '个数',
              data: y_data,
              type: 'bar',
              smooth: true
            }
          ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
      });
    },
    // 提交搜索表单
    onSubmit() {
      this.get_data()
    },
  },

}
</script>

<style scoped lang="scss">

</style>
