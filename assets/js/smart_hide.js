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

// 全局处理所有锚点链接，让目标居中显示（兼容 fixed menu + Hugo 自动锚点）
document.addEventListener('DOMContentLoaded', function () {
  // 选择所有内部锚点链接，包括：
  // 1. 普通 <a href="#xxx">
  // 2. PaperMod 主题的 .anchor 链接（标题旁的 #/¶ 图标）
  const anchors = document.querySelectorAll(
    'a[href^="#"]:not(a[href="#"]), ' +
    '.anchor[href^="#"], ' +
    '[class*="anchor"][href^="#"]'
  );
  anchors.forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();  // 阻止默认跳转

      const targetId = this.getAttribute('href').substring(1);
      if (!targetId) return;

      const target = document.getElementById(targetId);
      if (!target) return;
      // 执行居中滚动
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'center',     // 垂直居中
        inline: 'nearest'
      });

      // 可选：如果居中后仍被顶部导航栏轻微遮挡，可加偏移
      // const offset = -60;  // 根据你的 fixed header 高度调整（负数向上移）
      // window.scrollBy({ top: offset, behavior: 'smooth' });

      // 更新地址栏（保持 hash）
      history.replaceState(null, null, '#' + targetId);
    });
  });

  // 页面加载/刷新时处理现有 hash（兼容 Via 等浏览器刷新不跳）

  // 如果页面动态变化（如单页应用），监听 hashchange
});
function handleInitialHash() {
  if (!location.hash) return;
let rawHash = location.hash.substring(1);
  
  // 如果看起来是编码形式，强制 decode
  let id = rawHash;
  if (rawHash.includes('%')) {
    try {
      id = decodeURIComponent(rawHash);
    } catch (e) {
      console.error("decode 失败", e);
    }
  }
  if (!id) return;


  let elem = document.getElementById(id);

  // 兼容 Hugo 带前导 - 的 id
  if (!elem && !id.startsWith('-')) {
    elem = document.getElementById('-' + id);
  }

  if (elem) {
    setTimeout(() => {
      console.log('找到元素，执行滚动:', elem);
      elem.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
      });
    }, 800);  // Via 刷新时延迟加大到 800–1200ms 更稳
  } else {
alert("未找到");
    console.log('未找到 id:', id);
  }
}
window.addEventListener('pageshow', function (event) {
// persisted 表示是从 bfcache 恢复的（刷新/后退常见）
  // 无论 persisted true/false，都执行一次 hash 检查
	handleInitialHash();
});
