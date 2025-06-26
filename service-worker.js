const cacheName = "instrumentos-cache-v1";
const filesToCache = [
  "index.html",
  "instrumento.html",
  "style.css",
  "js/app.js",
  "instrumentos.json"
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(cacheName).then(cache => cache.addAll(filesToCache))
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(response => response || fetch(e.request))
  );
});
