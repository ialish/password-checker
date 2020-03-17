## Password Checker

This password checker is a secure way to check if the password has ever been hacked.

**From the terminal:**<br>
`$ python checkmypass.py <1st-password-to-check> <2nd-password>` . . .

**Example**<br>
`$ python password_checker.py hello password123 kjfdklgjdfjd`<br>
`hello was found 253581 times`<br>
`password123 was found 121251 times`<br>
`kjfdklgjdfjd was NOT found`<br>

### Searching by range
Source: [https://haveibeenpwned.com/API/v3](https://haveibeenpwned.com/API/v3)

In order to protect the value of the source password being searched for, Pwned Passwords also implements a k-Anonymity model that allows a password to be searched for by partial hash. This allows the first 5 characters of a SHA-1 password hash (not case-sensitive) to be passed to the API (testable by clicking here):
GET https://api.pwnedpasswords.com/range/{first 5 hash chars}
(SHA1 Hash Generator)

When a password hash with the same first 5 characters is found in the Pwned Passwords repository, the API will respond with an HTTP 200 and include the suffix of every hash beginning with the specified prefix, followed by a count of how many times it appears in the data set. The API consumer can then search the results of the response for the presence of their source hash and if not found, the password does not exist in the data set. A sample response for the hash prefix "21BD1" would be as follows:
0018A45C4D1DEF81644B54AB7F969B88D65:1
00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2
011053FD0102E94D6AE2F8B83D76FAF94F6:1
012A7CA357541F0AC487871FEEC1891C49C:2
0136E006E24E7D152139815FB0FC6A50B15:2
…

A range search typically returns approximately 500 hash suffixes, although this number will differ depending on the hash prefix being searched for and will increase as more passwords are added. There are 1,048,576 different hash prefixes between 00000 and FFFFF (16^5) and every single one will return HTTP 200; there is no circumstance in which the API should return HTTP 404.
Code
Body
Description
200
Hash suffixes counts.
Ok — all password hashes beginning with the searched prefix are returned alongside prevalence counts.

Read more about how k-Anonymity and the Pwned Passwords range search protects searched passwords.
