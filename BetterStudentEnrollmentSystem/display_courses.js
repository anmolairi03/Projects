document.addEventListener("DOMContentLoaded", function () {
    fetch('courses.xml')
        .then(response => response.text())
        .then(data => {
            console.log("✅ XML Loaded Successfully:\n", data); 

            let parser = new DOMParser();
            let xml = parser.parseFromString(data, "application/xml");  
            let courses = xml.getElementsByTagName("course"); // Use getElementsByTagName correctly

            console.log("📌 Parsed Courses:", courses); 

            if (courses.length === 0) {
                console.error("❌ No courses found in XML");
                return;
            }

            let courseList = document.getElementById("courseList");
            if (!courseList) {
                console.error("❌ courseList element not found");
                return;
            }

            let output = `
                <table>
                    <tr>
                        <th>Course Name</th>
                        <th>Code</th>
                        <th>Duration</th>
                        <th>Eligibility</th>
                        <th>Fees</th>
                    </tr>`;

            for (let i = 0; i < courses.length; i++) {
                let name = courses[i].getElementsByTagName("name")[0]?.textContent || "N/A";
                let code = courses[i].getElementsByTagName("code")[0]?.textContent || "N/A";
                let duration = courses[i].getElementsByTagName("duration")[0]?.textContent || "N/A";
                let eligibility = courses[i].getElementsByTagName("eligibility")[0]?.textContent || "N/A";
                let fees = courses[i].getElementsByTagName("fees")[0]?.textContent || "N/A";

                console.log(`📝 Course ${i + 1}:`, { name, code, duration, eligibility, fees });

                output += `
                    <tr>
                        <td>${name}</td>
                        <td>${code}</td>
                        <td>${duration}</td>
                        <td>${eligibility}</td>
                        <td>₹${fees}</td>
                    </tr>`;
            }

            output += "</table>";
            courseList.innerHTML = output;
        })
        .catch(error => console.error("❌ Error loading XML:", error));
});
