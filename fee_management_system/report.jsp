<!DOCTYPE html>
<html>
<head>
    <title>Fee Report</title>
    <meta charset="UTF-8">
    <style>
        /* Add your CSS styles here */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .report-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 800px;
            text-align: center;
            margin-top: 80px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            padding: 10px;
            border: 1px solid #ccc;
        }

        th {
            background-color: #23a6d5;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        .error-message {
            color: red;
            font-weight: bold;
        }

        .clearReport {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #ff4d4d;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .clearReport:hover {
            background-color: #ff1a1a;
        }
    </style>
</head>
<body>
    <div class="report-container">
        <h2>Fee Report</h2>
        <!-- Include the Reportt.jsp file to display the table -->
        <%@ include file="Reportt.jsp" %>
        <!-- Clear Report Button -->

        <!-- Clear Data Button -->
        <form action="clearData.jsp" method="post">
            <button class=" clearReport" type="submit">Clear Data from Database</button>
        </form>
    </div>
</body>
</html>