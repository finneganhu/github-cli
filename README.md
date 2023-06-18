# Github Command Line Tool

A Python command line tool that interfaces with GitHub REST API to pull recent releases and pull requests for a given public GitHub repository.

## Installation

There are 2 ways to install this tool once you cloned this repository to your local. You can either run the Python file directly, or build the application into a Docker image then run it as a Docker container. It's recommended to run it as a Docker container since it's simpler and doesn't involve any local installation. Please see the steps below for both ways of installation.

**Running Python Script Directly**

1. Make sure you are in the root directory of this repository and you have `python` and `pip` installed in your local.

2. Run `virtualenv env` to set up a virtual environment.

3. Run `source env/bin/activate` in the project folder to activate virtual environment.

4. Run `pip install -r requirements.txt` to install required Python packges.

**Running as Docker Container**

1. Make sure you are in the root directory of this repository, and you have Docker installed and running in your local.

2. Run `docker build -t {any_image_name} .`, e.g. `docker build -t github-cli .`

## Usage

The exact command to run will depend on how you chose to install the application. Please see the steps below for usage with both installations.

**Running Python Script Directly**

 - `python app/main.py {command_to_run} --repo {repository}`

**Running as Docker Container**

- `docker run {your_image_name} {command_to_run} --repo {repository}`
    - e.g. `docker run github-cli {command_to_run} --repo {repository}`

**General Usage**

- You have 2 options for command to run: 
    - `get-recent-releases`: pull most recent 3 releases for the given repository, or 
    - `get-recent-prs`: pull most recent 3 pull requests for the given repository.
- For `--repo` parameter, please make sure that the repository you provide is a public GitHub repository and the input follows format `{repo_owner}/{repo_name}`, e.g. `openai/gym`.

**Example Usage**

Let's say you want to find out the most recent 3 releases for [curl/curl](https://github.com/curl/curl). With Docker image `github-cli` built locally. You would run

```
docker run github-cli get-recent-releases --repo curl/curl
```

And you should get output similar to the following

```
Hey! Getting 3 most recent releases from curl/curl
...
Here are the 3 most recent releases from curl/curl:
curl-8_1_2
curl-8_1_1
curl-8_1_0
```

## Features

**Pull any number of recent releases/pull requests**

The number of recent releases/pull requests to pull is set to 3 in default. If you want to pull other number of results, you can easily do that by updating the input parameter for either command function in `app/main.py`.

**Argparse**

This command line tool utilizes Python package `argparse` to ingest and validate user input. You can run `python app/main.py -h` or `docker run github-cli -h` to get help information for the command line input arguments.

**Less releases/pull requests than requests**

The command line tool will try to pull all the results requests (default to 3). If there are less results than what's requested, it will return all results to the user. For example, if a repository has only 2 releases but 3 is requests by user, the tool will return all 2 releases.

**Optimization**

In order to improve the efficiency and performance of the requests, for the calls to GitHub APIs, instead of pulling all the releases/pull requests for the given repository, the requests utilize the `per_page` and `page` query parameters to limit the size of the result returned.

## Development Workflow

To contribute to this application, you can follow the below steps:

1. Clone the repository to your local.

2. Create a local develop branch based off on `main` branch.

3. Add and commit your changes.

4. Push your local develop branch to remote.

5. Create a pull request from your remote develop branch to `main`.

6. Once the pull request is created, the Github Action workflow `Main Branch Pull Request Workflow` will be triggered, which set up the application in a virtual environment and run it against unit tests in `/tests`. Same applies to any additional commits to the pull request.

7. Although it's not enforced, you should only merge the pull request if the workflow returns success status.

## Area for Improvements

- More unit tests to cover additional edge cases (connection timeout, invalid response content, etc.)

- Implement end-to-end test to test `app/main.py` additional to the unit tests for individual command functions.

- Currently the tool can only be shared through the GitHub repository. We can package the tool as a Python module and upload to PyPi, or push the Docker image to Docker Hub so that the tool can be installed more conveniently.