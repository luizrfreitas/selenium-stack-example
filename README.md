# Selenium Stack Example

Study and test project to create a robust production ready stack for testing using Selenium Grid.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Running Multithreading with pytest-xdist](#running-multithreading-if-pytest-xdist)
  - [Creating Many Nodes of Browser](#creating-many-nodes-of-browser)
  - [Making Nodes Execute More Tests](#making-nodes-execute-more-tests)
  - [Changing Tests Naming](#changing-tests-naming)
- [Stack](#stack)

## Installation

[...]

## Usage

### Running Tests

To execute tests with `unittest`, use the following command:

```bash
docker exec python python -m unittest discover -s tests -p "*Test.py"
```

For running tests with `pytest`, use:

```bash
docker exec python pytest
```

### Running Tests in Parallel

To enable multithreaded execution using `pytest-xdist`, specify the number of worker processes:

```bash
docker exec python pytest -n NUMBER_OF_WORKERS
```

### Scaling Browser Nodes

To create multiple nodes of a specific browser, modify the container configuration by removing the `container_name` and `ports`. Then, execute:

```bash
docker compose up chrome --scale NUMBER_OF_NODES
```

### Increasing Node Test Capacity

To allow nodes to handle more simultaneous tests, set the following environment variable for the desired node:

```yaml
- SE_NODE_MAX_SESSIONS=5
```

### Customizing Test Naming

Adjust the naming convention for your tests by modifying the `app/pytest.ini` file according to your preferences.

## Stack

- Python
- Selenium Grid
- Docker
- Docker Compose
