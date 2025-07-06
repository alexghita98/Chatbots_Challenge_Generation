<?php
$user = $_GET['user'];
$pass = $_GET['pass'];
$conn = new mysqli('localhost', 'root', '', 'ctf');
$query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
$result = $conn->query($query);
if($result->num_rows > 0) { echo 'flag{classic_sql_injection_win}'; } else { echo 'Try again'; } ?>