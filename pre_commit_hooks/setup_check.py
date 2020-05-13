import subprocess

def main():
    retval = 0
    process = subprocess.Popen(['python', 'setup.py', 'check'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = process.stdout.read().decode()
    if stdout != "running check\n":
        retval = 1
        print(stdout)
    return retval

if __name__ == '__main__':
    main()