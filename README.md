> # Vesting Events Parser

This application reads a file and parses its data to return a summary of all Vesting events sorted by Employees and its Awards.

You can filter the records by a given target date to return only the records computed until that target date.

<br>

> ## Architecture

The Architeture uses the Strategy Pattern to implement the parsers and keep the application open to add new parsers easily.

Notifications can easily have new implementations as well due to the use of interface segregation.

It was used the generator concept that Python offers to read the file without crashing the memory by reading it all at once.

### Application flow

<h1 align="center">
    <img alt="Architecture" title="#vesting" src="assets/images/architecture.png"/>
</h1>

> ## Requirements

The functional requirements are available on the Requirements PDF file.

<br>

> ## Install the dependencies

Create a local environment to install the dependencies and activate it:

```bash
# Needs admin permission to run
sudo make virtualenv
source .venv/bin/activate
```

<br>

> ## How to run the tests

```bash
make test
```

<br>

> ## How to run the application

Arguments accepted to execute the application:

```text
-f / --fullfilename
-d / --date
-p / --precision
```

Run the following command to see a description of the accepted args:

```bash
# See the args accepted
python3 main.py -h

# Run the application
python3 main.py -f assets/data1.csv -d 2021-01-01 -p 1
```

To run linting, execute the following command inside the root folder:

```bash
make lint
```

<br>

> ## Principles

- [Single Responsibility Principle (SRP)](https://en.wikipedia.org/wiki/Single-responsibility_principle)
- [Open/Closed Principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)
  - Use of the [Strategy Pattern](https://en.wikipedia.org/wiki/Strategy_pattern) so the application is open to be extended (you can implment other parsers just by implementing a new strategy), but closed to be modified (the context will take care of adding the new strategy to the flow).
- [KISS Principle](https://pt.wikipedia.org/wiki/Princ%C3%ADpio_KISS)
- [DRY Principle](https://pt.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [Clean Code](https://martinfowler.com/tags/clean%20code.html):

  Best practices used in this project to ensure Clean Code:

  - Functions were designed to:
    - be small
    - do one thing
    - contain code with the same level of abstraction
    - have fewer than 4 arguments
    - have no duplication
    - use descriptive names

- Code Patterns:

  To keep a better code pattern between the development team, it should be configured some tools for keeping the patterns without bigger effort and also configure a command that runs linting to prevent bad code to be promoted to production. Tools and libs used in this project:

  - [flake8](https://pypi.org/project/flake8/): Tool For Style Guide Enforcement
  - [isort](https://pycqa.github.io/isort/): Utility / library to sort imports alphabetically, and automatically separated into sections and by type
  - [black](https://pypi.org/project/black/): An uncompromising Python code formatter

<br>

> ## Methodologies and Designs

- Small commits: Use of the specification for adding human and machine readable meaning to commit messages concept from [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

- GitFlow: Usage of the [GitFlow](https://docs.github.com/en/get-started/quickstart/github-flow) for development.

<br>

> ## Libraries and Tools

- Python 3.8.2
- flake8
- black
- isort

<br>

> ## Improvements

Due to the lake of time to implement everything I had in mind, I'll just explain what I would do before promoting this application to production:

- The code coverage should be analyzed to add tests to improve its percentage. A good practice is to keep the coverage up to 80%. This application contemplates 100% coverage, but it needs improvement to cover more edge cases.

- In case of it's necessary to implement data persistency, a new structure should be designed to use a design pattern as Repository and DDD (Domain Driven Design) for a better Clean Architecture.

- To improve performance, could be used an architecture that read the file in chuncks and starts some threads to execute the parsing paralleling. But as this application showed being very efficient on tests using 1 million lines file (it took 6 seconds to run it, using less than 1% of the memory) this implementation was not chosen. The code bellow is an example how to implement parallelism in python:

  ```python
    import multiprocessing as mp
    import csv

    CHUNKSIZE = 10000   # Set this to whatever you feel reasonable
    def _run_parallel(csvfname, csvoutfname):
      with open(csvfname) as csvf, \
            open(csvoutfname, 'w') as csvout\
            mp.Pool() as p:
          reader = csv.reader(csvf)
          csvout.writerows(p.imap(process, reader, chunksize=CHUNKSIZE))
  ```

- To improve Exception and Error handling, it is a good practice is to create the application's own error classes and set it using a decorator on the methods.

- And last, but not least, would be interesting to implement dependency injection to decouple some objects, like the Logger, and make it available at the beggining of the running, so the object would be a singleton and would be available for all classes to use without the need for instanciation.
  One optios to use in Python for DI is the lib [Dependency Injector](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html). Dependency injection framework can significantly improve a flexibility of the language with a static typing. Implementation of a dependency injection framework for a language with a static typing is not something that one can do quickly. It will be a quite complex thing to be done well, that's the reason why I chose not to implement at this point of the project, but in larger projects, this comes to be quite necessary.
