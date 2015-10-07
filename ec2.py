#!/usr/bin/python

import os
import sys
import boto.ec2

from pprint import pprint
from optparse import OptionParser

__doc__ = """
    A script I (@josephmisiti) use to interface with EC2.
"""

auth = {"aws_access_key_id": os.environ['AWS_FETCHER_KEY'],
        "aws_secret_access_key": os.environ['AWS_FETCHER_SECRET'],}

def list_instances(auth, verbose=False):
    """ list all instances """
    ec2 = boto.ec2.connect_to_region("us-east-1", **auth)
    print("\n")
    for instance in ec2.get_all_instances():
        meta_data = instance.instances[0].__dict__
        if verbose:
            print("\n")
            pprint(meta_data)
        else:
            print("{id} -{tags}".format(id=instance.id,tags=meta_data['tags']))

def update_instance_state(instance_id, instance_state):
    """ update instance state """

def run_aws(auth):
    
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-r", "--region",
                      action="store", 
                      dest="region",
                      default="us-east-1",
                      help="AWS region",)
    parser.add_option("-i", "--instance-id",
                      action="store", 
                      dest="instance_id",
                      default=None,
                      help="instance id",)
    parser.add_option("--instance-state",
                      action="store", 
                      dest="instance_state",
                      default=None,
                      help="instance state",)
    parser.add_option("-v", "--verbose",
                      action="store_true", 
                      dest="verbose",
                      default=False,
                      help="Verbose",)
    parser.add_option("-l", "--list-instances",
                      action="store_true", 
                      dest="list_instances",
                      default=False,
                      help="List instances?",)
    parser.add_option("-k", "--key",
                      action="store_true", 
                      dest="aws_key",
                      default=None,
                      help="AWS Key",)
    parser.add_option("-s", "--secret",
                      action="store_true", 
                      dest="aws_secret",
                      default=None,
                      help="AWS Secret",)
    (options, args) = parser.parse_args()

    if options.list_instances:
        list_instances(auth, verbose=options.verbose)
    if options.instance_id and options.instance_state:
        update_instance_state(options.instance_id,options.instance_state)
    
    
if __name__ == '__main__':
    sys.exit(run_aws(auth))