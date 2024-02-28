from django.core.mail import send_mail

def send_registration_confirmation_email(email):
    subject = 'Sikeres regisztráció'
    message = """
                <!DOCTYPE html>
                <html lang="hu">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Regisztráció megerősítése</title>
                </head>
                <body>
                    <div style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
                        <h1 style="color: #333333;">Köszönjük, hogy regisztráltál!</h1>
                        <p style="color: #666666;">Sikeres üzleteket kíván a Rosszfogás!</p>
                        <p style="color: #666666;">Üdvözlettel,</p>
                        <p style="color: #666666;">A Rosszfogás csapata</p>
                    </div>
                </body>
                </html>
                """
    from_email = 'rosszfogas.noreply@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)