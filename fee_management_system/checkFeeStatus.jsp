<%@ page import="java.sql.*" %>
<%
    String studentId = request.getParameter("studentId");

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fee_management", "root", "gadheullu12");
        PreparedStatement ps = con.prepareStatement("SELECT SUM(amount) AS total_paid FROM payments WHERE student_id = ?");
        ps.setString(1, studentId);
        ResultSet rs = ps.executeQuery();

        if (rs.next()) {
            out.println("Total Fee Paid: " + rs.getDouble("total_paid"));
        } else {
            out.println("No payments found for this student.");
        }
    } catch (Exception e) {
        out.println("Error: " + e.getMessage());
    }
%>