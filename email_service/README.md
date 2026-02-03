# Resume Analyzer Email Service

Simple Node.js microservice to send password-reset emails using `nodemailer`.

Environment variables:

- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_SECURE` (true/false)
- `FROM_EMAIL` (optional)

If SMTP vars are not set the service uses Ethereal (dev) and returns a preview URL.

Run:

```bash
cd email_service
npm install
npm start
```

Send email (example):

```bash
curl -X POST http://localhost:3020/send-reset \
  -H "Content-Type: application/json" \
  -d '{"to":"you@example.com","subject":"Reset","text":"Your token: 12345"}'
```
