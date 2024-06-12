# TaskTrek

This repository contains the code for a Kanban To-Do List application built with Flask. This project allows users to create, manage, and organize tasks within projects through a web interface that supports task statuses and drag-and-drop capabilities.

## Live Version

A live version of TaskTrek is available at the following link: [https://tasktrek-mwg0.onrender.com](https://tasktrek-mwg0.onrender.com).

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication (register, login, logout)
- Project Management (create, update, delete)
- Task Management within projects with statuses:
  - TO-DO
  - IN PROGRESS
  - DONE
  - ARCHIVED
- Drag-and-Drop functionality to update task status
- Responsive design for mobile and desktop usage

## Technologies Used

- **Flask**: Web framework for building the backend.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database for storing user, project, and task data.
- **JavaScript**: For handling drag-and-drop functionality and AJAX calls.
- **Bootstrap**: For responsive design and styling components.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need to have the following installed to run the application locally:

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/BAXTOR95/TaskTrek.git
    cd TaskTrek
    ```

2. **Set up a virtual environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**

    Create a `.env` file in the root directory and update it with your variables:

    ```plaintext
    FLASK_APP=run.py
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///data.db
    UNSPLASH_ACCESS_KEY=your_secret_unsplash_api_key
    PROD=False
    ```

5. **Initialize the database**

    ```bash
    flask db upgrade
    ```

6. **Run the application**

    ```bash
    flask run
    ```

The application will be available at `http://127.0.0.1:5000`.

## Usage

After running the server, you can:

- Register a new user account.
- Log in using the user credentials.
- Create new projects and tasks.
- Move tasks across different statuses via drag-and-drop.
- Edit or delete projects as needed.
- Edit or delete tasks as needed.

## Contributing

Contributions are welcome, and any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

Brian Arriaga - [@BAXTOR95](https://twitter.com/BAXTOR95) - <brian.arriaga@gmail.com>

Project Link: [https://github.com/BAXTOR95/TaskTrek](https://github.com/BAXTOR95/TaskTrek)
