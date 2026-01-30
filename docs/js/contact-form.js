// Contact Form Handler for Raiz de Luz
// Integrated with Formspree for form submission

document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      // Get form data
      const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        phone: document.getElementById('phone').value.trim() || '',
        message: document.getElementById('message').value.trim(),
      };

      // Basic client-side validation
      if (!formData.name || !formData.email || !formData.message) {
        showMessage('Por favor, preencha todos os campos obrigatórios.', 'error');
        return;
      }

      // Email validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(formData.email)) {
        showMessage('Por favor, insira um endereço de email válido.', 'error');
        return;
      }

      // Get submit button and disable it during submission
      const submitButton = contactForm.querySelector('button[type="submit"]');
      const originalButtonText = submitButton.textContent;
      submitButton.disabled = true;
      submitButton.textContent = 'A enviar...';

      try {
        // Formspree endpoint for contact form submissions
        const formspreeEndpoint = 'https://formspree.io/f/xdkjyvvw';

        const response = await fetch(formspreeEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
        });

        if (response.ok) {
          showMessage(
            'Obrigado pela sua mensagem! Entraremos em contacto consigo em breve.',
            'success',
          );
          contactForm.reset();
        } else {
          throw new Error('Form submission failed');
        }
      } catch (error) {
        console.error('Error:', error);
        showMessage(
          'Ocorreu um erro ao enviar a mensagem. Por favor, tente novamente ou contacte-nos directamente por email.',
          'error',
        );
      } finally {
        // Re-enable submit button
        submitButton.disabled = false;
        submitButton.textContent = originalButtonText;
      }
    });
  }

  // Helper function to show messages to the user
  function showMessage(message, type) {
    // Remove any existing message
    const existingMessage = document.querySelector('.form-message');
    if (existingMessage) {
      existingMessage.remove();
    }

    // Create new message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `form-message form-message-${type}`;
    messageDiv.textContent = message;

    // Insert message before the form
    const formSection = document.querySelector('.contact-form-section');
    formSection.insertBefore(messageDiv, contactForm);

    // Auto-remove message after 5 seconds
    setTimeout(() => {
      messageDiv.style.transition = 'opacity 0.5s';
      messageDiv.style.opacity = '0';
      setTimeout(() => messageDiv.remove(), 500);
    }, 5000);

    // Scroll to message
    messageDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
});
