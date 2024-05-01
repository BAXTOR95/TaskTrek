if (document.getElementById('flash-message')) {
	window.setTimeout(function () {
		let alerts = document.querySelectorAll('.alert');
		alerts.forEach((alert) => {
			fadeOutAndSlideUp(alert, 500);
		});
	}, 5000);
}

function fadeOutAndSlideUp(element, duration) {
	element.style.transition = `opacity ${duration}ms, height ${duration}ms, margin ${duration}ms, padding ${duration}ms`;
	element.style.height = `${element.offsetHeight}px`; // Set initial height to prevent collapse during transition
	element.style.opacity = '0';

	setTimeout(() => {
		element.style.height = '0';
		element.style.marginTop = '0';
		element.style.marginBottom = '0';
		element.style.paddingTop = '0';
		element.style.paddingBottom = '0';

		setTimeout(() => {
			element.remove();
		}, duration);
	}, duration);
}
