const chk = document.getElementById('chk')

chk.addEventListener('change', () => {
    document.body.classList.toggle('dark')
})

document.getElementById('botao').addEventListener('click', function() {
    document.getElementById('container_l').style.display = 'block';
    setTimeout(function() {
      document.getElementById('container_l').style.display = 'none';
    }, 10000); 
  });


