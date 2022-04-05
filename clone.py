' write afunction to clone a github repository'

def clone(username, repo):
    ' clone a github repository '
    import requests
    import sys
    url = 'https://api.github.com/repos/{}/{}'.format(username, repo)
    r = requests.get(url)
    if r.status_code != 200:
        print('Error: {}'.format(r.status_code))
        sys.exit(1)
    url = r.json()['clone_url']
    r = requests.get(url)
    if r.status_code != 200:
        print('Error: {}'.format(r.status_code))
        sys.exit(1)
    print(r.text)

