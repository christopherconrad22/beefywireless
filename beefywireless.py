# BeefyWireless password generator
#
# Copyright (c) 2014 Christopher Todd Conrad
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# * Neither the name of Christopher Todd Conrad nor the names
# of its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import hashlib
import getpass
import base91

mname1 = getpass.getpass('Enter your moms madiem name:')
mname2 = getpass.getpass('Re-enter your moms madiem name:')

while mname1 != mname2 or len(mname1) == 0:
	if(mname1 != mname2):
		print("   ** Madien names did not match, try again! ** ")
	if(len(mname1) == 0):
		print("   ** Madien name must be at least one character long ** ")
	mname1 = getpass.getpass(' Enter your moms madiem name:')
	mname2 = getpass.getpass(' Re-enter your moms madiem name:')

born1 = getpass.getpass('Enter the name of the hospitable you were born in:')
born2 = getpass.getpass('Re-enter the name of the hospitable you were born in:')

while born1 != born2 or len(born1) == 0:
	if(born1 != born2):
		print("   ** Hospitable names did not match, try again! ** ")
	if(len(born1) == 0):
		print("   ** Hospitable name must be at least one character long ** ")
	born1 = getpass.getpass(' Enter the name of the hospitable you were born in:')
	born2 = getpass.getpass(' Re-enter the name of the hospitable you were born in:')

salt1 = hashlib.sha512(mname1).hexdigest()
salt2 = hashlib.sha512(born1).hexdigest()
salted = (salt1[0:64] + salt2[0:64])

pswd1 = getpass.getpass('Enter the wireless PW you wish to secure:')
pswd2 = getpass.getpass('Re-enter the wireless PW you wish to secure:')

while pswd1 != pswd2 or len(pswd1) < 8:
	if (pswd1 != pswd2):
		print("   ** Passwords did not match, try again!")
	if (len(pswd1) < 8):
		print("   ** Password must be at least 8 characters long!")
	pswd1 = getpass.getpass(' Enter the wireless PW you wish to secure:')
	pswd2 = getpass.getpass(' Re-enter the wireless PW you wish to secure:')

hashed_pw = hashlib.sha512(salted+pswd1).hexdigest()
base91_pw = base91.encode(hashed_pw)
print("Your new password: " + base91_pw[0:63])

hashed_pw = None
pswd1 = None
pswd2 = None
salt1 = None
salt2 = None
salted = None

