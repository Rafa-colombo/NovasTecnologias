(function(){

    "strict";


    const imagens = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"];
    let current = 0;
    document.getElementById('next').onclick = proxFoto;
    document.getElementById('previous').onclick = prevFoto;

    function proxFoto(){
        current++;
        if(current>4){ current = 0; }
        document.getElementById('myimage').src = imagens[current];
    }
    function prevFoto(){
        if(current == 0){current = 4;}
        current--;
        document.getElementById('myimage').src = imagens[current];
    }


})();

