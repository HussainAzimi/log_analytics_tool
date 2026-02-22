# Streaming Log Analytics: OO Structure & Functional Pipelines:
## Project Context: & Objective:
Modern systems generate massive volumes of event logs that make traditional procedural "loading" strategies brittle and prone to memory exhaustion.
## Project Objective:
  - **Architecture:** To replace brittle, "one giant loop" procedural code with a decoupled architecture that separates data modeling (OO) from data flow (FP).

  - **Performance:** To demonstrate that by using lazy evaluation and Python's native iterator protocol, we can build tools that are both highly readable and capable of handling "Big Data" scales on standard hardware

## Features:
  - **Lazy Log ingestion:** Implements the Iterator Pattern to read files line-by-line using Python generators.

  - **Domain-Driven Parsing:** Transforms raw text into **LogEvent** domain objects. This separates the messy reality of raw logs from the clean, structured logic required for analytics.

  - **Functional Processing Pipelines:** Employs a declarative approach to data transformation. By composing small, pure functions, the system filters and maps event streams without side effects or "one giant loop" complexity.

  - **Effective Use of Python Built-ins:** Leverages high-performance built-in functions for concise and efficient logic:

    any / all: For optimized, short-circuiting boolean checks (e.g., suspicious activity detection).

    sum: For memory-efficient counting within generator expressions.

    min / max / sorted: For analytical ranking and time-series boundaries.

    - **Zero-Materialization Summaries:** Produces complex analytical reports—such as top-N error counts—while avoiding unnecessary materialization of data into intermediate lists, preserving system resources.

  - **Immutable Domain Model:** Uses frozen Python Dataclasses for validation, thread-safe log event representation.

  - **Dynamic Query Engin:** A strategy pattern-based dispatch table that allows for extensible analytics without modifying core logic.

  - **Robust Parsing:** Handle pipe-delimited logs with optional comma-separated metadata and comprehensive error reporting.

  - **Comprehensive Tests:** Includes 9+ automated tests covering parsing edge cases, streaming behavior, and API dispatch logic.


## Project Structure:
```
├── src/
│   ├── __init__.py
│   ├── log_model.py    # OO: LogEvent dataclass and custom exceptions
│   ├── pipeline.py     # FP: Lazy filtering, mapping, and parsing
│   └── queries.py      # API: Dispatch table and analytic functions
├── tests/
│   ├── __init__.py
│   ├── test_parsing.py  # Tests for model and parsing logic
│   ├── test_pipeline.py # Tests for laziness and streaming
│   └── test_queries.py  # Tests for query dispatch and analytics
├── reflection.md       # Architectural justifications
└── README.md
```
## Requirements
 - Python 3
 - pytest (for running the tests)

## Running Tests 
  - run pytest from the root directory for general test:  
  ``` pytest -m pytest ```

  - For single file test
     ``` 
      pytest tests/test_parsing.py
      pytest tests/test_pipeline.py
      pytest tests/test_queries.py
     ```