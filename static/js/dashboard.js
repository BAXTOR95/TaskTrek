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

function redirectToProject(url) {
	window.location.href = url; // Redirect to the provided URL
}

document.addEventListener('DOMContentLoaded', function () {
	// Listen for click events on the document
	document.addEventListener('click', function (event) {
		// Check if the clicked element is a submit button
		if (event.target && event.target.classList.contains('submit-form')) {
			// Traverse up the DOM tree from the target to find its parent modal
			var parentModal = event.target.closest('.modal');

			// If a parent modal is found and it contains a form, submit that form
			if (parentModal) {
				var form = parentModal.querySelector('form');
				if (form) {
					form.submit();
				}
			}
		}
	});

	// Add event listeners for drag-and-drop functionality
	const columns = document.querySelectorAll('.task-column');

	columns.forEach((column) => {
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

	document.querySelectorAll('.card').forEach((task) => {
		task.addEventListener('dragstart', (e) => {
			e.dataTransfer.setData('text/plain', task.id);
		});
	});

	// Set form action for addProjectModal
	const addProjectModal = document.getElementById('addProjectModal');
	if (addProjectModal) {
		addProjectModal.addEventListener('show.bs.modal', function (event) {
			const button = event.relatedTarget; // Button that triggered the modal
			const url = button.getAttribute('data-bs-add-url');

			const form = addProjectModal.querySelector('form');
			form.action = url; // Update form action
		});
	}

	// Add event listeners for project edit buttons
	const editProjectModal = document.getElementById('editProjectModal');
	if (editProjectModal) {
		editProjectModal.addEventListener('show.bs.modal', function (event) {
			const button = event.relatedTarget; // Button that triggered the modal
			const url = button.getAttribute('data-bs-update-url');
			const projectTitle = button.getAttribute('data-bs-project-title');
			const projectDescription = button.getAttribute(
				'data-bs-project-description',
			);

			const modalTitle = editProjectModal.querySelector('.modal-title');
			const form = editProjectModal.querySelector('form');

			modalTitle.textContent = 'Edit Project: ' + projectTitle; // Update modal title
			form.action = url; // Update form action

			// Populate form fields
			form.querySelector('#projectTitle').value = projectTitle;
			form.querySelector('#projectDescription').value = projectDescription;
		});
	}

	// Add event listeners for task edit buttons
	const editTaskModal = document.getElementById('editTaskModal');
	if (editTaskModal) {
		editTaskModal.addEventListener('show.bs.modal', function (event) {
			const button = event.relatedTarget; // Button that triggered the modal
			const url = button.getAttribute('data-bs-update-url');
			const taskTitle = button.getAttribute('data-bs-task-title');
			const taskDescription = button.getAttribute('data-bs-task-description');
			const taskStatus = button.getAttribute('data-bs-task-status');
			const taskPriority = button.getAttribute('data-bs-task-priority');

			const modalTitle = editTaskModal.querySelector('.modal-title');
			const form = editTaskModal.querySelector('form');

			modalTitle.textContent = 'Edit Task: ' + taskTitle; // Update modal title
			form.action = url; // Update form action

			// Populate form fields
			form.querySelector('#taskTitle').value = taskTitle;
			form.querySelector('#taskDescription').value = taskDescription;
			form.querySelector('#taskStatus').value = taskStatus;
			form.querySelector('#taskPriority').value = taskPriority;
		});
	}

	// Set form action for addTaskModal
	const addTaskModal = document.getElementById('addTaskModal');
	if (addTaskModal) {
		addTaskModal.addEventListener('show.bs.modal', function (event) {
			const button = event.relatedTarget; // Button that triggered the modal
			const url = button.getAttribute('data-bs-add-url');

			const form = addTaskModal.querySelector('form');
			form.action = url; // Update form action
		});
	}
});

// Function to send a request to update the task's status
function updateTaskStatus(url, newStatus) {
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': document.querySelector('input[name="csrf_token"]').value,
		},
		body: JSON.stringify({ status: newStatus }),
	})
		.then((response) => response.json())
		.then((data) => {
			if (!data.success) {
				console.error('Failed to update task status:', data.message);
				alert('Failed to update task status.');
			}
		})
		.catch((error) => {
			console.error('Error updating task status:', error);
			alert('Error updating task status.');
		});
}
