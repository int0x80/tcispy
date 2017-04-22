# tcispy

Pull author and committer names and emails from Travis-CI.

# Dependencies

A personal access token is needed from GitHub to use the Travis-CI API, even for public repositories.  Create a token by editing your profile -> Personal Access Tokens, and select the following scopes:

* repo:status
* repo_deployment
* read:org
* write:repo_hook
* user:email

The [travispy](https://github.com/menegazzo/travispy) module is used to interface with the Travis-CI API.  Using virtual environments is suggested.

```
mkvirtualenv travispy  # only needed if keeping your evironment sane
pip install travispy
```

# Usage

```
python ./tcispy.py <target/repo> <access_token>
```

An example run looks like:

```
python ./tcispy.py rapid7/nexpose-client d84dda6de6244eb5c30d3ef3eeda957d390a4ee7
```
