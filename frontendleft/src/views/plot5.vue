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
        <span>农产品价格预测</span>
      </div>
      <div class="clearfix">
        <div id="main" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>

  </div>
</template>

<script>
import { get_sheng_productList, get_plot5} from "@/api/api";

export default {
  name: "rice_list",
  created() {
    this.get_data()
  },
  mounted() {
    this.get_data()
  },
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
      if (this.formInline.p1 == '') {
        this.$message({
          type: "error",
          message: "请选择个产品",
        })
        return
      }
      const loading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      get_plot5(this.formInline).then(res => {
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
