Cookie Monster (Medium)

Description:
This web page sets a cookie named 'role'. Can you become an admin?

Flag:
flag{cookie_privilege_escalation}

Write-up:
Visit the /set endpoint to receive a cookie. Then, using browser dev tools or an intercepting proxy like Burp, change the 'role' cookie from 'guest' to 'admin' and revisit the home page to retrieve the flag.
