# github-command-line-tool
A command line tool that interfaces with GitHub REST API to pull recent releases and pull requests.

# Requirement
Using the programming language of your choice, create a command line tool that interfaces with a GitHub REST API. It should be able to perform these two commands:

1. Given a repository, return the names/version numbers of the three latest releases.
2. Given a repository, return the title and number of the three most recent pull requests.

# Note to myself

## Development Steps
1. Come up with overall file structure
2. Initial implementation of functional code
3. Add tests
4. Review code
    - Comments
    - Logging
    - Readable & maintainable
    - Handling edge cases
    - Performance
        - Fast execution
        - Handling large inputs gracefully
5. Dockerize the app
6. Add-ons
    - CI/CD
    - Repo management
    - Monitoring
7. Documentation