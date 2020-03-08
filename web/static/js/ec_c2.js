var map_Chart = echarts.init(document.getElementById('c2'),'dark');

map_option = {
    title: {
        text: '累计确诊人数',
        // subtext: '纯属虚构',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data:['iphone3','iphone4','iphone5']
    },
    visualMap: {
		show: true,
        x: 'left',
        y: 'bottom',
        textStyle:{
			fontsize: 8
		},          // 文本，默认为数值文本

		splitList:[{start:1,end:9},
				{start:10,end:99},
				{start:100,end:999},
				{start:1000,end:9999},
				{start:10000}],
		color:['#8A3310','#C64918','#E55825','#F2AD92','#F9DCD1'],
    },
    toolbox: {
        show: false,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            dataView: {readOnly: false},
            restore: {},
            saveAsImage: {}
        }
    },
    series: [
        {
            name: '累计确诊人数',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {normal: {show: false},
                emphasis: {show: true}
            },
            data:[]
        }
    ]
};


                    



                    