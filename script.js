function trocarImagem(elemento, novaImagem) {
    elemento.style.opacity = '0';  
    setTimeout(function() {
      elemento.src = novaImagem;   
      elemento.style.opacity = '1'; 
    }, 100);  
  }

  function restaurarImagem(elemento, imagemOriginal) {
    elemento.style.opacity = '0';  
    setTimeout(function() {
      elemento.src = imagemOriginal;  
      elemento.style.opacity = '1';  
    }, 100);  
  }