// custom.js - term-modal 修复版
// 兼容你的 HTML：× 是实体 &times;，但 class 是 term-modal-close

document.addEventListener('DOMContentLoaded', () => {
  // 处理所有触发器
  document.querySelectorAll('.term-modal-trigger').forEach(trigger => {
    const modalId = trigger.dataset.modalId;
    const encodedContent = trigger.dataset.content;

    if (!modalId || !encodedContent) return;

    trigger.addEventListener('click', e => {
      e.preventDefault();

      let modal = document.getElementById(modalId);

      // 已存在 → 显示
      if (modal) {
        modal.style.display = 'block';
        return;
      }

      // 创建 modal
      modal = document.createElement('div');
      modal.id = modalId;
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

      // 关闭按钮（用 stopPropagation 防止冒泡）
      closeBtn.addEventListener('click', ev => {
        ev.preventDefault();
        ev.stopPropagation();
        history.replaceState(null, null, ' ');
        modal.style.display = 'none';
      });

      // 背景点击关闭（更宽松判断：只要不是内容区内部元素）
      modal.addEventListener('click', ev => {
        const content = modal.querySelector('.term-modal-content');
        if (content && !content.contains(ev.target)) {
          history.replaceState(null, null, ' ');
          modal.style.display = 'none';
        }
      });
      // ... 创建 modal 的代码不变 ...


      // UTF-8 安全解码 base64
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

      // MathJax 重新渲染
      if (typeof MathJax !== 'undefined') {
        MathJax.typesetPromise([body]).catch(err => console.error('MathJax 失败:', err));
      } else if (MathJax && MathJax.Hub) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, body]);
      }

      modal.style.display = 'block';
    });
  });

  // 全局 Esc 键关闭所有打开的 modal
  document.addEventListener('keydown', ev => {
    if (ev.key === 'Escape') {
      document.querySelectorAll('.term-modal[style*="block"]').forEach(modal => {
        history.replaceState(null, null, ' ');
        modal.style.display = 'none';
      });
    }
  });

  // hashchange 关闭（侧滑/后退）
  window.addEventListener('hashchange', () => {
    if (!window.location.hash) {
      document.querySelectorAll('.term-modal').forEach(modal => {
        modal.style.display = 'none';
      });
    }
  });
});
