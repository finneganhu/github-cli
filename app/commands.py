import requests
from typing import List

def get_recent_releases(repo: str, num: int) -> None:
    """
    Retrieve most recent releases for the given repository

    :param repo: user provided repository, follows format {repo_owner}/{repo_name}
    :param num: number of most recent releases to display, default to 3
    """ 
    print(f'Hey! Getting {num} most recent releases from {repo}\n...')
    # call Github Releases API to retrieve most recent releases
    releases_api = f'https://api.github.com/repos/{repo}/releases?per_page={num}&page=1'
    try:
        res = requests.get(releases_api, timeout = 5)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if res.status_code != 200:
        # provide error information if the response status code is not 200
        print(f'Error fetching releases for repository: {repo}')
        print(f'Error message: {res.json().get("message")}')
        print('Please make sure the repo input follows the format {repo_owner}/{repo_name} and the repository is public')
    else:
        # if the response status code is 200, print the most recent releases
        try:
            releases = res.json()
        except Exception as e:
            print('Invalid response')
            raise SystemExit(e)
        
        if len(releases) == 0:
            print(f'{repo} has no releases yet')
        else:
            print(f'Here are the {len(releases)} most recent releases from {repo}:')
        for release in releases:
            version = release['tag_name']
            print(f'{version}')

def get_recent_prs(repo: str, num: int) -> List[dict]:
    """
    Retrieve most recent pull requests for the given repository

    :param repo: user provided repository, follows format {repo_owner}/{repo_name}
    :param num: number of most recent pull requests to display, default to 3
    """ 
    print(f'Hey! Getting {num} most recent pull requests from {repo}\n...')
    # call Github Pulls API to retrieve most recent pull requests
    pulls_api = f'https://api.github.com/repos/{repo}/pulls?state=all&per_page={num}&page=1'
    try:
        res = requests.get(pulls_api, timeout = 5)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if res.status_code != 200:
        # provide error information if the response status code is not 200
        print(f'Error fetching pull requests for repository: {repo}')
        print(f'Error message: {res.json().get("message")}')
        print('Please make sure the repo input follows the format {repo_owner}/{repo_name} and the repository is public')
    else:
        # if the response status code is 200, print the most recent releases
        try:
            prs = res.json()
        except Exception as e:
            print('Invalid response')
            raise SystemExit(e)
        
        if len(prs) == 0:
            print(f'{repo} has no pull requests yet')
        else:
            print(f'Here are the {len(prs)} most recent pull requests from {repo}:')
        for pr in prs:
            title = pr['title']
            number = pr['number']
            print(f'PR#{number} {title}')