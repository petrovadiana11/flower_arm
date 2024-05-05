
$(function() {
		var pathname_url = window.location.pathname;
		var href_url = window.location.href;

		$(".menu li").each(function () {

			var link = $(this).find("a").attr("href");

			if(pathname_url == link || href_url == link) {

				$(this).addClass("active");
			}
		});

	});


$(function() {
		var pathname_url = window.location.pathname;
		var href_url = window.location.href;

		$(".but-n li").each(function () {

			var link = $(this).find("a").attr("href");

			if(pathname_url == link || href_url == link) {

				$(this).addClass("active");
			}
		});

	});