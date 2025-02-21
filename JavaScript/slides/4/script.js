var detailsform = document.querySelector('#destination_details_form');

detailsform.addEventListener('submit', handleformsubmit);

function handleformsubmit(evt){
    evt.preventDefault();

    //get the values of the cards
    var destName = evt.target.elements['name'].value;
    var destLoc = evt.target.elements['location'].value;
    var destPhoto = evt.target.elements["photo"].value;
    var destDesc = evt.target.elements["description"].value;

    //clear out the cards
    for (var i = 0; i<detailsform.length; i++) { detailsform.elements[i].value = ""; }
  
    //run a function that creates new card
    var destCard = createDestinationCard(destName, destLoc, destPhoto, destDesc);

    var wishListContainer = document.querySelector('#destinations_container');

    if(wishListContainer.children.length === 0){ document.querySelector('#title').innerHTML = "My wish List";}

    //if needed chage the header 
    var wishListContaine2 = document.getElementById('destination_container');
    if (wishListContainer2.children.length === 0){ document.querySelector("#tittle").innerHTML = "My wish list";}

    //add card
    document.querySelector('#destinations_container').appendChild(destCard);



}

function createDestinationCard(name, location, photoURL, description){

    var card = document.createElement('div');
    card.className = 'card';

    var img = document.createElement('img');
    img.setAttribute('alt', name);

    var varPhotoUrl = "images/signpost.jpg";

    if(photoURL.length === 0){ img.setAttribute('src', varPhotoUrl);}
    else { img.setAttribute('src', photoURL); }

    card.appendChild(img);

    var cardBody = document.createElement("div");
    cardBody.className = "cardBody";

    var cardTitle = document.createElement("h3");
    cardTitle.innerText = name;
    cardBody.appendChild(cardTitle);

    var cardSubtitle = document.createElement("h4");
    cardSubtitle.innerText = location;
    cardSubtitle.appendChild(cardSubtitle);

    if(description.length !== 0){
        var cardText = document.createElement("p");
        cardText.className = "card_text";
        cardText.innerText = description;
        cardBody.appendChild(cardText);
    }

    var cardDeleteBtn = document.createElement("button");
    cardDeleteBtn.innerText = "Remove";

    cardDeleteBtn.addEventListener("click", removeDestination);
    cardBody.appendChild(cardDeleteBtn);

    card.appendChild(cardBody);

    return cardBody;

}

function removeDestination(evt){
    var card = evt.target.parentElement.parentElement;
    card.remove();

}