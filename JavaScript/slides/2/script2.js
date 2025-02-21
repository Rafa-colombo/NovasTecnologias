(function(){


    const imagens = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"];
    var current = 0;
    const prox = document.getElementById('next');
    const prev = document.getElementById('previous');
    const content = document.getElementById('content');

    prox.addEventListener('click', function(evt){

        evt.preventDefault();
        current++;
        if(current>(imagens.length - 1)){current = 0;}
        var newSlide = document.createElement('img');
        newSlide.src = 'slides/${imagens[current]}';
        newSlide.className = 'fadeinimg';
        content.appendChild(newSlide);

    })

})();