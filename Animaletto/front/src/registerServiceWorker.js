import { register } from 'register-service-worker';

register(`${process.env.BASE_URL}service-worker.js`, {
  ready () {
    console.log("OK -> Service worker ready");
  },
  registered () {
    console.log('OK -> Service worker registrato');
  },
  cached () {
    console.log("OK -> Pronta per l'uso offline (Cached)")
    return caches.open('app-cache').then(cache => {
      return cache.addAll([
        '/',
        '/index.html',
        '/manifest.json',
        '/service-worker.js',
        '/robots.txt',
      ]);
    });
  },
  offline () {
    console.log('OK -> Applicazione in modalità offline.');
  },
  error (error) {
    console.error("KO -> Error during service worker registration: ",error)
  }
});
