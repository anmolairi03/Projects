<%@ page import="java.sql.*" %>
<%
    try {
        // Load the MySQL JDBC driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Establish a connection to the database
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fee_management", "root", "gadheullu12");

        // Delete all records from the payments table
        String sql1 = "DELETE FROM payments";
        Statement stmt1 = con.createStatement();
        stmt1.executeUpdate(sql1);

        // Delete all records from the students table
        String sql2 = "DELETE FROM students";
        Statement stmt2 = con.createStatement();
        stmt2.executeUpdate(sql2);

        // Close the connection
        stmt1.close();
        stmt2.close();
        con.close();

        // Redirect back to the report page
        response.sendRedirect("report.jsp");
    } catch (Exception e) {
        // Log the error and display an error message
        e.printStackTrace();
        out.println("<p style='color: red;'>Error clearing data. Please try again later.</p>");
    }
%>