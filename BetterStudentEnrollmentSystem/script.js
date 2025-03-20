document.getElementById("enrollmentForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let mobile = document.getElementById("mobile").value;
    let course = document.getElementById("course").value;
    
    if (!validateEmail(email)) {
        alert("Invalid email format!");
        return;
    }

    document.getElementById("confirmationMessage").textContent = `Thank you, ${name}! You have successfully enrolled in ${course}.`;
});

function validateEmail(email) {
    let re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
}
