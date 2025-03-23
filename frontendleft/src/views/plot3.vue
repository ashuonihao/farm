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
import { get_all_product, get_plot3} from "@/api/api";

export default {
  name: "rice_list",
  created() {
    this.get_data()
  },
  data() {
    return {
      // 搜索表单
      formInline: {
        p1: '冬瓜',
      },
      // 类别数据
      data_list: [],
    }
  },
  methods: {

    // 改变
    get_data() {
      get_all_product({}).then(res => {
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
      get_plot3(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })

        // 数据
        let data = [
          {'value': 1048, 'name': 'Search Engine'},
          {'value': 735, 'name': 'Direct'},
          {'value': 580, 'name': 'Email'},
          {'value': 484, 'name': 'Union Ads'},
          {'value': 300, 'name': 'Video Ads'}
        ]
        data = res.data



        // 指定图表的配置项和数据
        let myChart = this.$echarts.init(document.getElementById("main"));
        let   option = {
          tooltip: {
            trigger: 'item'
          },
          legend: {
            top: '5%',
            left: 'center'
          },
          series: [
            {
              name: '',
              type: 'pie',
              radius: ['40%', '70%'],
              // 是否玫瑰图
              //roseType: 'area',
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
              },
              label: {
                show: false,
                position: 'center'
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: 40,
                  fontWeight: 'bold'
                }
              },
              labelLine: {
                show: false
              },
              data: data
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
