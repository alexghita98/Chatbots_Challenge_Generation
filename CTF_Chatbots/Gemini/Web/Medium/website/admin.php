<?php
session_start();

// Ensure the user is generally logged in via session
$is_logged_in_session = isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true;

// **VULNERABILITY POINT:** Also check a client-side cookie for admin status
$is_admin_cookie = isset($_COOKIE['admin_status']) && $_COOKIE['admin_status'] === 'true';

// If not logged in at all (even as a regular user), redirect to login
if (!$is_logged_in_session) {
    header("Location: login.php");
    exit();
}

// Crucial check: Is the user an admin according to the *client-side cookie*?
// This is the bypass. Even if $_SESSION['role'] is 'user', the cookie grants access.
if (!$is_admin_cookie) {
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Access Denied</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background-color: #f0f0f0; }
            .container { text-align: center; padding: 40px; border-radius: 8px; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            h1 { color: #dc3545; }
            p { color: #666; }
            a { color: #007bff; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Access Denied!</h1>
            <p>You do not have administrative privileges to view this page. (Hint: Check your cookies!)</p>
            <p><a href="login.php">Go back to login</a></p>
        </div>
    </body>
    </html>';
    exit();
}

// If the user is logged in AND the admin_status cookie is 'true', display the flag
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background-color: #e9f7ef; }
        .container { text-align: center; padding: 40px; border-radius: 8px; background-color: #d4edda; border: 1px solid #28a745; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #28a745; margin-bottom: 20px; }
        p { color: #155724; line-height: 1.6; }
        .flag { font-family: 'Courier New', monospace; font-size: 1.2em; color: #000; background-color: #fff; padding: 10px 15px; border-radius: 5px; display: inline-block; margin-top: 20px; border: 1px dashed #666; }
        a { color: #007bff; text-decoration: none; margin-top: 20px; display: inline-block; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Admin Panel!</h1>
        <p>Congratulations, you've successfully bypassed the restrictions!</p>
        <p>This is highly sensitive information that only true administrators should see.</p>
        <p>Your flag is:</p>
        <p class="flag">flag{insecure_authentication_is_bad}</p>
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>