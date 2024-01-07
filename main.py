import subprocess

p1 = subprocess.Popen(["bash", "bash.sh"])
p2 = subprocess.Popen(["./frpc", "-c", "frpc.ini"])
p1.wait()
p2.wait()