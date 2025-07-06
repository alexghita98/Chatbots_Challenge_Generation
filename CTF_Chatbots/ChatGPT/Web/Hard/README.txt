SQL Injection 101 (Hard)

Description:
A classic SQL injection challenge. The login form is vulnerable.

Flag:
flag{classic_sql_injection_win}

Write-up:
Bypass the login with: `user=admin'--` and any password. This closes the string and comments out the rest of the query.
