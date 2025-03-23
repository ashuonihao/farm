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
            <el-form-item label="关键词">
              <el-input v-model="formInline.name" placeholder="关键词"></el-input>
            </el-form-item>
            <el-form-item label="省份">
              <el-select v-model="formInline.kind" placeholder="省份">
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

    <!--    数据表格-->
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>水稻数据列表</span>
      </div>

      <div class="clearfix">
        <el-table
            :data="data_list"
            style="width: 100%"
        >
          <el-table-column
              prop="sheng"
              label="省份"
              width="180">
          </el-table-column>
          <el-table-column
              prop="pzlx"
              label="品种名称"
              width="180">
          </el-table-column>
          <el-table-column
              prop="qbly"
              label="亲本来源">
          </el-table-column>
          <el-table-column
              prop="lx"
              label="类型">
          </el-table-column>
          <el-table-column
              prop="ycd"
              label="原产地">
          </el-table-column>
          <el-table-column
              prop="sdbh"
              label="审定编号">
          </el-table-column>
          <el-table-column
              prop="sdf"
              label="审定方">
          </el-table-column>
          <el-table-column
              prop="sdxh"
              label="审定序号">
          </el-table-column>
          <el-table-column
              prop="mb"
              label="母本">
          </el-table-column>
          <el-table-column
              prop="sdgs"
              label="审定公司">
          </el-table-column>
          <el-table-column
              prop="recordDate"
              label="发布日期">
          </el-table-column>
        </el-table>

      </div>

    </el-card>
    <!--    分页-->
    <el-pagination
        style="text-align: center"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="formInline.pageNum"
        :page-sizes="[20, 40, 60]"
        :page-size="formInline.pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total" class="bottom">
    </el-pagination>
  </div>
</template>

<script>
import {get_rice_list} from "@/api/api";

export default {
  name: "rice_list",
  created() {
    this.get_table_data()
  },
  data() {
    return {
      // 搜索表单
      formInline: {
        name: '',
        kind: '',
        pageSize: 20,
        pagenum: 1,
      },
      // 数据列表
      data_list: [
        {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }],
      // 类别数据
      kind_list: [],
      //总数
      total: 0,
    }
  },
  methods: {
    // 获取数据
    get_table_data() {
      get_rice_list(this.formInline).then(res => {
        this.$message({
          type: "success",
          message: "获取数据成功",
        })
        this.data_list = res.data_list
        this.kind_list = res.kind_list
        this.total = res.total
      });
    },
    // pagesize改变
    handleSizeChange(newsize) {
      this.formInline.pageSize = newsize
      this.get_table_data()
    },
    // pagenum改变
    handleCurrentChange(pagenum) {
      this.formInline.pagenum = pagenum
      this.get_table_data()
    },
    // 提交搜索表单
    onSubmit() {
      this.get_table_data()
    },
  },

}
</script>

<style scoped lang="scss">

</style>
