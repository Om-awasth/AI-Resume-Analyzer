import os
import smtplib
from email.message import EmailMessage


def _smtp_configured():
    return bool(os.environ.get('SMTP_HOST') and os.environ.get('SMTP_USER') and os.environ.get('SMTP_PASS'))


def send_email(to_address, subject, plain_text, html_text=None):
    """Send an email via SMTP using environment vars.

    Env vars:
      SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SMTP_SECURE (true/false), FROM_EMAIL

    Returns (True, info) on success or (False, reason) on failure.
    """
    if not _smtp_configured():
        return False, 'smtp not configured'

    host = os.environ.get('SMTP_HOST')
    port = int(os.environ.get('SMTP_PORT') or 587)
    user = os.environ.get('SMTP_USER')
    password = os.environ.get('SMTP_PASS')
    secure = os.environ.get('SMTP_SECURE', 'false').lower() == 'true'
    from_addr = os.environ.get('FROM_EMAIL') or user

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_address
    msg.set_content(plain_text)
    if html_text:
        msg.add_alternative(html_text, subtype='html')

    try:
        if secure:
            smtp = smtplib.SMTP_SSL(host, port, timeout=10)
        else:
            smtp = smtplib.SMTP(host, port, timeout=10)
            smtp.ehlo()
            try:
                smtp.starttls()
            except Exception:
                pass

        smtp.login(user, password)
        smtp.send_message(msg)
        smtp.quit()
        return True, 'sent'
    except Exception as e:
        return False, str(e)
