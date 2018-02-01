#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time
import paramiko
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

  parser.add_option('', '--sc', action="store", type="string", dest="service_chain", help="chain rule", default="pkt_counter")

  parser.add_option('', '--r1', action="store", type="int", dest="r1_number", help="How many rts in r1", default="1")

  parser.add_option('', '--r2', action="store", type="int", dest="r2_number", help="How many rts in r2", default="1")

  parser.add_option('', '--r3', action="store", type="int", dest="r3_number", help="How many rts in r3", default="1")

  options, args = parser.parse_args()

  return options,args


def start_r4():
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".r4:x --farm-recheck 200 &"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate()
  print error
def start_g1(ssh):                                                                                                         
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+" --farm-recheck 200 &"
  print cmd
  stdin,stdout,stderr =  ssh.exec_command(cmd);

def start_g2(ssh):
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g2:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 

def start_g3(ssh):
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g3:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_g4(ssh):
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g4:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_g5(ssh):
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g5:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def start_g6(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g6:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
                                                                                                                                       
def start_g7(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g7:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
def start_g8(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".g8:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_r5(ssh):
  success_flag = False;
  cmd="nohup ~/xiaodong/cpp-ethereum/build/ethminer/ethminer -U -S eth.f2pool.com:8080 --stratum-protocol 1 -O "+address+".r5:x --farm-recheck 200 &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_r4():
  cmd="sudo kill -9 $(ps -ef | grep ethminer | grep -v grep | awk '{print $2}')"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate() 
def remote_kill(ssh):
  cmd="sudo kill -9 $(ps -ef | grep ethminer | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g1(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep ethminer | grep -v grep | awk '{print $2}')"                               
  stdin,stdout,stderr =  ssh.exec_command(cmd); 

def kill_b2(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_b3(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_b4(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_b6(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                          
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
def kill_b7(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                          
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
def kill_b8(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                          
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def start_traffic_gen(options):
  cmd="sudo ./start_flowgen.sh "+str(options.r1_number)
  #process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate()

def read_pkts(ssh,rt_num):
  cmd="sudo ~/nfa/deps/bess/bessctl/bessctl show port rt"+str(rt_num)+"_iport"
  stdin,stdout,stderr = ssh.exec_command(cmd);

  received_pkts_line = ''
  dropped_pkts_line = ''

  i = 0
  for line in stdout:
    if i == 6:
	received_pkts_line = line
    if i == 7:
        dropped_pkts_line = line
    i=i+1


  return long(received_pkts_line.split(":")[1].replace(',', '')), long(dropped_pkts_line.split(":")[1].replace(',', ''))
def clean(ssh_b1,ssh_b2,ssh_b3,ssh_b4,ssh_b6,ssh_b7,ssh_b8):
  ssh_b1.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b2.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b3.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b4.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b6.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b7.exec_command('rm ~/cpu.txt ~/config.txt')
  ssh_b8.exec_command('rm ~/cpu.txt ~/config.txt')
  
  

def test():
  #print "Creating SSH to R2 & R3"
  ssh_r5 = paramiko.SSHClient()
  ssh_r5.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_r5.connect('202.45.128.158',username='net',password='netexplo')
  ssh_r5.exec_command('cd ~/xiaodong/xmr-stak/build/bin')
  ssh_g1 = paramiko.SSHClient()                                                                                                        
  ssh_g1.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g1.connect('202.45.128.221',username='net',password='netexplo') 
  ssh_g1.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_g2 = paramiko.SSHClient()                                                                                                        
  ssh_g2.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g2.connect('202.45.128.222',username='net',password='netexplo')
  ssh_g2.exec_command('cd ~/xiaodong/xmr-stak/build/bin') 

  ssh_g3 = paramiko.SSHClient()                                                                                                        
  ssh_g3.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g3.connect('202.45.128.223',username='net',password='netexplo') 
  ssh_g3.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_g4 = paramiko.SSHClient()                                                                                                        
  ssh_g4.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g4.connect('202.45.128.224',username='net',password='netexplo')
  ssh_g4.exec_command('cd ~/xiaodong/xmr-stak/build/bin')
 
  ssh_g5 = paramiko.SSHClient()
  ssh_g5.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_g5.connect('202.45.128.225',username='net',password='netexplo')
  ssh_g5.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_g6 = paramiko.SSHClient()                                                                                                        
  ssh_g6.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g6.connect('202.45.128.226',username='net',password='netexplo')
  ssh_g6.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_g7 = paramiko.SSHClient()                                                                                                        
  ssh_g7.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g7.connect('202.45.128.227',username='net',password='netexplo')
  ssh_g7.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_g8 = paramiko.SSHClient()                                                                                                        
  ssh_g8.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_g8.connect('202.45.128.228',username='net',password='netexplo')
  ssh_g8.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

#  clean(ssh_b1,ssh_b2,ssh_b3,ssh_b4,ssh_b6,ssh_b7,ssh_b8)

  kill_r4()
  remote_kill(ssh_r5)
  remote_kill(ssh_g1)
  remote_kill(ssh_g2)
  remote_kill(ssh_g3)
  remote_kill(ssh_g4)
  remote_kill(ssh_g5)
  remote_kill(ssh_g6)
  remote_kill(ssh_g7)
  remote_kill(ssh_g8)


def main():


  test()

if __name__ == '__main__':
    main()
