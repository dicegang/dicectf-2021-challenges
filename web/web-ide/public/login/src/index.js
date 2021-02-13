(async () => {

  await new Promise((r) => { window.addEventListener(('load'), r); });

  const passwordInput = document.querySelector('input[type=password]');
  document.querySelector('form')
    .addEventListener('click', (e) => {
      switch (e.toElement.value) {
      case 'guest': 
        passwordInput.style.display = 'none';
        break;
      case 'admin':
        passwordInput.style.display = 'block';
      }
    });

})();
