// custom.js - term-modal 修复版
// 兼容你的 HTML：× 是实体 &times;，但 class 是 term-modal-close

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.term-modal-trigger').forEach(trigger => {
    // 修改点 1：从 dataset.modalId 改为 trigger.id
    const modalId = trigger.id;  
    const encodedContent = trigger.dataset.content;

    if (!modalId || !encodedContent) {
      console.warn('term-modal-trigger 缺少 id 或 data-content', trigger);
      return;
    }

    trigger.addEventListener('click', e => {
      e.preventDefault();
	history.pushState({ modal: modalId }, "", `#${modalId}`);
      let modal = document.getElementById("modal-"+modalId);

      if (modal) {
        modal.style.display = 'block';
        return;
      }

      modal = document.createElement('div');
      modal.id = "modal-"+modalId;  // modal 的 id 仍然是 term-modal-xxx，与 trigger.id 相同
      modal.className = 'term-modal';
modal.innerHTML = `
  <span class="term-modal-close">×</span>
  <div class="term-modal-content">
    <div class="term-modal-body"></div>
  </div>
`;
      document.body.appendChild(modal);

      const body = modal.querySelector('.term-modal-body');
      const closeBtn = modal.querySelector('.term-modal-close');

      closeBtn.addEventListener('click', ev => {
        ev.preventDefault();
        ev.stopPropagation();
        history.replaceState(null, null, ' ');
        modal.style.display = 'none';
      });
/*
      modal.addEventListener('click', ev => {
        const content = modal.querySelector('.term-modal-content');
        if (!content || !content.contains(ev.target)) {
          history.replaceState(null, null, ' ');
          modal.style.display = 'none';
        }
      });
*/
      // UTF-8 解码
      let content;
      try {
        const binary = atob(encodedContent);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) {
          bytes[i] = binary.charCodeAt(i);
        }
        content = new TextDecoder('utf-8').decode(bytes);
      } catch (err) {
        content = '<p style="color:red;">内容解码失败</p>';
        console.error('base64 解码错误:', err);
      }

      body.innerHTML = content;

      // MathJax 处理（新旧版本兼容）
      if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
        MathJax.typesetPromise([body]).catch(err => console.error('MathJax typesetPromise 失败:', err));
      } else if (typeof MathJax !== 'undefined' && MathJax.Hub && MathJax.Hub.Queue) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, body]);
      }
      modal.style.display = 'block';
    });
  });

  // Esc 关闭所有可见 modal
  document.addEventListener('keydown', ev => {
    if (ev.key === 'Escape') {
      document.querySelectorAll('.term-modal[style*="block"]').forEach(modal => {
        history.replaceState(null, null, ' ');
        modal.style.display = 'none';
      });
    }
  });

	window.addEventListener('popstate', (event) => {
  // 如果是我们的 modal state
  if (event.state && event.state.modal) {
    const modalIdFromState = event.state.modal;
    const modal = document.getElementById("modal-" + modalIdFromState);
    if (modal) {
      modal.style.display = 'none';
    }
  } else {
    // 兜底：关闭所有打开的 modal
    document.querySelectorAll('.term-modal[style*="block"]').forEach(m => {
      m.style.display = 'none';
    });
  }
});
});
