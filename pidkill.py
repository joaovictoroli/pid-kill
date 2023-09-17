import os

# kill process by port
# like netstat -ano | findstr :5234
# taskkill /PID 5234 /F

def kill_by_port(port):
    try:
        # get pid by port
        pid = os.popen("netstat -ano | findstr :%s" % port).readlines()[0].strip().split(' ')[-1]
        # kill pid
        os.system('taskkill /PID %s /F' % pid)
        print('kill pid: %s' % pid)
    except Exception as e:
        print(e)

def main():
    result = input('Which port do you want to kill?')
    try:
        kill_by_port(result)
    except: 
        print("Something went wrong")
    else:
        print("Nothing went wrong")
    

if __name__ == "__main__":
    main()