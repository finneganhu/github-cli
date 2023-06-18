import argparse
from commands import get_recent_releases, get_recent_prs

def main():
    # initiate and setup argparse
    parser = argparse.ArgumentParser(description = 'GitHub Command Line Tool')
    parser.add_argument('command', type = str, help = 'The command to run. Should be either "get-recent-releases" or "get-recent-prs"',
                        choices = ['get-recent-releases', 'get-recent-prs'])
    parser.add_argument('--repo', type = str, required = True, help = 'The Github repo to run the command on')

    # parse user command line input
    args = parser.parse_args()
    command, repo = args.command, args.repo

    # run corresponding command function
    if command == 'get-recent-releases':
        get_recent_releases(repo, 3)
    elif command == 'get-recent-prs':
        get_recent_prs(repo, 3)

if __name__ == '__main__':
    main()