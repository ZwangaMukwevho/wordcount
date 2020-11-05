# Imported files
import sys
import subprocess

class fileManager:
	"""This is a class that manages files and also allows the downloading, seaching and deleting of files.
    """


	def splitUrl(self,url):
		"""[Takes a url, splites it to and splits it to get the file type and also obtains the name of the file from the url.]

		:param url: [nameList (list): Takes in a ``url`` of the document to be downloaded.]
		:type url: [string]
		:return: [returns a list where the contents are the strings in the url that are seperated by a backslash ``/``. or  If the string has no backslash ``/`` decilimator it returns ``invalid URL given``]
		:rtype: [list]
		"""		

		# Checking if the url given is a strinf
		res= isinstance(url,str)

		if res is False:
			return "invalid URL given"

		urlList = url.split("/")
		if len(urlList) == 1:
			return "invalid URL given"
		else:
			return urlList
		


	def obtainName(self,nameList):
		"""[Obtains the name of the file from the url]

		:param nameList: [The ``nameList`` argument represent the url list returned the ``spliturl(self,url)`` function]
		:type nameList: [string]
		:return: [The name of file that URL in the nameList points to.]
		:rtype: [string]
		"""	

		# Checking if the namelist if of type tuple	
		if type(nameList) is not list:
			return ""

		length = len(nameList) -1
		nameWithtype = nameList[length]

		# Checking if the name is given as a string
		if type(nameWithtype) is not str:
			return ""

		#Obtaining the name of the file
		typeList = nameWithtype.split(".")
		
		# Checking if the name had a type within it initially i.e file.pdf, if it had a type the length of the file will be 2
		if len(typeList) == 1:
			return ""

		name = typeList[0]
		return name

	def obtainType(self,nameList):
		"""[Obtains the type of the file that the link points to]

		:param nameList: [The ``nameList`` argument represent the url list returned the ``spliturl(self,url)`` function]
		:type nameList: [strimg]
		:return: [The type of file that URL in the nameList points to]
		:rtype: [string]
		"""

		# Checking if the namelist if of type tuple	
		if type(nameList) is not list:
			return ""

		# Obtaining the name of file with type
		length = len(nameList) -1
		nameWithtype = nameList[length]

		# Checking if the name is given as a string
		if type(nameWithtype) is not str:
			return ""

		#Obtaining type of the file
		typeList = nameWithtype.split(".")

		# Checking if the name had a type within it initially i.e file.pdf, if it had a type the length of the file will be 2
		if len(typeList) == 1:
			return ""

		fileType = typeList[1]
		return fileType

	
	def donwloadFile(self,URL,fName,fType):
			
		
		if type(fName) is str and type(fType) is str:
			outName = fName + "." + fType
			subprocess.run(["curl","-O",URL])
			#subprocess.run(["mv",outName,"/media/usb/files"])
			subprocess.run(["mv",outName,"/home/pi/files"])
	
	def authDownload(self,URL,username,password,outName):
		"""[Downloads the file from a website that requires authentication, and stores the file in the USB. ]

		:param URL: [is the url that points to the file that is to be downladed.]
		:type URL: [string]
		:param username: [This is the username that the individual uses to login to a website]
		:type username: [string]
		:param password: [This is the password the individual uses to login to a file.]
		:type password: [string]
		:param outName: [This is the name of the file that the individual is downloading.]
		:type outName: [string]
		"""
		print("this is the outName "+outName)
		if type(username) is str and type(password) is str and type(outName) is str:
			authToken = username+":"+password
			subprocess.run(["curl","-u",authToken,"-O",URL])
			subprocess.run(["mv",outName,"/home/pi/files"])
		

	def searchFile(self,fName):
		"""[searches for the fileName in the usb module.]

		:param fName: [The name of the file that is being searched]
		:type fName: [string]
		:return: [The name of result of searching for the file using `find` command on a linux terminal.]
		:rtype: [string]
		"""

		if type(fName) is not str:
			return ""
		searchName = fName 
		#out = subprocess.Popen(["find","/media/usb/files","-name", searchName],stdout=subprocess.PIPE)
		out = subprocess.Popen(["find","/home/pi/files","-name", searchName],stdout=subprocess.PIPE)

		#Removing the "\n" at the end of the line
		output = out.stdout.read()[:-1:]
		return output

	def deleteFile(self,fName):
		"""[searches for the fileName and deletes it from the usb module]

		:param fName: [ The name of the file that is being searched, the name should include its file type at the end]
		:type fName: [string]
		:return: [The name of result of deleting for the file using `find` command on a linux terminal]
		:rtype: [string]
		"""

		if type(fName) is not str:
			return ""
		
		searchName = fName
		#out = subprocess.Popen(["find","/media/usb/files","-name", searchName,"-delete"],stdout=subprocess.PIPE)
		out = subprocess.Popen(["find","/home/pi/files","-name", searchName,"-delete"],stdout=subprocess.PIPE)
		return out
	
		



	
	


	
	
	
	
	
	
	

