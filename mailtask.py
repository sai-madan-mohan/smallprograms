def send_bulk_email_batch(email_batches, subject):
    """
    Asynchronous Celery Task to send emails in bulk.
    `email_data` is a list of tuples containing (email, personalized_body).
    """
    for email_data in email_batches:
        for email, personalized_body in email_data:
            # Email Template Rendering
            sign_off = "Sincerely,<br>Team Infyni"
            email_context = {"greetings": personalized_body, "sign_off": sign_off}
            html_content = render_to_string("email_notification_base.html", {"email_body": email_context, "NEW_HOST_URL": HOST_URL})
            # Send email
            send_email_background(
                recipient_id=None,
                notification_text=None,
                email_subject=subject,
                email_list=[email],
                html_content=html_content
            )
        return f"Sent {len(email_data)} emails"
    
    """local function"""