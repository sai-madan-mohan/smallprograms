class AdminSendEmailsView(View):
    MAX_EMAILS = 1000  

    def get(self, request):
        return render(request, "admin_send_emails.html", {})

    def post(self, request):
        subject = request.POST.get("subject", "").strip()
        email_body_template = request.POST.get("email_body", "").strip()
        email_list, unique_emails = [], set()

        def add_email(email, first_name="User"):
            """Helper function to add an email with personalization."""
            if email and "@" in email and email.endswith(".com") and email not in unique_emails:
                unique_emails.add(email)
                email_list.append((email, email_body_template.replace("{name}", first_name)))
            else:
                messages.error(request, f"Invalid email format: {email}. Email must contain '@' and end with '.com'.")
            return len(email_list) >= self.MAX_EMAILS  # Stop if limit reached

        # Process manual emails
        manual_emails = request.POST.get("manual_emails", "").strip()
        if manual_emails:
            for email in {e.strip() for e in manual_emails.split(",") if e.strip()}:
                if add_email(email):
                    break # Stop processing once max limit is reached

        # Process uploaded Excel file
        file = request.FILES.get('excel_file')
        if file:
            # Validate file format
            if not file.name.endswith(('.csv', '.xlsx', '.xls')):  # Include .xls for compatibility
                messages.error(request, "Invalid file format! Please upload a CSV or Excel file.")
                return redirect(request.META.get('HTTP_REFERER', '/'))
            try:
                df = pd.read_excel(file, engine='openpyxl') if file.name.endswith(('.xls', '.xlsx')) else pd.read_csv(file)
                email_col = next((col for col in ['Email', 'email', 'email_address'] if col in df.columns), None)
                first_name_col = next((col for col in ['First Name', 'first_name', 'Name'] if col in df.columns), None)

                if not email_col:
                    messages.error(request, "Excel file must contain an 'Email' column.")
                    return redirect("yoshimitsujpinfy:admin_send_emails")

                # Using vectorized operations for speed (instead of iterrows)
                for _, row in df.iterrows():
                    email = str(row[email_col]).strip()
                    first_name = str(row[first_name_col]).strip() if first_name_col and pd.notna(row[first_name_col]) else "User"
                    if add_email(email, first_name):
                        break  # Stop processing once max limit is reached

            except Exception as e:
                messages.error(request, f"Error reading file: {e}")
                return redirect("yoshimitsujpinfy:admin_send_emails")

        if not email_list:
            messages.error(request, "Please enter at least one recipient email.")
            return redirect("yoshimitsujpinfy:admin_send_emails")

        # **Batch Emails for Celery Processing**
        batch_size = 500  # Break into smaller batches for performance
        email_batches = [email_list[i:i + batch_size] for i in range(0, len(email_list), batch_size)]
        task_group = send_bulk_email_batch(email_batches, subject)

        # task_group = group(send_bulk_email_batch.s(batch, subject) for batch in email_batches)
        # task_group.apply_async()
        
        messages.success(request, f" {len(email_list)} emails sent successfully!")
        return redirect("yoshimitsujpinfy:admin_send_emails")
        