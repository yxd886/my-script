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
  cmd="nohup ~/xiaodong/xmrMiner/build/gputest -l 16x48 -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x &"
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
  cmd="nohup ~/xiaodong/xmrMiner/build/gputest -l 16x48 -o stratum+tcp://xmr.pool.minergate.com:45560 -u xiaodongyee@gmail.com -p x &"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_r4():
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate()
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmrMiner/build/gputest | grep -v grep | awk '{print $2}')"
  process = subprocess.Popen(cmd, stdout=FNULL, shell=True)
  output, error = process.communicate() 
def kill_r5(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
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
  
  
def kill_g1(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                          
  stdin,stdout,stderr =  ssh.exec_command(cmd);                                                                                        
def kill_g2(ssh):                                                                                                                      
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"                          
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g3(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g4(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g5(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g6(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g7(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);
def kill_g8(ssh):
  cmd="sudo kill -9 $(ps -ef | grep /xiaodong/xmr-stak/build/bin/xmr-stak | grep -v grep | awk '{print $2}')"
  stdin,stdout,stderr =  ssh.exec_command(cmd);


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

  kill_g1(ssh_g1)                                                                                                                      
  kill_g2(ssh_g2)
  kill_g3(ssh_g3)
  kill_g4(ssh_g4)
  kill_g5(ssh_g5)
  kill_g6(ssh_g6)
  kill_g7(ssh_g7)
  kill_g8(ssh_g8)

  ssh_g1.close()                                                                                                                       
  ssh_g2.close()
  ssh_g3.close()
  ssh_g4.close()
  ssh_g5.close()
  ssh_g6.close()
  ssh_g7.close()
  ssh_g8.close() 
def main():


  test()

if __name__ == '__main__':
    main()
