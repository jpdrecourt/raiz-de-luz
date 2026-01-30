// Main JavaScript for Raiz de Luz website
// This file contains general utilities and interactive features

document.addEventListener('DOMContentLoaded', () => {
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href !== '#' && href !== '') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
          });
        }
      }
    });
  });

  // Highlight active navigation link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach((link) => {
    const linkPage = link.getAttribute('href');
    if (linkPage === currentPage) {
      link.classList.add('active');
    }
  });

  // Add fade-in animation for sections on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px',
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  // Observe service cards and other sections for animation
  document.querySelectorAll('.service-card, .service-detail').forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });

  // Mobile menu toggle (if needed in the future)
  // This is a placeholder for potential mobile menu functionality
  const createMobileMenu = () => {
    // Mobile menu logic can be added here if needed
  };

  // Initialize mobile menu if screen is small
  if (window.innerWidth <= 768) {
    createMobileMenu();
  }
});

// Utility function to validate Portuguese phone numbers
export function validatePortuguesePhone(phone) {
  // Portuguese phone number format: +351 XXX XXX XXX or 9XX XXX XXX
  const phonePattern = /^(\+351|00351|351)?\s?[2-9]\d{8}$/;
  return phonePattern.test(phone.replace(/\s/g, ''));
}

// Utility function to format date in Portuguese
export function formatDate(date) {
  return new Intl.DateTimeFormat('pt-PT', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(date);
}
