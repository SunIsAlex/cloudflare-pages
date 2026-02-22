document.addEventListener('DOMContentLoaded', () => {

  let header = document.querySelector('header.header') || document.querySelector('header') || document.querySelector('.header');

  if (!header) {
    console.warn("Header not found after fallback selectors");
    return;
  }

  console.log("Header found:", header);

  let lastScrollTop = 0;
  const delta = 5;
  const headerHeight = header.offsetHeight || 60;

  window.addEventListener('scroll', () => {
    let st = window.pageYOffset || document.documentElement.scrollTop;

    if (Math.abs(lastScrollTop - st) <= delta) return;

    if (st > lastScrollTop && st > headerHeight) {
      header.style.transform = 'translateY(-100%)';
    } else {
      header.style.transform = 'translateY(0)';
    }

    lastScrollTop = st <= 0 ? 0 : st;
  }, { passive: true });
});
