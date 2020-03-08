function gettime(){
	$.ajax({
		url:"/time",
		timeout:10000,
		success:function(data) {
			$("#time").html(data)
		}
	});
}
function get_c1_data(){
	$.ajax({
		url:"/c1",
		success:function(data){
			$(".num").eq(0).text(data.confirm)
			$(".num").eq(1).text(data.heal)
			$(".num").eq(2).text(data.dead)
			$(".num").eq(3).text(data.nowConfirm)
			$(".num").eq(4).text(data.suspect)
			$(".num").eq(5).text(data.nowSevere)
		}
	})
}
function get_c2_data(){
	$.ajax({
		url:'/c2',
		success:function(d){
			map_option.series[0].data = d.data
			map_Chart.setOption(map_option)
		},
	})
	
}
function get_l1_data(){
	$.ajax({
		url:'l1',
		success:function(d){
			l1_option.xAxis.data = d.dt
			l1_option.series[0].data = d.confirm
			l1_option.series[1].data = d.suspect
			l1_option.series[2].data = d.heal
			l1_option.series[3].data = d.dead
			l1_option.series[4].data = d.now_confirm
			l1_option.series[5].data = d.now_severe
			ec_l1.setOption(l1_option)
		}
	})
}
function get_l2_data(){
	$.ajax({
		url:'l2',
		success:function(d){
			l2_option.xAxis.data = d.dt
			l2_option.series[0].data = d.confirm_add
			l2_option.series[1].data = d.suspect_add
			l2_option.series[2].data = d.heal_add
			l2_option.series[3].data = d.dead_add
			ec_l2.setOption(l2_option)
		}
	})
}
function get_r1_data(){
	$.ajax({
		url:'/r1',
		success:function(d){
			r1_option.xAxis[0].data = d.city
			r1_option.series[0].data = d.confirm
			ec_r1.setOption(r1_option)	
		}
	})
}
function get_r2_data(){
	$.ajax({
		url:'/r2',
		success:function(d){
			r2_option.series[0].data = d.data
			ec_r2.setOption(r2_option)
			
		}
	})
}
gettime()
get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()
setInterval(gettime,1000)
setInterval(get_c1_data,10000)
setInterval(get_c2_data,10000)
setInterval(get_l1_data,10000)
setInterval(get_l2_data,10000)
setInterval(get_r1_data,10000)
setInterval(get_r2_data,10000)

