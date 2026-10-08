# JobTracker

JobTracker is a Python application for managing and tracking job applications.

The application allows users to register job opportunities, search and filter applications, update their status, remove records, and view application statistics. Data is persisted locally using a JSON file.

The project was developed to practice Python, object-oriented programming, software design, data persistence, validation, automated testing, and Git version control.

## Features

- Create job applications
- List registered jobs
- Search jobs by company and position
- Search jobs by technology
- Filter jobs by application status
- Update application status
- Delete job applications
- View application statistics
- Calculate application success rate
- Persist data using JSON
- Validate company and position information
- Validate required technologies
- Validate application dates
- Validate job statuses
- Prevent duplicate job applications
- Handle missing JSON files
- Handle invalid JSON files
- Automated tests with pytest
- Case-insensitive searches

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
Job Tracker

1. Ver trabajos
2. Agregar trabajo
3. Buscar trabajo
4. Filtrar por estado
5. Buscar por tecnología
6. Actualizar estado
7. Eliminar trabajo
8. Ver estadísticas
9. Salir
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

## Job Information

Each job application contains the following information:

| Field | Description |
|---|---|
| Company | Company offering the position |
| Position | Job position |
| Status | Current application status |
| Technologies | Technologies required for the position |
| Application Date | Date when the application was submitted |
| Notes | Additional information about the application |

The application date must use the following format:

```text
YYYY-MM-DD
```

Example:

```text
2026-09-22
```

## Running Tests

Run the complete test suite with:

```bash
python -m pytest
```

The project currently contains **71 automated tests** covering the main components of the application.

Current test result:

```text
71 passed
```

The tests cover:

- Job creation
- Company validation
- Position validation
- Technology validation
- Application date validation
- Job status validation
- Job status changes
- Job serialization
- Job deserialization
- Job searching
- Case-insensitive searches
- Search by status
- Search by technology
- Duplicate job prevention
- Job deletion
- Job updates
- Job loading
- Job persistence
- Statistics
- Success rate calculation
- JSON loading
- Missing JSON files
- Invalid JSON files
- JSON structure validation
- Data persistence

## Architecture

The project separates responsibilities into different modules.

### `models.py`

Contains the `Job` class, which represents a job application.

It is responsible for:

- Storing job information
- Validating company information
- Validating position information
- Validating technologies
- Validating application dates
- Validating job statuses
- Changing job statuses
- Converting jobs to dictionaries
- Creating jobs from dictionaries

### `job_manager.py`

Contains the `JobManager` class.

It is responsible for the application's business logic, including:

- Adding jobs
- Searching jobs
- Searching jobs by status
- Searching jobs by technology
- Updating job statuses
- Removing jobs
- Loading jobs
- Saving changes
- Preventing duplicate applications
- Generating application statistics
- Calculating the success rate

### `storage.py`

Handles JSON persistence.

It is responsible for:

- Reading JSON data
- Saving JSON data
- Creating the data directory when necessary
- Handling missing files
- Handling invalid JSON
- Validating the JSON structure

### `main.py`

Contains the command-line interface.

It is responsible for:

- Displaying the menu
- Reading user input
- Calling the appropriate `JobManager` operations
- Displaying results
- Displaying validation errors

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

The JSON file is used as the application's local persistence layer.

## Statistics

JobTracker provides basic statistics about the registered applications.

The statistics include:

- Total number of applications
- Number of applications in each status
- Success rate

The current success rate is calculated using applications with the following statuses:

```text
Offer
Hired
```

The result is expressed as a percentage.

## Input Validation

The application validates user-provided data before storing it.

Examples include:

- Company cannot be empty.
- Position cannot be empty.
- Technologies must be provided as a list.
- Technologies cannot be empty.
- Technology values must be strings.
- Technology values cannot be empty.
- Application date must use `YYYY-MM-DD`.
- Status must be one of the supported statuses.
- Notes must be a string.
- Duplicate applications for the same company and position are prevented.

## Development Practices

This project follows several software development practices:

- Object-oriented programming
- Separation of responsibilities
- Modular project structure
- Automated testing
- Input validation
- Error handling
- JSON persistence
- Git version control
- Conventional commit messages
- Semantic versioning
- Test-driven development practices

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

The main branch is:

```text
main
```

## Versioning

The project follows Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Current development version:

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

Improved data validation, storage reliability, application management, and automated testing.

Included:

- JSON validation
- Invalid JSON handling
- Missing file handling
- JSON structure validation
- Job data validation
- Application date validation
- Duplicate application prevention
- Search and filtering functionality
- Application statistics
- Automated tests
- Expanded test coverage

## Roadmap

Planned improvements for future versions:

- [ ] Sort applications by date
- [ ] Improve CLI user experience
- [ ] Add database persistence
- [ ] Create a REST API
- [ ] Create a web interface
- [ ] Add authentication
- [ ] Add automated CI/CD
- [ ] Add logging
- [ ] Improve application architecture
- [ ] Add database migrations
- [ ] Add API documentation

## Author

**Cristian Gonzalez**

GitHub:

https://github.com/crisgv851/JobTracker