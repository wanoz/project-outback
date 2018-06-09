// Set eventlistener to check for click
document.addEventListener("click", eventHandling);

// Event handling function
function eventHandling(event) {
    var elemObj = document.getElementById(event.target.id);

    if (elemObj !== null) {
        if (elemObj.type === "button"){
            var ind = elemObj.classList.contains("button_red_selected")
            
            if (ind === false){
                elemObj.classList.add("button_red_selected");
            } else {
                elemObj.classList.remove("button_red_selected");
            }           
        }
    }
}

// Slider bar functionality
var slider = document.getElementById("myRange");
var output = document.getElementById("budget");
output.textContent = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.textContent = (this.value*0.01*100).toFixed(2);
}

// Custom Bootstrap Javascript, nav-pills tab function
// $('#pills-meat-tab a[href="#pills-meat"]').tab('show')
// $('#pills-vegetable-tab a[href="#pills-vegetable"]').tab('show')
// $('#pills-carbs-tab a[href="#pills-carbs"]').tab('show')
// $('#pills-dairy-tab a[href="##pills-dairy"]').tab('show')

// $('#pills-method-tab a[href="#pills-method"]').tab('show')
// $('#pills-flavour-tab a[href="#pills-flavour"]').tab('show')
// $('#pills-cuisine-tab a[href="#pills-cuisine"]').tab('show')
