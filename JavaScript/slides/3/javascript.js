(function(){ 

    'use strict';

    document.getElementById('convert').addEventListener('submit', function(evt){
       
        evt.preventDefault(); //cancel the action of submit to page

        const distance = parseFloat( document.getElementById('distance').value);
        //distance = parseFloat(distance); //change the string (distance) to number
        const answer = document.getElementById('answer');
        
         if(distance){ 
            
            var name = "rafa";
            console.log(`hello ${name}`);
            const result = (distance * 1.60934).toFixed(3);
            answer.innerHTML = `<h2>The distance (${distance}) in miles are (${result}) in km </h2>`
            
        
        }
        else { answer.innerHTML = '<h2>Provide a number! </h2>';}
 
    });

})();