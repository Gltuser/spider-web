var ec_l1 = echarts.init(document.getElementById('l1'),'dark');
l1_option = {
    title: {
        text: '疫情趋势图'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['累计确诊','现有疑似','累计治愈','死亡','现有确诊','现有重症'],
		left: "25%"
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
            name: '累计确诊',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '现有疑似',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '累计治愈',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '死亡',
            type: 'line',
            // stack: '总量',
            data: []
        },
        {
            name: '现有确诊',
            type: 'line',
            // stack: '总量',
            data: []
        },
		{
		    name: '现有重症',
		    type: 'line',
		    // stack: '总量',
		    data: []
		}
    ]
};
ec_l1.setOption(l1_option)