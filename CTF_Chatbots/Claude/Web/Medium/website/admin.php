<?php
if (isset($_COOKIE['user_role']) && $_COOKIE['user_role'] == 'admin') {
    echo "<h1>Admin Panel</h1>";
    echo "<p>Welcome, admin!</p>";
    echo "<p>Here's your flag: <strong>FLAG{cookie_manipulation_master}</strong></p>";
} else {
    echo "<h1>Access Denied</h1>";
    echo "<p>You don't have admin privileges.</p>";
}
?>