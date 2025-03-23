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
        <div id="main" :style="{width: '100%', height: '600px'}"/>
      </div>
    </el-card>

  </div>
</template>

<script>
import { get_all_product, get_plot4} from "@/api/api";

export default {
  name: "rice_list",
  created() {

  },
  data() {
    return {
      // 搜索表单
      formInline: {
        kind: '',

      },
      kind_list: ['广东', '广西', '河南', '海南', '湖北', '湖南'],
    }
  },
  methods: {


    // 提交搜索表单
    onSubmit() {
      if (this.formInline.kind == '') {
        this.$message({
          type: "error",
          message: "请选择省",
        })
        return
      }
      get_plot4(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })

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
  },

}
</script>

<style scoped lang="scss">

</style>
