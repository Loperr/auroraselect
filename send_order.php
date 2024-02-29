<?php
// Configuration
$to = 'neo2_neo@mail.ru';
$subject = 'New Order Received';
$headers = "From: $from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";
$headers .= "Content-type: text/plain; charset=UTF-8 \r\n";

// Visitor's Information
$name = $_POST['name'];
$email = $_POST['email'];
$product = $_POST['product'];
$quantity = $_POST['quantity'];

// Send the email
mail($to, $subject, $message, $headers);

// Redirect back to the order form
header('Location: index.html');
?>
