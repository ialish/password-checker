## Password Checker

This password checker is a secure way to check if the password as ever been hacked.

From the terminal:
$ python checkmypass.py <1st-password-to-check> <2nd-password> ...

### Example

$ python checkmypass.py hello password123 kjfdklgjdffjdhshdjfk
hello was hacked 253581 times... you should change your password
password123 hacked found 121251 times... you should change your password
kjfdklgjdffjdhshdjfk was NEVER been hacked. Carry on!

