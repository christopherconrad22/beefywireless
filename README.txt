BeefyWireless by Chris Conrad

Summary: BeefWireless generates a password using two user chosen salts, uses SHA512 to hash the salt + the user chosen password (8 characters or more), then encodes the resulting hash using Base91 and lastly truncates the final result down to 63 characters to fit into the WPA2 password field. 

christopherconrad22@gmail.com
