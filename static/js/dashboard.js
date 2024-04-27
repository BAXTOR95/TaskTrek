(function () {
	'use strict';

	var fullHeight = function () {
		var elements = document.querySelectorAll('.js-fullheight');
		elements.forEach(function (element) {
			element.style.height = window.innerHeight + 'px';
		});

		window.addEventListener('resize', function () {
			elements.forEach(function (element) {
				element.style.height = window.innerHeight + 'px';
			});
		});
	};
	fullHeight();

	var sidebarCollapse = document.getElementById('sidebarCollapse');
	var sidebar = document.getElementById('sidebar');
	sidebarCollapse.addEventListener('click', function () {
		sidebar.classList.toggle('active');
	});
})();
