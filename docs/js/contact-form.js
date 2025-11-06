// Contact Form Handler for Raiz de Luz
// This is a basic client-side validation handler
// You'll need to integrate with a backend service or email service for actual form submission

document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Get form data
      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value || '',
        service: document.getElementById('service').value || '',
        message: document.getElementById('message').value,
      };

      // Basic client-side validation
      if (!formData.name || !formData.email || !formData.message) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
      }

      // Email validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(formData.email)) {
        alert('Por favor, insira um endereço de email válido.');
        return;
      }

      // TODO: Replace this with actual form submission logic
      // Options include:
      // 1. Using a service like Formspree, FormSubmit, or Netlify Forms
      // 2. Sending to your own backend API
      // 3. Using mailto: (not recommended for production)

      console.log('Form data:', formData);

      // For now, show a success message
      alert(
        'Obrigado pela sua mensagem! Entraremos em contacto consigo em breve.\n\nNota: Este é um formulário de demonstração. Por favor, integre com um serviço de email para funcionalidade completa.',
      );

      // Reset form
      contactForm.reset();

      // Example integration with Formspree (uncomment and add your endpoint):
      /*
      fetch('https://formspree.io/f/YOUR_FORM_ID', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
      .then(response => {
        if (response.ok) {
          alert('Obrigado pela sua mensagem! Entraremos em contacto consigo em breve.');
          contactForm.reset();
        } else {
          alert('Ocorreu um erro ao enviar a mensagem. Por favor, tente novamente.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Ocorreu um erro ao enviar a mensagem. Por favor, tente novamente.');
      });
      */
    });
  }
});
