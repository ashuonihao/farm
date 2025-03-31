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
        <span>未来7天价格预测</span>
      </div>
      <div class="clearfix">
        <div id="main" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>

  </div>
</template>

<script>
import {get_all_product, get_sheng_productList, product_predict} from "@/api/api";

export default {
  name: "rice_list",
  data() {
    return {
      kind_list: ['广东', '广西', '河南', '海南', '湖北', '湖南'],
      // 搜索表单
      formInline: {
        p1: '', //冬瓜
        kind: '',
      },
      // 类别数据
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
      if (this.formInline.kind === '') {
        this.$message({
          type: "error",
          message: "请选择省份",
        })
        return
      }
      if (this.formInline.p1 === '') {
        this.$message({
          type: "error",
          message: "请选择产品",
        })
        return
      }
      const loading = this.$loading({
        lock: true,
        text: '正在预测中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      product_predict(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })
        loading.close();
        // 数据
        let legend = ['name1', 'name2'];
        let x_data = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        let series = [
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


        legend = res.legend
        x_data = res.x_data
        series = res.series



        // 指定图表的配置项和数据
        let myChart = this.$echarts.init(document.getElementById("main"));
        let option = {
          title: {
            text: `${this.formInline.kind}-${this.formInline.p1}未来7天价格预测`,
            left: 'center',
            textStyle: {
              color: 'black',
              fontSize: '20px',
            },
          },
          tooltip: {
            trigger: 'axis',
            formatter: function(params) {
              let result = params[0].name + '<br/>';
              params.forEach(item => {
                result += item.seriesName + ': ' + item.value + '元/kg<br/>';
              });
              return result;
            }
          },
          dataZoom: [
            {
              type: 'inside',
              start: 0,
              end: 100
            }, 
            {
              type: 'slider',
              start: 0,
              end: 100
            }
          ],
          xAxis: {
            type: 'category',
            data: x_data,
            name: '日期'
          },
          yAxis: {
            type: 'value',
            name: '价格(元/kg)',
            axisLabel: {
              formatter: '{value} 元'
            }
          },
          legend: {
            data: legend,
            top: '30px'
          },
          series: series
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);




      });


    },
  },

}
</script>

<style scoped lang="scss">

</style>
