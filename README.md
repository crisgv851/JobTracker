# JobTracker

JobTracker is a Python application for managing and tracking job applications.

The application allows users to register job opportunities, search for applications, update their status, and remove records. Data is persisted locally using a JSON file.

## Features

- Create job applications
- List registered jobs
- Search jobs by company and position
- Update application status
- Delete job applications
- Persist data using JSON
- Validate job statuses
- Handle invalid or missing JSON files
- Prevent duplicate job applications
- Automated tests with pytest

## Technologies

- Python 3.11+
- JSON
- pytest
- Git
- GitHub

## Project Structure

```text
JobTracker/
│
├── data/
│   └── jobs.json
│
├── src/
│   ├── __init__.py
│   ├── job_manager.py
│   ├── main.py
│   ├── models.py
│   └── storage.py
│
├── tests/
│   ├── test_job_manager.py
│   ├── test_models.py
│   └── test_storage.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/crisgv851/JobTracker.git
```

### 2. Move into the project directory

```bash
cd JobTracker
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Application

Start JobTracker with:

```bash
python -m src.main
```

The application provides the following menu:

```text
Job Tracker =)

1. Ver Trabajos
2. Agregar Trabajo
3. Buscar Trabajo
4. Actualizar Estado de Trabajo
5. Eliminar Trabajo
6. Salir
```

## Job Statuses

The application currently supports the following job application statuses:

- Applied
- Technical Assessment
- HR Interview
- Technical Interview
- Offer
- Hired
- Rejected

## Running Tests

Run the complete test suite with:

```bash
python -m pytest
```

The project currently contains **12 automated tests** covering the main functionality.

Tests include:

- Job creation
- Job status validation
- Job status changes
- Job searching
- Duplicate job prevention
- Job deletion
- JSON loading
- Missing JSON files
- Invalid JSON files
- JSON structure validation

Current result:

```text
============================= test session starts =============================

collected 12 items

tests/test_job_manager.py .....                                    [ 41%]
tests/test_models.py ...                                           [ 66%]
tests/test_storage.py ....                                         [100%]

============================== 12 passed ==============================
```

## Architecture

The project separates responsibilities into different modules.

### `models.py`

Contains the `Job` class, which represents a job application.

It is responsible for:

- Storing job information
- Validating job statuses
- Changing job statuses
- Converting jobs to dictionaries
- Creating jobs from dictionaries

### `job_manager.py`

Contains the `JobManager` class.

It is responsible for:

- Adding jobs
- Searching jobs
- Updating job statuses
- Removing jobs
- Loading jobs
- Saving changes

### `storage.py`

Handles JSON persistence.

It is responsible for:

- Reading JSON data
- Saving JSON data
- Handling missing files
- Handling invalid JSON
- Validating the JSON structure

### `main.py`

Contains the command-line interface.

It is responsible for:

- Displaying the menu
- Reading user input
- Calling the appropriate `JobManager` operations
- Displaying results and errors

## Data Persistence

JobTracker stores job applications locally in:

```text
data/jobs.json
```

Example:

```json
[
    {
        "company": "Microsoft",
        "position": "Python Developer",
        "status": "Technical Interview",
        "technologies": [
            "Python",
            "Django"
        ],
        "application_date": "2026-09-17",
        "notes": "Backend position"
    }
]
```

## Development Practices

This project follows several software development practices:

- Object-oriented programming
- Separation of responsibilities
- Automated testing
- Input validation
- Error handling
- JSON persistence
- Git version control
- Conventional commit messages
- Semantic versioning
- Modular project structure

## Git Workflow

The project uses Git for version control.

Commit messages follow a conventional format such as:

```text
feat: add new functionality
fix: fix application error
test: add automated tests
refactor: improve code structure
docs: improve documentation
chore: update project configuration
```

## Versioning

The project follows Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Current version:

```text
v0.2.0
```

### Versions

#### v0.1.0

Initial functional version of JobTracker.

Included:

- Job creation
- Job searching
- Status updates
- Job deletion
- JSON persistence

#### v0.2.0

Improved storage reliability and automated testing.

Included:

- JSON validation
- Invalid JSON handling
- Missing file handling
- JSON structure validation
- Automated tests
- Storage tests
- 12 tests passing

## Roadmap

Planned improvements for future versions:

- [ ] Filter jobs by status
- [ ] Sort applications by date
- [ ] Improve input validation
- [ ] Add better error messages
- [ ] Add database persistence
- [ ] Create a REST API
- [ ] Create a web interface
- [ ] Add authentication
- [ ] Add automated CI/CD
- [ ] Improve application architecture

## Author

**Cristian Gonzalez**

GitHub:  
https://github.com/crisgv851/JobTracker