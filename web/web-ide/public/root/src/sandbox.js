(async () => {

  await new Promise((r) => { window.addEventListener(('load'), r); });

  const log = (data) => {
    const element = document.createElement('p');
    element.textContent = data.toString();
    document.querySelector('div').appendChild(element);
    window.scrollTo(0, document.body.scrollHeight);
  };

  const safeEval = (d) => (function (data) {
    with (new Proxy(window, {
      get: (t, p) => {
        if (p === 'console') return { log };
        if (p === 'eval') return window.eval;
        return undefined;
      }
    })) {
      eval(data);
    }
  }).call(Object.create(null), d);

  window.addEventListener('message', (event) => {
    const div = document.querySelector('div');
    if (div) document.body.removeChild(div);
    document.body.appendChild(document.createElement('div'));
    try {
      safeEval(event.data);
    } catch (e) {
      log(e);
    }
  });

})();
