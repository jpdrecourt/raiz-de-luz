// Carousel for the Cocares page.
// Markup: <div class="carousel" data-carousel-source="cocaresSlides" aria-label="..."></div>
// The source names a global array (see cocares-data.js) of
//   { src: 'media/images/cocares/<name>', alt: '...', caption: '...' }
// where src has no extension: <name>.webp and <name>.jpg must both exist.
// Scrolling is native CSS scroll-snap; this script renders the slides and
// adds prev/next buttons, arrow keys and a live counter.

(function () {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const EAGER_COUNT = 0; // slides that load eagerly; the gallery sits far below the fold
  const EN_DASH = String.fromCharCode(0x2013);

  const chevron = (dir) =>
    '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">' +
    (dir === 'prev'
      ? '<path d="M15 5l-7 7 7 7" />'
      : '<path d="M9 5l7 7-7 7" />') +
    '</svg>';

  function el(tag, className, attrs) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (attrs) {
      Object.keys(attrs).forEach((k) => node.setAttribute(k, attrs[k]));
    }
    return node;
  }

  function buildSlide(slide, i, total) {
    const slideEl = el('div', 'carousel__slide', {
      role: 'group',
      'aria-roledescription': 'diapositivo',
      'aria-label': `${i + 1} de ${total}`,
    });
    const figure = el('figure', 'carousel__figure');
    const frame = el('div', 'carousel__frame');
    const picture = el('picture');
    picture.appendChild(
      el('source', null, { srcset: `${slide.src}.webp`, type: 'image/webp' })
    );
    const img = el('img', null, {
      src: `${slide.src}.jpg`,
      alt: slide.alt || '',
      loading: i < EAGER_COUNT ? 'eager' : 'lazy',
      decoding: 'async',
      width: String(slide.width || 600),
      height: String(slide.height || 800),
    });
    picture.appendChild(img);
    frame.appendChild(picture);
    figure.appendChild(frame);
    if (slide.caption) {
      const cap = el('figcaption', 'carousel__caption');
      cap.textContent = slide.caption;
      figure.appendChild(cap);
    }
    slideEl.appendChild(figure);
    return slideEl;
  }

  function initCarousel(root, slides) {
    if (!slides || !slides.length) {
      root.hidden = true;
      return;
    }
    root.setAttribute('role', 'region');
    root.setAttribute('aria-roledescription', 'carrossel');

    // role="group" so the focusable scroller can carry a label
    const track = el('div', 'carousel__track', {
      tabindex: '0',
      role: 'group',
      'aria-label': 'Diapositivos (use as setas para navegar)',
    });
    const items = slides.map((s, i) => {
      const slideEl = buildSlide(s, i, slides.length);
      track.appendChild(slideEl);
      return slideEl;
    });

    const controls = el('div', 'carousel__controls');
    const prev = el('button', 'carousel__btn carousel__btn--prev', {
      type: 'button',
      'aria-label': 'Anterior',
    });
    prev.innerHTML = chevron('prev');
    const next = el('button', 'carousel__btn carousel__btn--next', {
      type: 'button',
      'aria-label': 'Seguinte',
    });
    next.innerHTML = chevron('next');
    const counter = el('span', 'carousel__counter', {
      'aria-live': 'polite',
      'aria-atomic': 'true',
    });
    controls.append(prev, counter, next);

    root.replaceChildren(track, controls);

    // Geometry --------------------------------------------------------------
    const padStart = () => parseFloat(getComputedStyle(track).paddingLeft) || 0;
    const step = () =>
      items.length > 1
        ? items[1].offsetLeft - items[0].offsetLeft
        : items[0].offsetWidth;
    const visibleCount = () =>
      Math.max(1, Math.round((track.clientWidth - 2 * padStart()) / step()));
    const maxIndex = () => Math.max(0, items.length - visibleCount());

    function currentIndex() {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 2) return maxIndex();
      return Math.min(maxIndex(), Math.round(track.scrollLeft / step()));
    }

    function goTo(index) {
      const i = Math.max(0, Math.min(maxIndex(), index));
      track.scrollTo({
        left: items[i].offsetLeft - items[0].offsetLeft,
        behavior: reducedMotion.matches ? 'auto' : 'smooth',
      });
    }

    // State -----------------------------------------------------------------
    let shown = -1;
    let shownVisible = -1;
    function update() {
      const i = currentIndex();
      const v = visibleCount();
      // aria-disabled, not disabled: a disabled button drops keyboard focus
      // to <body> when it reaches the end of the gallery.
      prev.setAttribute('aria-disabled', String(i <= 0));
      next.setAttribute('aria-disabled', String(i >= maxIndex()));
      if (i === shown && v === shownVisible) return;
      shown = i;
      shownVisible = v;
      const last = Math.min(items.length, i + v);
      counter.textContent =
        v > 1 && last > i + 1
          ? `${i + 1}${EN_DASH}${last} de ${items.length}`
          : `${i + 1} de ${items.length}`;
    }

    let ticking = false;
    track.addEventListener(
      'scroll',
      () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
          ticking = false;
          update();
        });
      },
      { passive: true }
    );
    track.addEventListener('scrollend', update);
    window.addEventListener('resize', update);

    const isOff = (btn) => btn.getAttribute('aria-disabled') === 'true';
    prev.addEventListener('click', () => {
      if (!isOff(prev)) goTo(currentIndex() - visibleCount());
    });
    next.addEventListener('click', () => {
      if (!isOff(next)) goTo(currentIndex() + visibleCount());
    });

    root.addEventListener('keydown', (e) => {
      switch (e.key) {
        case 'ArrowLeft':
          goTo(currentIndex() - 1);
          break;
        case 'ArrowRight':
          goTo(currentIndex() + 1);
          break;
        case 'Home':
          goTo(0);
          break;
        case 'End':
          goTo(maxIndex());
          break;
        default:
          return;
      }
      e.preventDefault();
    });

    root.classList.add('carousel--ready');
    update();
  }

  function initAll() {
    document.querySelectorAll('[data-carousel-source]').forEach((root) => {
      initCarousel(root, window[root.dataset.carouselSource]);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
