require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');

const app = express();
app.use(express.json());

async function createTransporter() {
  if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
    return nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: Number(process.env.SMTP_PORT || 587),
      secure: process.env.SMTP_SECURE === 'true',
      auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS }
    });
  }
  // dev: Ethereal test account
  const testAccount = await nodemailer.createTestAccount();
  return nodemailer.createTransport({
    host: testAccount.smtp.host,
    port: testAccount.smtp.port,
    secure: testAccount.smtp.secure,
    auth: { user: testAccount.user, pass: testAccount.pass }
  });
}

app.post('/send-reset', async (req, res) => {
  const { to, subject, text, html } = req.body || {};
  if (!to) return res.status(400).json({ error: 'to required' });

  try {
    const transporter = await createTransporter();
    const info = await transporter.sendMail({
      from: process.env.FROM_EMAIL || process.env.SMTP_USER || 'no-reply@example.com',
      to,
      subject: subject || 'Password reset',
      text: text || '',
      html: html || undefined
    });

    const preview = nodemailer.getTestMessageUrl(info);
    return res.json({ ok: true, messageId: info.messageId, preview });
  } catch (err) {
    console.error('send error', err);
    return res.status(500).json({ ok: false, error: err.message });
  }
});

const PORT = process.env.PORT || 3020;
app.listen(PORT, () => console.log(`Email service listening on ${PORT}`));
