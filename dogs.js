document.getElementById("showDogButton").addEventListener("click", async function(){
  const response = await fetch ("https://dog.ceo/api/breeds/image/random");
  const data = await response.json();

  const imageUrl = data.message;


  const dogImage = document.getElementById("dogImage");
  dogImage.src = imageUrl;
  dogImage.style.display = "block";

});