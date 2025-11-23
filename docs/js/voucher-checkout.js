// Stripe Voucher Checkout Handler
// This script handles the voucher purchase form and Stripe integration

// CONFIGURATION - Replace with your actual Stripe Publishable Key
const STRIPE_PUBLISHABLE_KEY = 'pk_test_YOUR_PUBLISHABLE_KEY_HERE'; // TODO: Replace with your key

// Initialize Stripe
const stripe = Stripe(STRIPE_PUBLISHABLE_KEY);

// Pricing configuration (in cents)
const PRICING = {
  '50': 5000,
  '75': 7500,
  '100': 10000,
  '150': 15000,
  'service-therapeutic': 6000,      // €60 for 60min
  'service-sports': 6000,
  'service-pregnancy': 6500,
  'service-craniosacral': 7000,
  'service-lymphatic': 6500,
  'service-relaxation': 6000,
  'service-hotstones': 9000,        // €90 for 90min
  'service-shamanic': 9500,
};

// Service names for display
const SERVICE_NAMES = {
  '50': 'Vale de €50',
  '75': 'Vale de €75',
  '100': 'Vale de €100',
  '150': 'Vale de €150',
  'service-therapeutic': 'Massagem Terapêutica (60min)',
  'service-sports': 'Massagem Desportiva (60min)',
  'service-pregnancy': 'Massagem para Grávidas (60min)',
  'service-craniosacral': 'Terapia Sacro Craniana (60min)',
  'service-lymphatic': 'Drenagem Linfática (60min)',
  'service-relaxation': 'Relaxamento (60min)',
  'service-hotstones': 'Pedras Quentes (90min)',
  'service-shamanic': 'Massagem Xamânica (90min)',
};

// Character counter for personal message
const messageTextarea = document.getElementById('personal-message');
const charCount = document.getElementById('char-count');

if (messageTextarea && charCount) {
  messageTextarea.addEventListener('input', function() {
    const count = this.value.length;
    charCount.textContent = `${count}/300 caracteres`;
  });
}

// Form submission handler
const form = document.getElementById('voucher-form');
const submitBtn = document.getElementById('submit-btn');
const formMessage = document.getElementById('form-message');

form.addEventListener('submit', async function(e) {
  e.preventDefault();

  // Disable submit button to prevent double submissions
  submitBtn.disabled = true;
  submitBtn.textContent = 'A processar...';
  formMessage.textContent = '';
  formMessage.className = '';

  try {
    // Collect form data
    const formData = {
      voucherType: document.getElementById('voucher-type').value,
      recipientName: document.getElementById('recipient-name').value,
      recipientEmail: document.getElementById('recipient-email').value,
      senderName: document.getElementById('sender-name').value,
      senderEmail: document.getElementById('sender-email').value,
      personalMessage: document.getElementById('personal-message').value,
      deliveryDate: document.getElementById('delivery-date').value,
    };

    // Validate voucher type
    if (!formData.voucherType) {
      throw new Error('Por favor selecione um tipo de vale');
    }

    // Get price
    const amount = PRICING[formData.voucherType];
    if (!amount) {
      throw new Error('Tipo de vale inválido');
    }

    // Create Stripe Checkout Session
    // Note: This requires a server endpoint to create the session
    // For now, we'll redirect to Stripe Payment Links (see instructions below)

    // OPTION 1: Using Stripe Payment Links (Recommended for manual workflow)
    // Create payment links in Stripe Dashboard and use them here
    // See STRIPE-SETUP-INSTRUCTIONS.md for details

    // For demonstration, show what data would be sent:
    console.log('Voucher Data:', formData);
    console.log('Amount:', amount / 100, 'EUR');

    // TEMPORARY: Show instructions since backend is not set up yet
    formMessage.className = 'message-info';
    formMessage.innerHTML = `
      <strong>⚠️ Configuração Necessária</strong><br>
      Por favor complete a configuração do Stripe seguindo as instruções em STRIPE-SETUP-INSTRUCTIONS.md<br>
      <br>
      <strong>Dados do Vale:</strong><br>
      Tipo: ${SERVICE_NAMES[formData.voucherType]}<br>
      Valor: €${(amount / 100).toFixed(2)}<br>
      Para: ${formData.recipientName}<br>
      De: ${formData.senderName}<br>
      ${formData.personalMessage ? 'Mensagem: ' + formData.personalMessage : ''}
    `;

    submitBtn.disabled = false;
    submitBtn.textContent = 'Proceder ao Pagamento';

    // TODO: Replace the above with actual Stripe integration
    // See implementation options in STRIPE-SETUP-INSTRUCTIONS.md

  } catch (error) {
    console.error('Error:', error);
    formMessage.className = 'message-error';
    formMessage.textContent = error.message || 'Erro ao processar o pedido. Por favor tente novamente.';
    submitBtn.disabled = false;
    submitBtn.textContent = 'Proceder ao Pagamento';
  }
});

// CSS for messages
const style = document.createElement('style');
style.textContent = `
  .message-error {
    background-color: #fee;
    border-left: 4px solid #f44336;
    color: #c62828;
    padding: 1rem;
    border-radius: 4px;
  }

  .message-success {
    background-color: #efe;
    border-left: 4px solid #4caf50;
    color: #2e7d32;
    padding: 1rem;
    border-radius: 4px;
  }

  .message-info {
    background-color: #e3f2fd;
    border-left: 4px solid #2196f3;
    color: #1565c0;
    padding: 1rem;
    border-radius: 4px;
  }
`;
document.head.appendChild(style);
