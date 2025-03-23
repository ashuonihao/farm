// 设置 网页名字
export  function setAppTitle(titleText) {
    const processTitle = titleText || process.env.VUE_APP_TITLE
    window.document.title = `${processTitle}`
}
