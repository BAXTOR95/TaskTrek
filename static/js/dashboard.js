const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');
const sidebarToggle = document.getElementById('sidebarToggle');

sidebarToggle.addEventListener('click', function () {
	sidebar.classList.toggle('collapsed');
	if (window.innerWidth > 768) {
		// On desktops, adjust content margin when sidebar toggled
		if (sidebar.classList.contains('collapsed')) {
			content.style.marginLeft = '80px';
		} else {
			content.style.marginLeft = '250px';
		}
	} else {
		// On mobile, overlay sidebar on top of content
		if (sidebar.classList.contains('collapsed')) {
			sidebar.style.visibility = 'visible';
		} else {
			sidebar.style.visibility = 'hidden';
		}
	}
});

// Collapse sidebar on window resize if on mobile
window.addEventListener('resize', function () {
	if (window.innerWidth <= 768) {
		sidebar.classList.add('collapsed');
		content.style.marginLeft = '0';
		sidebar.style.visibility = 'hidden';
	} else {
		sidebar.classList.remove('collapsed');
		content.style.marginLeft = '250px';
		sidebar.style.visibility = 'visible';
	}
});
