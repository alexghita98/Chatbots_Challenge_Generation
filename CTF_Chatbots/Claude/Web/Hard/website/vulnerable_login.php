<?php
if ($_POST['username'] && $_POST['password']) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    // Vulnerable SQL query (for educational purposes only)
    $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    
    // Simulate SQL injection vulnerability
    if (strpos($username, "' OR '1'='1'") !== false || strpos($username, "admin' OR 1=1") !== false) {
        echo "<h1>Login Successful!</h1>";
        echo "<p>FLAG{sql_injection_detected}</p>";
    } else {
        echo "<h1>Login Failed</h1>";
        echo "<p>Invalid credentials.</p>";
    }
}
?>
<html>
<head><title>Login</title></head>
<body>
    <h1>Secure Login</h1>
    <form method="post">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>