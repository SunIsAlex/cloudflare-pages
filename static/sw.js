const CACHE_NAME = 'desmos-cache-v1';

self.addEventListener('install', event => {
  self.skipWaiting(); // 立即生效
});

self.addEventListener('activate', event => {
  clients.claim(); // 接管页面
});

self.addEventListener('fetch', event => {
  const url = event.request.url;

  // 👉 只拦截 Desmos
  if (url.includes('desmos.com/api')) {
    console.log('Service Worker: Caching', url);
    event.respondWith(
      caches.open(CACHE_NAME).then(cache =>
        cache.match(event.request).then(cached => {
          if (cached) {
            return cached; // 直接用缓存
          }

          return fetch(event.request).then(response => {
            cache.put(event.request, response.clone());
            return response;
          });
        })
      )
    );
  }
});