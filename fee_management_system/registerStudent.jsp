<%@ page import="java.sql.*" %>
<%
    if ("POST".equalsIgnoreCase(request.getMethod())) {
        // Get form data
        String id = request.getParameter("id"); // User-defined ID
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String phone = request.getParameter("phone");

        try {
            // Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish a connection to the database
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fee_management", "root", "gadheullu12");

            // Check if the ID already exists
            String checkSql = "SELECT * FROM students WHERE id = ?";
            PreparedStatement checkStmt = con.prepareStatement(checkSql);
            checkStmt.setInt(1, Integer.parseInt(id));
            ResultSet rs = checkStmt.executeQuery();

            if (rs.next()) {
                // ID already exists
                out.println("<p style='color: red;'>Error: ID already exists. Please enter a unique ID.</p>");
            } else {
                // Insert the new student record with the user-defined ID
                String insertSql = "INSERT INTO students (id, name, email, phone) VALUES (?, ?, ?, ?)";
                PreparedStatement insertStmt = con.prepareStatement(insertSql);
                insertStmt.setInt(1, Integer.parseInt(id));
                insertStmt.setString(2, name);
                insertStmt.setString(3, email);
                insertStmt.setString(4, phone);
                int rowsInserted = insertStmt.executeUpdate();

                if (rowsInserted > 0) {
                    out.println("<p style='color: green;'>Student registered successfully!</p>");
                } else {
                    out.println("<p style='color: red;'>Error: Failed to register student.</p>");
                }

                // Close the insert statement
                insertStmt.close();
            }

            // Close the check statement and result set
            rs.close();
            checkStmt.close();

            // Close the connection
            con.close();
        } catch (ClassNotFoundException e) {
            out.println("<p style='color: red;'>Error: MySQL JDBC driver not found. Please add the driver to your classpath.</p>");
        } catch (SQLException e) {
            out.println("<p style='color: red;'>Error: " + e.getMessage() + "</p>");
        } catch (NumberFormatException e) {
            out.println("<p style='color: red;'>Error: ID must be a valid number.</p>");
        }
    } else {
        out.println("<p style='color: red;'>Error: Invalid request method. Use POST to submit the form.</p>");
    }
%>