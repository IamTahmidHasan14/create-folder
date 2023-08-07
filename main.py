import os 
if (not os.path.exists("NewF")):
    os.mkdir("NewF")
for i in range(5):
    os.mkdir(f"NewF/NewF{i+1}")