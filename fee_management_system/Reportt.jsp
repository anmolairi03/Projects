<%@ page import="java.sql.*" %>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
    try {
        // Load the MySQL JDBC driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Establish a connection to the database
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fee_management", "root", "gadheullu12");

        // Query to fetch student names and total fee paid
        String sql = "SELECT students.name, SUM(payments.amount) AS total_paid " +
                     "FROM students " +
                     "LEFT JOIN payments ON students.id = payments.student_id " +
                     "GROUP BY students.id";
        Statement stmt = con.createStatement();
        ResultSet rs = stmt.executeQuery(sql);

        // Start generating the HTML table
        out.println("<table border='1'>");
        out.println("<thead>");
        out.println("<tr>");
        out.println("<th>Student Name</th>");
        out.println("<th>Total Fee Paid</th>");
        out.println("</tr>");
        out.println("</thead>");
        out.println("<tbody>");

        // Loop through the result set and generate table rows
        while (rs.next()) {
            out.println("<tr>");
            out.println("<td>" + rs.getString("name") + "</td>");

            double totalPaid = rs.getDouble("total_paid");
            if (rs.wasNull()) {
                totalPaid = 0.0; // Set to 0 if NULL
            }
            out.println("<td>₹" + String.format("%.2f", totalPaid) + "</td>");
            out.println("</tr>");
        }

        // Close the table
        out.println("</tbody>");
        out.println("</table>");

        // Close the connection
        rs.close();
        stmt.close();
        con.close();
    } catch (Exception e) {
        // Log the error and display an error message
        e.printStackTrace();
        out.println("<p style='color: red;'>Error loading data. Please try again later.</p>");
    }
%>