#	Chris Conrad 2/25/2014
#	Simple script to hash a password using SHA512
#	and to shorten to 63 characters for maximum
#	length using WPA wireless security

import hashlib
import getpass

pswd1 = getpass.getpass('Enter the wireless PW you wish to secure:')
hash1 = hashlib.sha512(pswd1).hexdigest()
pswd1 = None

pswd2 = getpass.getpass('Re-enter the wireless PW you wish to secure:')
hash2 = hashlib.sha512(pswd2).hexdigest()
pswd2 = None

while hash1 != hash2:
	print("Passwords did not match, try again!")
	pswd1 = getpass.getpass(' Enter the wireless PW you wish to secure:')
	hash1 = hashlib.sha512(pswd1).hexdigest()
	pswd1 = None
	pswd2 = getpass.getpass(' Re-enter the wireless PW you wish to secure:')
	hash2 = hashlib.sha512(pswd2).hexdigest()
	pswd2 = None

concatenated_pw = hash1[0:63]
hash1 = None
hash2 = None
print("Your new password: " + concatenated_pw)
concatenated_pw = None

