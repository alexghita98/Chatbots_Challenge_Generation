<?php
// In a real application, proper authentication and authorization would be here.
// For this challenge, the IDOR vulnerability exists because it relies only on the ID parameter.

$report_id = isset($_GET['id']) ? (int)$_GET['id'] : 0; // Cast to int for safety, but vulnerability remains

$reports = [
    1 => "This is a general employee performance review for Employee ID 1. Nothing sensitive here.",
    2 => "Monthly sales report for Employee ID 2. All good.",
    3 => "Employee ID 3's project update. Standard information.",
    4 => "Attendance record for Employee ID 4. Regular working hours.",
    5 => "Training completion certificate for Employee ID 5.",
    6 => "Employee ID 6's benefits enrollment details.",
    7 => "Travel expenses for Employee ID 7.",
    8 => "Performance metrics for Employee ID 8.",
    9 => "Daily activity log for Employee ID 9.",
    10 => "<h2>CEO's Top Secret Report!</h2><p>This report contains highly confidential strategic plans. Access to this document is strictly limited!</p><p>The flag is: <strong style='color: green;'>flag{idor_exposes_sensitive_data}</strong></p><p>You should not be seeing this!</p>",
];

$report_content = $reports[$report_id] ?? "<h1>Report Not Found</h1><p>The report for the requested ID doesposes not exist or you do not have permission.</p>";

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report ID: <?php echo htmlspecialchars($report_id); ?></title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background-color: #f0f0f0; }
        .report-container { background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); width: 700px; text-align: left; }
        h1 { color: #333; margin-bottom: 20px; text-align: center; }
        h2 { color: #0056b3; margin-bottom: 15px; }
        p { color: #555; line-height: 1.6; }
        .back-link { display: block; margin-top: 20px; text-align: center; }
        .back-link a { text-decoration: none; color: #007bff; font-weight: bold; }
        .back-link a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="report-container">
        <h1>Report Details (ID: <?php echo htmlspecialchars($report_id); ?>)</h1>
        <?php echo $report_content; ?>
        <div class="back-link">
            <a href="index.php">Back to Report List</a>
        </div>
    </div>
</body>
</html>