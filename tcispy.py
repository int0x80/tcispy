#!/usr/bin/env python
# -----------------------------------------------------------
# tcispy.py 
#
# Pull author and committer names and emails from travis-ci.
#
# Usage:
#   mkvirtualenv travispy
#   pip install travispy
#   python ./tcispy.py <target/repo> <access_token>
#
# Example:
#   python ./tcispy.py rapid7/nexpose-client d84dda6de6244eb5c30d3ef3eeda957d390a4ee7 2>/dev/null
# -----------------------------------------------------------

from sys import argv, exit
from travispy import TravisPy


def main():

  # -----------------------------------------------------------
  # quick sanity check for args
  # -----------------------------------------------------------
  if len(argv) != 3:
    print 'Insufficient arguments.'
    print 'Usage: {} <target/repo> <access_token>'.format(argv[0])
    print 'Example: {} krux/hyperion d84dda6de6244eb5c30d3ef3eeda957d390a4ee7'.format(argv[0])
    exit(1)
  
  
  # -----------------------------------------------------------
  # generate a token on github with the following access:
  #   repo:status
  #   repo_deployment
  #   read:org
  #   write:repo_hook
  #   user:email
  #
  # populate the github_token variable with the resulting token
  # -----------------------------------------------------------
  target_repo = argv[1] 
  github_token = argv[2] 
  
  
  # -----------------------------------------------------------
  # minimal client setup
  # -----------------------------------------------------------
  t = TravisPy.github_auth(github_token)
  builds = t.builds(slug=target_repo)
  
  
  # -----------------------------------------------------------
  # append users as a tuple (name, email). some users have 
  # multiple email addresses, and we want everything
  # -----------------------------------------------------------
  users = []
  for b in builds:
    try:
      build = t.build(b.id)

    except AttributeError:
      pass
      
    users.append((build.commit.author_name, build.commit.author_email))
    users.append((build.commit.committer_name, build.commit.committer_email))
  
  
  # -----------------------------------------------------------
  # trim the collection to unique tuples
  # -----------------------------------------------------------
  unique = list(set(users))
  
  
  # -----------------------------------------------------------
  # aaaaaaaaaaaand dump
  # -----------------------------------------------------------
  print 'Name,Email'
  for u in unique:
    print '{},{}'.format(u[0], u[1])


# -----------------------------------------------------------
# make it do the thing
# -----------------------------------------------------------
if __name__ == '__main__':
  main()
