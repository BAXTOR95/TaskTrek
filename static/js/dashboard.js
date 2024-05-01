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

if (document.getElementById('submitForm')) {
	document.addEventListener('DOMContentLoaded', function () {
		var submitButton = document.getElementById('submitForm');
		submitButton.addEventListener('click', function () {
			if (document.getElementById('projectForm')) {
				var form = document.getElementById('projectForm');
				form.submit(); // Trigger form submission
			}
			if (document.getElementById('taskForm')) {
				var form = document.getElementById('taskForm');
				form.submit(); // Trigger form submission
			}
		});
	});
}

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

document.addEventListener('DOMContentLoaded', function() {
    const columns = document.querySelectorAll('.task-column');

    columns.forEach(column => {
        column.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
        });

        column.addEventListener('drop', (e) => {
            e.preventDefault();
            const taskId = e.dataTransfer.getData('text/plain');
            const task = document.getElementById(taskId);
			const url = task.getAttribute('data-url');
			const newStatus = column.getAttribute('data-status');
            column.appendChild(task);
            updateTaskStatus(url, newStatus);
        });
    });

    document.querySelectorAll('.card').forEach(task => {
        task.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', task.id);
        });
    });
});

// Function to send a request to update the task's status
function updateTaskStatus(url, newStatus) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('input[name="csrf_token"]').value
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            console.error('Failed to update task status:', data.message);
            alert('Failed to update task status.');
        }
    })
    .catch(error => {
        console.error('Error updating task status:', error);
        alert('Error updating task status.');
    });
}