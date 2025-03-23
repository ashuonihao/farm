<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  }
}
</script>

<style lang="scss">
// 引用 静态文件
@import "~@/assets/style/global.scss";
@import "~@/assets/style/element-ui.scss";
#app {
}
</style>
