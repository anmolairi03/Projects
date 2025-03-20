<%@ page import="java.sql.*" %>
<%
    if ("POST".equalsIgnoreCase(request.getMethod())) {
        String studentId = request.getParameter("studentId");
        String amount = request.getParameter("amount");

        try {
            // Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish a connection to the database
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fee_management", "root", "gadheullu12");

            // Check if the student_id exists in the students table
            String checkStudentSql = "SELECT id FROM students WHERE id = ?";
            PreparedStatement checkStudentStmt = con.prepareStatement(checkStudentSql);
            checkStudentStmt.setString(1, studentId);
            ResultSet rs = checkStudentStmt.executeQuery();

            if (rs.next()) {
                // Insert payment data into the database
                String sql = "INSERT INTO payments (student_id, amount) VALUES (?, ?)";
                PreparedStatement ps = con.prepareStatement(sql);
                ps.setString(1, studentId);
                ps.setString(2, amount);
                int rowsInserted = ps.executeUpdate();

                if (rowsInserted > 0) {
                    out.println("Payment processed successfully!");
                } else {
                    out.println("Error: Failed to process payment.");
                }

                // Close the statement
                ps.close();
            } else {
                out.println("Error: Invalid student ID. The student does not exist.");
            }

            // Close the connection
            checkStudentStmt.close();
            con.close();
        } catch (ClassNotFoundException e) {
            out.println("Error: MySQL JDBC driver not found. Please add the driver to your classpath.");
        } catch (SQLException e) {
            out.println("Error: " + e.getMessage());
        }
    } else {
        out.println("Error: Invalid request method. Use POST to submit the form.");
    }
%>