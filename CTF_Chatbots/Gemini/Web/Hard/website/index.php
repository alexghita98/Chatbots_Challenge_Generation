<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Reports</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background-color: #f0f0f0; }
        .container { background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); width: 600px; text-align: center; }
        h1 { color: #333; margin-bottom: 20px; }
        p { color: #555; line-height: 1.6; }
        .reports-list { list-style: none; padding: 0; }
        .reports-list li { margin-bottom: 10px; }
        .reports-list li a { text-decoration: none; color: #007bff; font-weight: bold; }
        .reports-list li a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Employee Report Viewer</h1>
        <p>You can view public employee reports using the links below. Some reports might be restricted.</p>
        <ul class="reports-list">
            <li><a href="report.php?id=1">View Report for Employee ID 1</a></li>
            <li><a href="report.php?id=2">View Report for Employee ID 2</a></li>
            <li><a href="report.php?id=3">View Report for Employee ID 3</a></li>
            <li><a href="report.php?id=4">View Report for Employee ID 4</a></li>
            <li><a href="report.php?id=5">View Report for Employee ID 5</a></li>
            </ul>
        <p>Happy exploring!</p>
    </div>
</body>
</html>