<?php
$message_sent = false;
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    
    // Validate the input
    if (!empty($name) && !empty($email) && !empty($message)) {
        // Prepare email information
        $to = "your-email@example.com";
        $subject = "New Contact Form Submission";
        $body = "Name: $name\nEmail: $email\nMessage: $message";
        $headers = "From: $email";
        
        // Send email
        if (mail($to, $subject, $body, $headers)) {
            $message_sent = true;
        } else {
            $error_message = "Failed to send the message!";
        }
    } else {
        $error_message = "All fields are required!";
    }
}
?>
