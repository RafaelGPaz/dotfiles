#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import re

####EDIT HERE####
ffs_batch_folder_path = '<.../RTS_Config/>'
ffs_batch_file = '<BatchRun_.ffs_batch>'
nas_folder_path = '<...>'
u = '<user>'
p = '<pass>'
ipnas = '<remote ip>'
#################

#Quick info#
#mount_afp output cannot be recorded through subprocess
#re.search(A in var) true - is not None
#re.search(A in var) false - is None

sleep_period = 60 #in seconds
first_launch_sleep_period = 30 #in seconds

def run_ffs_batch():
    #give some time to connect remote folder where it will sync
    time.sleep(first_launch_sleep_period)
    local_mount_folder = os.path.join('/Volumes/'+nas_folder_path)
    #auto connect to remote folder
    if (os.path.exists('/Volumes/%s' %nas_folder_path) is False):
        try:
            os.mkdir(local_mount_folder)
        except OSError as e:
            print('%s' %e)
    try:
        mount_afp_ps = subprocess.Popen('mount_afp -i afp://%s:%s@%s/%s %s' %(u,p,ipnas,nas_folder_path,local_mount_folder), shell=True, stdout=subprocess.PIPE)
        read_mount_afp_ps = mount_afp_ps.stdout.read().decode('utf-8')
        mount_afp_ps.stdout.close()
        mount_afp_ps.wait()
        ping_ps = subprocess.Popen('ping -c 3 -m 3 -i 1 %s' %ipnas, shell=True, stdout=subprocess.PIPE)
        read_ping_ps = ping_ps.stdout.read().decode('utf-8')
        ping_ps.stdout.close()
        ping_ps.wait()
        print ('read_ping_ps:\n%s' %read_ping_ps)
        abc = re.search('100.0% packet loss',read_ping_ps)
        print ('%s' %abc)
        if re.search('100.0% packet loss',read_ping_ps) is None:
            print ('Remote folder is mounted!')
        else:
            print ('Remote folder is NOT mounted!')
    except OSError as e:
        print('%s' %e)
    #starts periodic function
    while(1):
        ping_ps = subprocess.Popen('ping -c 3 -m 3 -i 1 %s' %ipnas, shell=True, stdout=subprocess.PIPE)
        read_ping_ps = ping_ps.stdout.read().decode('utf-8')
        ping_ps.stdout.close()
        ping_ps.wait()
        ls_ps = subprocess.Popen('ls %s' %local_mount_folder, shell=True, stdout=subprocess.PIPE)
        read_ls_ps = ls_ps.stdout.read().decode('utf-8')
        ls_ps.stdout.close()
        ls_ps.wait()
        print ('read_ls_ps:\n%s' %read_ls_ps)
        if (((os.path.exists('/Volumes/%s' %nas_folder_path) is True)and(re.search('100.0% packet loss',read_ping_ps) is None))and((re.search('No such file or directory',read_ls_ps) is not None)or(len(read_ls_ps)!=0))):
            if os.path.exists('%s' %ffs_batch_folder_path):
                print('Connected to remote folder')
                #check if there is another FreeFileSync process openned
                freefilesync_app_ps = subprocess.Popen("ps -eaf | grep FreeFileSync", shell=True, stdout=subprocess.PIPE)
                freefilesync_read_ps = freefilesync_app_ps.stdout.read().decode('utf-8')
                freefilesync_app_ps.stdout.close()
                freefilesync_app_ps.wait()
                if re.search('FreeFileSync.app',freefilesync_read_ps) is None:
                    try:
                        #run batch file
                        subprocess.call(['open', "%s" %ffs_batch_file], cwd=ffs_batch_folder_path)
                        print('FreeFileSync.app started!')
                    except subprocess.CalledProcessError as e:
                        print ('Unable to sync, check batch file name and location: \n%s' %e)
                else:
                    print('Process already exists, another one was ignored till the previous one terminate!')
            else:
                ap = """ display dialog "Localhost folder not accessible, please contact your system administrator!" with title "Warning from Localhost Folder!" with icon stop buttons {"OK"} """
                subprocess.call("osascript -e '{}'".format(ap),shell=True)
                print ('Localhost folder not accessible!')
        else:
            #if ((os.path.exists('/Volumes/%s' %nas_folder_path)) is False)or(re.search('timeout',read_ping_ps) is None):
            ap = """ display dialog "Remote folder not mounted, please check your network connection and click Try again. If this problem persist contact your system administrator!" with title "Warning from Remote Folder!" with icon caution buttons {"Try again"} """
            subprocess.call("osascript -e '{}'".format(ap),shell=True)
            print('Remote folder is NOT mounted!')
            #time.sleep(sleep_period)
            if (os.path.exists('/Volumes/%s' %nas_folder_path) is False):
                try:
                    os.mkdir(local_mount_folder)
                except OSError as e:
                    print('%s' %e)
            try:
                mount_afp_ps = subprocess.Popen('mount_afp -i afp://%s:%s@%s/%s %s' %(u,p,ipnas,nas_folder_path,local_mount_folder), shell=True, stdout=subprocess.PIPE)
                read_mount_afp_ps = mount_afp_ps.stdout.read().decode('utf-8')
                mount_afp_ps.stdout.close()
                mount_afp_ps.wait()
            except OSError as e1:
                print('%s' %e)
            if (re.search('100.0% packet loss',read_ping_ps) is None)and(len(e1)==0):
                print ('Remote folder is NOW mounted!')
            else:
                print ('Remote folder is NOT mounted!')
        #sync period of time
        time.sleep(sleep_period)

if __name__=="__main__":
    run_ffs_batch()