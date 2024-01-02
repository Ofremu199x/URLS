function myFunction() {
    var copyText = document.getElementById("myText").value;
    navigator.clipboard.writeText(copyText).then(() => {
        // Alert the user that the action took place.
        // Nobody likes hidden stuff being done under the hood!
        alert(`${copyText} has been copied to clipboard`);
    });


}