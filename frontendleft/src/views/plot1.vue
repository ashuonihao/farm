<template>
  <div id="welcome">
    <!--    数据筛选-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>数据筛选</span>
      </div>
      <div class="clearfix">
        <el-col :span="24">
          <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item label="省份">
              <el-select v-model="formInline.kind" placeholder="省份" @change="change">
                <el-option v-for="kind in kind_list" :label="kind" :value="kind"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="产品1">
              <el-select v-model="formInline.p1" placeholder="产品1">
                <el-option v-for="kind in data_list" :label="kind" :value="kind"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="产品2">
              <el-select v-model="formInline.p2" placeholder="产品2">
                <el-option v-for="kind in data_list" :label="kind" :value="kind"></el-option>
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
        <span>最高价格</span>
      </div>
      <div class="clearfix">
        <div id="main1" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>
    <!--    可视化-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>最低价格</span>
      </div>
      <div class="clearfix">
        <div id="main2" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>
    <!--    平均价格-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>平均价格</span>
      </div>
      <div class="clearfix">
        <div id="main3" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>
  </div>
</template>

<script>
import {get_plot1, get_sheng_productList,} from "@/api/api";

export default {
  name: "rice_list",
  created() {
  },
  data() {
    return {
      // 搜索表单
      formInline: {
        kind: '',
        p1: '',
        p2: '',
      },
      // 类别数据
      kind_list: ['广东', '广西', '河南', '海南', '湖北', '湖南'],
      data_list: [],
    }
  },
  methods: {

    // 改变
    change(value) {
      get_sheng_productList(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })
        this.data_list = res.data_list
      });
    },
    // 提交搜索表单
    onSubmit() {
      if (this.formInline.p1 == '' || this.formInline.p2 == '') {
        this.$message({
          type: "error",
          message: "请选择两个产品",
        })
        return
      }
      if (this.formInline.p1 == this.formInline.p2) {
        this.$message({
          type: "error",
          message: "请选择不同产品",
        })
        return
      }
      get_plot1(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })

        // 数据
        let legend = ['name1', 'name2'];
        let x_data = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        let series1 = [
          {
            'name': 'name1',
            'data': [150, 230, 224, 218, 135, 147, 260],
            'type': 'line'
          },
          {
            'name': 'name2',
            'data': [22, 100, 124, 118, 35, 47, 160],
            'type': 'line'
          }
        ]
        let series2 = series1
        let series3 = series1

        legend = res.legend
        x_data = res.x_data
        series1 = res.series1
        series2 = res.series2
        series3 = res.series3


        // 指定图表的配置项和数据
        let myChart1 = this.$echarts.init(document.getElementById("main1"));
        let option1 = {
          //标题
          title: {
            text: '',
            left: 'center',
            textStyle: { //设置主标题风格
              color: 'black',//设置主标题字体颜色
              fontSize: '30px',
            },
          },
          //提示
          tooltip: {
            trigger: 'axis',
            //trigger: 'item',
          },
          // 伸缩
          dataZoom: [{type: 'inside'}, {type: 'slider'}],
          xAxis: {
            type: 'category',
            data: x_data,
          },
          yAxis: {
            type: 'value'
          },
          legend: {
            data: legend
          },
          series: series1
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart1.setOption(option1);

        // 指定图表的配置项和数据
        let myChart2 = this.$echarts.init(document.getElementById("main2"));
        let option2 = {
          //标题
          title: {
            text: '',
            left: 'center',
            textStyle: { //设置主标题风格
              color: 'black',//设置主标题字体颜色
              fontSize: '30px',
            },
          },
          //提示
          tooltip: {
            trigger: 'axis',
            //trigger: 'item',
          },
          // 伸缩
          dataZoom: [{type: 'inside'}, {type: 'slider'}],
          xAxis: {
            type: 'category',
            data: x_data,
          },
          yAxis: {
            type: 'value'
          },
          legend: {
            data: legend
          },
          series: series2
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart2.setOption(option2);

        // 指定图表的配置项和数据
        let myChart3 = this.$echarts.init(document.getElementById("main3"));
        let option3 = {
          //标题
          title: {
            text: '',
            left: 'center',
            textStyle: { //设置主标题风格
              color: 'black',//设置主标题字体颜色
              fontSize: '30px',
            },
          },
          //提示
          tooltip: {
            trigger: 'axis',
            //trigger: 'item',
          },
          // 伸缩
          dataZoom: [{type: 'inside'}, {type: 'slider'}],
          xAxis: {
            type: 'category',
            data: x_data,
          },
          yAxis: {
            type: 'value'
          },
          legend: {
            data: legend
          },
          series: series3
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart3.setOption(option3);
      });


    },
  },

}
</script>

<style scoped lang="scss">

</style>
