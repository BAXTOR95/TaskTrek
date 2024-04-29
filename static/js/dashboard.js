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

document.addEventListener('DOMContentLoaded', function () {
	var submitButton = document.getElementById('submitForm');
	submitButton.addEventListener('click', function () {
		var form = document.getElementById('projectForm');
		form.submit(); // Trigger form submission
	});
});

if (document.getElementById('flash-message')) {
	window.setTimeout(function () {
		$('.alert')
			.fadeTo(500, 0)
			.slideUp(500, function () {
				$(this).remove();
			});
	}, 5000);
}

function redirectToProject(url) {
    window.location.href = url; // Redirect to the provided URL
}