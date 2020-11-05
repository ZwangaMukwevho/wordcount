import sys
import subprocess
 


class fileTransfer:
    """Class that handles file transfer transfer functionlities. 
    """
    def getIP(self):
        """It returns the IP address of the raspberry PI.
		"""
        subprocess.run(["hostname","-I"])

  