import request from "@/api/request";
// 使用
// USER_LOGIN(params).then(res => {
// });

///////////////////////////////////////////
///  用户相关
///////////////////////////////////////////
// 登录
export function User_login (data) {
    // data 是json数据
    return request({
        url: '/api/login/',
        method: 'post',
        data
    })
}

// 注册
export function User_register (data) {
    // data 是json数据
    return request({
        url: '/api/register/',
        method: 'post',
        data
    })
}

export function User_info (data) {
    // data 是json数据
    return request({
        url: '/api/user/info',
        method: 'get',
        data
    })
}
export function User_update (data) {
    // data 是json数据
    return request({
        url: '/api/user/update',
        method: 'post',
        data
    })
}

export function User_password (data) {
    // data 是json数据
    return request({
        url: '/api/user/password',
        method: 'post',
        data
    })
}

export function get_rice_list (data) {
    // data 是json数据
    return request({
        url: '/api/get_rice_list',
        method: 'get',
        params:data
    })
}
export function get_products_list (data) {
    // data 是json数据
    return request({
        url: '/api/get_products_list',
        method: 'get',
        params:data
    })
}
export function get_rice_recommed (data) {
    // data 是json数据
    return request({
        url: '/api/get_rice_recommed',
        method: 'get',
        params:data
    })
}
export function get_sheng_productList (data) {
    // data 是json数据
    return request({
        url: '/api/get_sheng_productList',
        method: 'get',
        params:data
    })
}
export function get_plot1 (data) {
    // data 是json数据
    return request({
        url: '/api/get_plot1',
        method: 'get',
        params:data
    })
}

export function get_all_product (data) {
    // data 是json数据
    return request({
        url: '/api/get_all_product',
        method: 'get',
        params:data
    })
}
export function get_plot2 (data) {
    // data 是json数据
    return request({
        url: '/api/get_plot2',
        method: 'get',
        params:data
    })
}

export function get_plot3 (data) {
    // data 是json数据
    return request({
        url: '/api/get_plot3',
        method: 'get',
        params:data
    })
}
export function get_plot4 (data) {
    // data 是json数据
    return request({
        url: '/api/get_plot4',
        method: 'get',
        params:data
    })
}
export function get_plot5 (data) {
    // data 是json数据
    return request({
        url: '/api/get_plot5',
        method: 'get',
        params:data
    })
}
export function product_predict (data) {
    // data 是json数据
    return request({
        url: '/api/product_predict',
        method: 'get',
        params:data
    })
}

/////////////////////////////////////// 待删除
// 获取电影信息
export function Movie_list (data) {
    // data 是json数据
    return request({
        url: '/api/movie/list',
        method: 'post',
        data
    })
}

export function Movie_star (data) {
    // data 是json数据
    return request({
        url: '/api/movie/star',
        method: 'post',
        data
    })
}
// 获取收藏电影信息
export function Movie_star_list (data) {
    // data 是json数据
    return request({
        url: '/api/movie/starlist',
        method: 'post',
        data
    })
}
//
export function Star_plot (data) {
    // data 是json数据
    return request({
        url: '/api/star/plot',
        method: 'get',
        data
    })
}


export function PlotData9 (data) {
    // data 是json数据
    return request({
        url: '/api/plot9',
        method: 'get',
        data
    })
}
export function History (data) {
    // data 是json数据
    return request({
        url: '/api/history',
        method: 'post',
        data
    })
}



export function Tuijian_item (data) {
    // data 是json数据
    return request({
        url: '/api/tuijian/item',
        method: 'post',
        data
    })
}

export function Movie_info (data) {
    // data 是json数据
    return request({
        url: '/api/movie/info',
        method: 'post',
        data
    })
}

export function Movie_price (data) {
    // data 是json数据
    return request({
        url: '/api/movie/price',
        method: 'post',
        data
    })
}
export function PlotData (data) {
    // data 是json数据
    return request({
        url: '/api/plotData',
        method: 'get',
        data
    })
}
