document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.term-modal-trigger').forEach(trigger => {
    const modalId = trigger.dataset.modalId;
    const encoded = trigger.dataset.content;

    trigger.addEventListener('click', (e) => {
      e.preventDefault();

      let modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = 'block';
        return;
      }

      modal = document.createElement('div');
      modal.id = modalId;
      modal.className = 'term-modal';
      modal.innerHTML = `
        <div class="term-modal-content">
          <span class="term-modal-close">&times;</span>
          <div class="term-modal-body"></div>
        </div>
      `;
      document.body.appendChild(modal);

      const body = modal.querySelector('.term-modal-body');
      const closeBtn = modal.querySelector('.term-modal-close');

      closeBtn.addEventListener('click', () => modal.style.display = 'none');
      modal.addEventListener('click', ev => {
        if (ev.target === modal) modal.style.display = 'none';
      });
	// base64 → binary string → Uint8Array → UTF-8 解码
let binary = atob(encoded);
let len = binary.length;
let bytes = new Uint8Array(len);
for (let i = 0; i < len; i++) {
  bytes[i] = binary.charCodeAt(i);
}
const decoder = new TextDecoder('utf-8');
const content = decoder.decode(bytes);

      body.innerHTML = content;

      // MathJax 重新渲染
      if (typeof MathJax !== 'undefined') {
        MathJax.typesetPromise([body]).catch(err => {
          console.error('MathJax typeset failed:', err);
        });
      } else if (MathJax && MathJax.Hub) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, body]);
      }

      modal.style.display = 'block';
    });
  });
});
