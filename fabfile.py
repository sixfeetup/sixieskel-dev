"""
Commands available to deploy using sixfeetup.deployment
"""
from fabric.api import env
# this is necessary to make the fabric commands available
from sixfeetup.deployment.commands import *

# General metadata

# This is the trac/svn/dist name
# Default: ""
env.project_name = "sixieskel"

# URL to the trac instance base
# Default: "https://trac.sixfeetup.com"
#env.trac_url_base = "

# packages

# Default release target. This is a jarn.mkrelease target name
# Default: "public"
env.default_release_target = "public"

# This is a directory that contains the eggs we want to release
# Default: ['src']
#env.package_dirs = []

# List of package paths
# Default: []
#env.packages = []

# List of package paths names to ignore (e.g. 'my.package')
# Default: []

# KARL will require manual releases for now
env.ignore_dirs = []
