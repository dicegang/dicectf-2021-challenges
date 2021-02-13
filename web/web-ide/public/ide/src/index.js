(async () => {

  await new Promise((r) => { window.addEventListener(('load'), r); });

  document.getElementById('run').addEventListener('click', () => {
    document.querySelector('iframe')
      .contentWindow
      .postMessage(document.querySelector('textarea').value, '*');
  });

  document.getElementById('save').addEventListener('click', async () => {
    const response = await fetch('/ide/save', {
      method: 'POST',
      body: document.querySelector('textarea').value,
      headers: {
        'Content-Type': 'application/javascript'
      }
    });
    if (response.status === 200) {
      window.location = `/ide/saves/${await response.text()}`;
      return;
    }
    alert('You are not an admin.');
  });

})();

