import os
from datetime import datetime

now = datetime.now()

class Logger():
    def CheckStatus():
        # Check if log file exists
        if os.path.exists("runtime_logs.log"):
            pass
        else:
            with open("runtime_logs.log", "w") as cf:
                cf.close()
        return 200
    
    def WriteLog(type, pos, data):
        dt = now.strftime("%d/%m/%Y-%H:%M:%S")
        seperator = "==================="
        with open("runtime_logs.log") as logfile:
            logfile.write(seperator)
            logfile.write(f"This report was generated at: {dt}\n")
            logfile.write(f"Location: {pos}\n\n")
            logfile.write(data)
            