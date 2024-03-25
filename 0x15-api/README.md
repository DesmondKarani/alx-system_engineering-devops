# Employee Data API Interaction Project

## Project Overview

This project focuses on accessing and managing employee data through an API. It demonstrates the transition from Bash scripting to Python, highlighting the advantages of using Python for tasks involving complex data manipulation, API interactions, and adherence to modern coding practices. The project covers fetching, organizing, and exporting employee data to various data structures.

## Learning Objectives

By the end of this project, learners should be able to:

- Understand the limitations of Bash scripting for certain tasks.
- Explain what APIs are and how they facilitate communication between different software systems.
- Describe what a REST API is and its significance in web services and microservices.
- Understand the structure and use of CSV and JSON formats in data manipulation.
- Apply Pythonic coding styles and conventions for more readable and maintainable code.

## Prerequisites

- Python 3.8.5
- Ubuntu 20.04 LTS
- Familiarity with text editors (vi, vim, emacs)
- Basic understanding of HTTP methods and status codes
- Knowledge of Python's `requests`, `json`, and `csv` modules

## Setup and Installation

1. **Environment Preparation**: Ensure Python 3.8.5 is installed on your Ubuntu 20.04 LTS system.

2. **Project Files**: Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

3. **Dependencies**: Install necessary Python modules:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To fetch and display employee data:

  ```bash
  ./fetch_employee_data.py
  ```

- To export employee data to CSV:

  ```bash
  ./export_to_csv.py
  ```

- To export employee data to JSON:

  ```bash
  ./export_to_json.py
  ```

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Code Style

This project adheres to the PEP8 Python style guide. Ensure your contributions are compliant.

## License

[MIT License](LICENSE.txt)

## Acknowledgments

- Special thanks to all contributors and reviewers.
- This project is inspired by the transition towards more efficient scripting and system administration practices.
