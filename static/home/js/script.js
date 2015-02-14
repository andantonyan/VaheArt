$( document ).ready(function() {
	$.ajax({
		url: '/ajax/galery',
		dataType: 'json',
	})
	.done(function(data) {
		console.log(data)
		$(".galery").elastic_grid({
			items: data
		})
	})

	$("html,body").animate({scrollTop: 0}, 200);
})