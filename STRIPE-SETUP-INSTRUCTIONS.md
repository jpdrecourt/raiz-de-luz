# Stripe Setup Instructions for Voucher Sales

This guide will help you set up Stripe to accept voucher payments on your GitHub Pages site with a **manual Canva workflow**.

## Overview

**Workflow:**
1. Customer fills voucher form on your website
2. Customer completes payment via Stripe
3. You receive email notification with voucher details
4. You create personalized voucher in Canva
5. You email the voucher PDF to customer

---

## Step 1: Create Stripe Account

1. Go to [https://stripe.com](https://stripe.com)
2. Click **Sign Up** (or **Start now**)
3. Create your account with business email (info@raizdeluz.eu)
4. Complete business verification (required to receive payments)
5. Enable your account in Portugal (EUR currency)

**Important:** Keep your account in **Test Mode** until you're ready to go live.

---

## Step 2: Create Products in Stripe

You'll create products for each voucher type so customers can purchase them.

### 2.1 Access Products

1. Log into [Stripe Dashboard](https://dashboard.stripe.com)
2. Click **Products** in the left sidebar
3. Click **+ Add product**

### 2.2 Create Monetary Vouchers

Create these 4 products:

**Product 1: Vale de €50**
- Name: `Vale de €50`
- Description: `Vale personalizado de €50 para serviços Raiz de Luz`
- Pricing: **One-time payment** → `€50.00 EUR`
- Click **Save product**

**Product 2: Vale de €75**
- Name: `Vale de €75`
- Description: `Vale personalizado de €75 para serviços Raiz de Luz`
- Pricing: **One-time payment** → `€75.00 EUR`

**Product 3: Vale de €100**
- Name: `Vale de €100`
- Description: `Vale personalizado de €100 para serviços Raiz de Luz`
- Pricing: **One-time payment** → `€100.00 EUR`

**Product 4: Vale de €150**
- Name: `Vale de €150`
- Description: `Vale personalizado de €150 para serviços Raiz de Luz`
- Pricing: **One-time payment** → `€150.00 EUR`

### 2.3 Create Service Vouchers

Create these products for specific services:

**Massagem Terapêutica (60min)**
- Name: `Massagem Terapêutica (60min)`
- Description: `Vale para uma sessão de Massagem Terapêutica de 60 minutos`
- Pricing: `€60.00 EUR`

**Massagem Desportiva (60min)**
- Name: `Massagem Desportiva (60min)`
- Pricing: `€60.00 EUR`

**Massagem para Grávidas (60min)**
- Name: `Massagem para Grávidas (60min)`
- Pricing: `€65.00 EUR`

**Terapia Sacro Craniana (60min)**
- Name: `Terapia Sacro Craniana (60min)`
- Pricing: `€70.00 EUR`

**Drenagem Linfática (60min)**
- Name: `Drenagem Linfática (60min)`
- Pricing: `€65.00 EUR`

**Relaxamento (60min)**
- Name: `Relaxamento (60min)`
- Pricing: `€60.00 EUR`

**Pedras Quentes (90min)**
- Name: `Pedras Quentes (90min)`
- Pricing: `€90.00 EUR`

**Massagem Xamânica (90min)**
- Name: `Massagem Xamânica (90min)`
- Pricing: `€95.00 EUR`

> **Note:** Adjust prices according to your actual service rates.

---

## Step 3: Create Payment Links (Simple Option)

Payment Links are the easiest way to accept payments without a backend.

### 3.1 Create Payment Links

For **each product** you created:

1. Go to **Products** in Stripe Dashboard
2. Click on the product (e.g., "Vale de €50")
3. Click **Create payment link** button
4. Configure the payment link:
   - **Collect customer addresses**: Optional (set to "Don't collect")
   - **Collect phone numbers**: Optional
   - **Collect custom fields**: ✅ **IMPORTANT - Enable this!**
5. Click **Add custom field** and add these fields:
   - **Field 1:**
     - Label: `Nome do Destinatário`
     - Type: Text
     - Required: Yes
   - **Field 2:**
     - Label: `Email do Destinatário (opcional)`
     - Type: Text
     - Required: No
   - **Field 3:**
     - Label: `Nome do Remetente`
     - Type: Text
     - Required: Yes
   - **Field 4:**
     - Label: `Mensagem Pessoal (opcional)`
     - Type: Text
     - Required: No
   - **Field 5:**
     - Label: `Data de Entrega Preferida (opcional)`
     - Type: Text
     - Required: No
6. **After payment**: Select "Show success page" or redirect to your success page:
   - Redirect URL: `https://raizdeluz.eu/voucher-success.html`
7. Click **Create link**
8. **Copy the payment link URL** - you'll need this!

Repeat for all products.

### 3.2 Update Your Website Code

Now you need to update `voucher-checkout.js` to redirect to the appropriate payment link.

**Option A: Direct Payment Links (Simplest)**

Edit `docs/js/voucher-checkout.js` and replace the TODO section with:

```javascript
// Mapping of voucher types to Stripe Payment Links
const PAYMENT_LINKS = {
  '50': 'https://buy.stripe.com/XXXXX',           // Replace with actual link
  '75': 'https://buy.stripe.com/XXXXX',
  '100': 'https://buy.stripe.com/XXXXX',
  '150': 'https://buy.stripe.com/XXXXX',
  'service-therapeutic': 'https://buy.stripe.com/XXXXX',
  'service-sports': 'https://buy.stripe.com/XXXXX',
  'service-pregnancy': 'https://buy.stripe.com/XXXXX',
  'service-craniosacral': 'https://buy.stripe.com/XXXXX',
  'service-lymphatic': 'https://buy.stripe.com/XXXXX',
  'service-relaxation': 'https://buy.stripe.com/XXXXX',
  'service-hotstones': 'https://buy.stripe.com/XXXXX',
  'service-shamanic': 'https://buy.stripe.com/XXXXX',
};

// Get the payment link
const paymentLink = PAYMENT_LINKS[formData.voucherType];
if (!paymentLink) {
  throw new Error('Link de pagamento não configurado para este vale');
}

// Pre-fill the payment link with customer data (if supported)
const url = new URL(paymentLink);
url.searchParams.set('prefilled_email', formData.senderEmail);

// Redirect to Stripe Payment Link
window.location.href = url.toString();
```

**Limitation:** Payment Links don't support pre-filling custom fields, so customers will need to enter the voucher details twice (once on your form, once on Stripe). This is not ideal.

**Option B: Better UX - Use Stripe Checkout (Recommended)**

See **Step 4** below for a better integration that pre-fills all data.

---

## Step 4: Advanced Integration - Stripe Checkout (Recommended)

For better UX where customers only fill the form once, you need to use Stripe Checkout API.

### Requirements:
- A simple backend/serverless function to create checkout sessions
- Options: Netlify Functions, Vercel Functions, or Cloudflare Workers

### 4.1 Get Your Stripe API Keys

1. Go to [Stripe Dashboard](https://dashboard.stripe.com)
2. Click **Developers** → **API Keys**
3. Copy two keys:
   - **Publishable key** (starts with `pk_test_` for test mode)
   - **Secret key** (starts with `sk_test_` for test mode)

⚠️ **Never share or commit your Secret Key publicly!**

### 4.2 Update Publishable Key

Edit `docs/js/voucher-checkout.js`:

```javascript
const STRIPE_PUBLISHABLE_KEY = 'pk_test_YOUR_KEY_HERE'; // Replace with your actual key
```

### 4.3 Create a Backend Function (Example for Netlify)

Since GitHub Pages doesn't support backend code, you'll need to:

1. **Deploy to Netlify instead of GitHub Pages** (still free, easier setup)
2. Create a Netlify Function to create Stripe sessions

**Create file:** `netlify/functions/create-checkout.js`

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const data = JSON.parse(event.body);

    // Get price ID from environment variables
    const priceId = process.env[`PRICE_${data.voucherType}`];
    if (!priceId) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Invalid voucher type' }),
      };
    }

    // Create Checkout Session
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [
        {
          price: priceId,
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: `${process.env.URL}/voucher-success.html?email={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.URL}/vouchers.html`,
      customer_email: data.senderEmail,
      metadata: {
        voucher_type: data.voucherType,
        recipient_name: data.recipientName,
        recipient_email: data.recipientEmail || '',
        sender_name: data.senderName,
        sender_email: data.senderEmail,
        personal_message: data.personalMessage || '',
        delivery_date: data.deliveryDate || '',
      },
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ sessionId: session.id }),
    };
  } catch (error) {
    console.error('Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
```

### 4.4 Update Frontend Code

Edit `docs/js/voucher-checkout.js` and replace the TODO section with:

```javascript
// Call your backend function to create checkout session
const response = await fetch('/.netlify/functions/create-checkout', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(formData),
});

if (!response.ok) {
  throw new Error('Erro ao criar sessão de pagamento');
}

const { sessionId } = await response.json();

// Redirect to Stripe Checkout
const { error } = await stripe.redirectToCheckout({ sessionId });

if (error) {
  throw error;
}
```

### 4.5 Deploy to Netlify

1. Push your code to GitHub
2. Go to [Netlify](https://netlify.com) and sign up
3. Click **Add new site** → **Import an existing project**
4. Connect to your GitHub repository
5. Set build settings:
   - Base directory: (leave empty)
   - Publish directory: `docs`
   - Build command: (leave empty for static sites)
6. Add **Environment Variables** in Netlify:
   - `STRIPE_SECRET_KEY` = your secret key
   - `PRICE_50` = price ID for €50 voucher (from Stripe)
   - `PRICE_75` = price ID for €75 voucher
   - etc. (for each product)
7. Deploy!

To get Price IDs: Go to **Products** in Stripe → click product → copy the Price ID (starts with `price_`)

---

## Step 5: Set Up Email Notifications

You need to receive order details when someone purchases a voucher.

### Option 1: Stripe Email Receipts (Basic)

Stripe automatically sends email receipts to customers. You can also:

1. Go to **Settings** → **Emails** in Stripe Dashboard
2. Enable **Successful payments** notifications to your email
3. Customize the email template if needed

**Limitation:** Basic receipt, doesn't include custom metadata clearly.

### Option 2: Stripe Webhooks (Better)

Receive structured data when payment succeeds:

1. Go to **Developers** → **Webhooks** in Stripe
2. Click **Add endpoint**
3. Endpoint URL: Your webhook handler (requires backend)
   - If using Netlify, create another function: `/.netlify/functions/stripe-webhook`
4. Select events to listen to:
   - `checkout.session.completed`
5. Click **Add endpoint**
6. Copy the **Signing secret** (starts with `whsec_`)

**Create webhook handler:** `netlify/functions/stripe-webhook.js`

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
  const sig = event.headers['stripe-signature'];
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let stripeEvent;

  try {
    stripeEvent = stripe.webhooks.constructEvent(
      event.body,
      sig,
      webhookSecret
    );
  } catch (err) {
    return { statusCode: 400, body: `Webhook Error: ${err.message}` };
  }

  // Handle the event
  if (stripeEvent.type === 'checkout.session.completed') {
    const session = stripeEvent.data.object;
    const metadata = session.metadata;

    // TODO: Send email to yourself with voucher details
    // Use a service like SendGrid, Mailgun, or Formspree

    console.log('New voucher purchase:', {
      customerEmail: session.customer_email,
      amount: session.amount_total / 100,
      voucherType: metadata.voucher_type,
      recipientName: metadata.recipient_name,
      senderName: metadata.sender_name,
      message: metadata.personal_message,
    });

    // Example: Send email via SendGrid
    // const sgMail = require('@sendgrid/mail');
    // sgMail.setApiKey(process.env.SENDGRID_API_KEY);
    // await sgMail.send({
    //   to: 'info@raizdeluz.eu',
    //   from: 'orders@raizdeluz.eu',
    //   subject: 'New Voucher Purchase',
    //   html: `<h3>New voucher order!</h3>
    //          <p>Recipient: ${metadata.recipient_name}</p>
    //          <p>Sender: ${metadata.sender_name}</p>
    //          <p>Message: ${metadata.personal_message}</p>`,
    // });
  }

  return { statusCode: 200, body: JSON.stringify({ received: true }) };
};
```

Add environment variable in Netlify:
- `STRIPE_WEBHOOK_SECRET` = your webhook signing secret

### Option 3: Use Zapier/Make (No Code)

1. Sign up for [Zapier](https://zapier.com) or [Make](https://make.com)
2. Create a new automation (Zap/Scenario):
   - **Trigger:** Stripe - New Payment
   - **Action:** Email - Send Email (to yourself)
3. Map the fields to include metadata
4. Test and activate

---

## Step 6: Test the Complete Flow

### 6.1 Test Mode

1. Make sure Stripe is in **Test Mode** (toggle in dashboard)
2. Visit your vouchers page: `http://localhost:8000/vouchers.html`
3. Fill out the form
4. Use Stripe test card: `4242 4242 4242 4242`
   - Expiry: Any future date
   - CVC: Any 3 digits
   - ZIP: Any 5 digits
5. Complete payment
6. Verify you received notification email
7. Check Stripe Dashboard → **Payments** to see the test payment

### 6.2 Go Live

When ready to accept real payments:

1. Complete Stripe account verification
2. Switch to **Live Mode** (toggle in Stripe dashboard)
3. Get your **Live API keys** (pk_live_xxx and sk_live_xxx)
4. Update environment variables in Netlify with live keys
5. Create **Live webhooks** (separate from test webhooks)
6. Test with a real (small) payment
7. Launch! 🚀

---

## Step 7: Create Vouchers in Canva

### 7.1 Design Template

1. Go to [Canva](https://canva.com)
2. Create custom size: **A4 (210 × 297 mm)** or **Letter (8.5 × 11 in)**
3. Design your voucher template with:
   - Raiz de Luz branding/logo
   - Placeholder text for:
     - Recipient name: "Para: [NOME]"
     - Voucher value/service: "[SERVIÇO/VALOR]"
     - Personal message: "[MENSAGEM]"
     - Unique code: "Código: [CÓDIGO]"
     - Expiry date: "Válido até: [DATA]"
   - Decorative elements
   - Terms and conditions (small print)
4. Save as **Template** in Canva

### 7.2 Voucher Creation Workflow

When you receive a voucher order notification:

1. Open your Canva template
2. Fill in the details:
   - Recipient name
   - Service or value
   - Personal message from sender
   - Generate unique code (e.g., `RDL-2025-001`)
   - Calculate expiry (12 months from today)
3. Download as **PDF** (high quality)
4. Email to customer (and recipient if email provided)

### 7.3 Email Template

Subject: **O seu Vale Raiz de Luz está pronto! 🎁**

```
Olá [SENDER NAME],

Obrigado pela sua compra!

Em anexo encontra o seu vale personalizado para [RECIPIENT NAME].

Detalhes do Vale:
- Serviço/Valor: [SERVICE/AMOUNT]
- Código: [VOUCHER CODE]
- Válido até: [EXPIRY DATE]

O vale pode ser usado marcando uma sessão através de:
- Email: info@raizdeluz.eu
- Telefone: +351 XXX XXX XXX

Obrigado por escolher a Raiz de Luz!

Com gratidão,
[Your Name]
Raiz de Luz
```

---

## Summary of Options

| Option | Complexity | Features | Cost |
|--------|-----------|----------|------|
| **Payment Links** | ⭐ Simple | Basic, customers enter details twice | Free (Stripe fees only) |
| **Netlify + Checkout** | ⭐⭐ Medium | Best UX, pre-filled data, metadata | Free (Stripe fees only) |
| **Zapier Automation** | ⭐ Simple | No code, automated emails | €15-30/month + Stripe fees |

---

## Recommended Path

For your use case (manual Canva workflow), I recommend:

1. **Start with Payment Links** (quickest to set up)
2. **Later upgrade to Netlify + Checkout** (better customer experience)
3. **Use Stripe webhooks or Zapier** for automated notifications

---

## Support

If you need help:

- **Stripe Documentation:** https://stripe.com/docs
- **Netlify Functions:** https://docs.netlify.com/functions/overview/
- **Stripe Payment Links:** https://stripe.com/docs/payment-links

Questions? Reach out to info@raizdeluz.eu or check the Stripe support chat.

---

**Good luck with your voucher sales! 🎉**
