import sys
import subprocess

class admin:
	"""This is a class manages the users who use the system  and also allows user to be created, check if the user exists, check the users password

    """

	
	def createUser(self,name,password):
		"""Writes the name and password of the user in a textfile in a newline

		:param name: This is the name the user will use to login.
		:type name: string
		:param password: This is the password the user uses to sign in
		:type password: string
		"""
		file1 = open(r"/home/pi/Design/users.txt","a")
		line = name+" "+password + "\n"
		file1.writelines(line)
	
	
	def check(self,name,password):
		"""[checks if the user is registered user, does this by checking if they're name and password is in the textfile.The name should also match the corresponding password.]

		:param name: [This is the name the user uses to login]
		:type name: [string]
		:param password: [This is the password the user will uses to login.]
		:type password: [string]
		:return: [Returns True if the user was successfuly validated and False if the user was not successfuly validated.]
		:rtype: [bool]
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] and password == splitList[1]):
				return True
		return False

	def checkPassword(self,name):
		"""[Takes in a username and returns the corresponding password to the username]

		:param name: [This is the name the user uses to login.]
		:type name: [string]
		:return: [plitList[0] which is the password of the user or Not found (str): Returns a ``Not found`` string if the corresponding username is not registered]
		:rtype: [string]
		"""
		file1 = open(r"/home/pi/Design/users.txt","r")
		lines = file1.readlines()

		for line in lines:
			splitList = line.split()

			if(name == splitList[0] ):
				return splitList[1]

		return "Not found"

	def makeAdmin(username,password):
		"""Function that takes the username and password of a user and makes them an admin

		:param username: The username the individual will uses to login
		:type username: string
		:param password: The password the individual uses to login
		:type password: string
		"""
				

		with open(r"/home/pi/Design/users.txt", "r") as f:
			lines = f.readlines()
		
		with open(r"/home/pi/Design/users.txt", "a") as f:	
			for line in lines:
				splitList = line.split()	
				if len(splitList)==0:
					pass
				
				if(username == splitList[0] and password == splitList[1]):
					line = username+" "+password +" "+"admin"+"\n"
					f.writelines(line)
					return True
		
		return False


	def deleteUser(username,password):
		"""Functions that deletes a registered user from the list of registered users

		:param username: The username the individual uses to log in
		:type username: string
		:param password: The password the user uses to log in
		:type password: String
		"""
		with open(r"/home/pi/Design/users.txt", "r") as f:
			lines = f.readlines()
		
		with open(r"/home/pi/Design/users.txt", "w") as f:
			for line in lines:
				splitList = line.split()
				
				if len(splitList) == 0:
					pass
			
				if(username != splitList[0] and password != splitList[1]):
					f.write(line)
				
	def checkAdmin(username,password):
		"""Function that checks if a user is an admin

		:param username: The username the user uses to log in
		:type username: string
		:param password: The password the user uses to log in
		:type password: string
		:return: Returns true if the user is an admin
		:rtype: Returns false if the user is not an admin
		"""
		with open(r"/home/pi/Design/users.txt", "r") as f:
			lines = f.readlines()
		
			for line in lines:
				splitList = line.split()	
				if len(splitList)==3:
					if splitList[2] == "admin":
						return True
				
		return False

		
