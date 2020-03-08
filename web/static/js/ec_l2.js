var ec_l2 = echarts.init(document.getElementById('l2'),'dark');
l2_option = {
    title: {
        text: '新增疫情趋势图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: [ '新增确诊', '新增疑似','新增治愈','新增死亡'],
		left: "50%"
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '新增确诊',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '新增疑似',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '新增治愈',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '新增死亡',
            type: 'line',
            // stack: '总量',
            data: []
        }
       
    ]
};
ec_l2.setOption(l2_option)