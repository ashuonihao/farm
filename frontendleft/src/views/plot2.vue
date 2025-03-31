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
import { get_all_product, get_plot2 } from "@/api/api";

export default {
  name: "rice_list",
  created() {
    this.get_data();
  },
  data() {
    return {
      // 搜索表单
      formInline: {
        p1: "",
        p2: "",
      },
      // 类别数据
      data_list: [],
    };
  },
  methods: {
    // 改变
    get_data() {
      get_all_product({}).then((res) => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        });
        this.data_list = res.data_list;
      });
    },
    // 提交搜索表单
    onSubmit() {
      if (this.formInline.p1 === "" || this.formInline.p2 === "") {
        this.$message({
          type: "error",
          message: "请选择两个产品",
        });
        return;
      }
      if (this.formInline.p1 === this.formInline.p2) {
        this.$message({
          type: "error",
          message: "请选择不同产品",
        });
        return;
      }
      get_plot2(this.formInline).then((res) => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        });

        // 处理最高价格图表（main1）
        const chartDom1 = document.getElementById("main1");
        let myChart1 = this.$echarts.getInstanceByDom(chartDom1);
        if (myChart1) {
          myChart1.dispose();
        }
        myChart1 = this.$echarts.init(chartDom1);
        const option1 = {
          title: {
            text: "",
            left: "center",
            textStyle: {
              color: "black",
              fontSize: "30px",
            },
          },
          tooltip: {
            trigger: "axis",
          },
          dataZoom: [{ type: "inside" }, { type: "slider" }],
          xAxis: {
            type: "category",
            data: res.x_data,
          },
          yAxis: {
            type: "value",
          },
          legend: {
            data: res.legend,
          },
          series: res.series.max, // 假设 max 对应最高价格数据
        };
        myChart1.setOption(option1);

        // 处理最低价格图表（main2）
        const chartDom2 = document.getElementById("main2");
        let myChart2 = this.$echarts.getInstanceByDom(chartDom2);
        if (myChart2) {
          myChart2.dispose();
        }
        myChart2 = this.$echarts.init(chartDom2);
        const option2 = {
          title: {
            text: "",
            left: "center",
            textStyle: {
              color: "black",
              fontSize: "30px",
            },
          },
          tooltip: {
            trigger: "axis",
          },
          dataZoom: [{ type: "inside" }, { type: "slider" }],
          xAxis: {
            type: "category",
            data: res.x_data,
          },
          yAxis: {
            type: "value",
          },
          legend: {
            data: res.legend,
          },
          series: res.series.min, // 假设 min 对应最低价格数据
        };
        myChart2.setOption(option2);

        // 处理平均价格图表（main3）
        const chartDom3 = document.getElementById("main3");
        let myChart3 = this.$echarts.getInstanceByDom(chartDom3);
        if (myChart3) {
          myChart3.dispose();
        }
        myChart3 = this.$echarts.init(chartDom3);
        const option3 = {
          title: {
            text: "",
            left: "center",
            textStyle: {
              color: "black",
              fontSize: "30px",
            },
          },
          tooltip: {
            trigger: "axis",
          },
          dataZoom: [{ type: "inside" }, { type: "slider" }],
          xAxis: {
            type: "category",
            data: res.x_data,
          },
          yAxis: {
            type: "value",
          },
          legend: {
            data: res.legend,
          },
          series: res.series.avg, // 假设 avg 对应平均价格数据
        };
        myChart3.setOption(option3);
      });
    },
  },
};
</script>

<style scoped lang="scss">
</style>