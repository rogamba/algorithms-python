orders = {}
/**
 * Repeat fetching data every second
 */
function renderShelves(data){
    // Sort shelves
    container = document.querySelector("#shelves");
    container.innerHTML="";
    shelves = Object.keys(data).sort();
    for(c in shelves){
        console.log(shelves[c]);
        // Create shelf on the go
        shelf = document.createElement('div');
        shelf.classList.add('shelf');
        subtitle = document.createElement('h1');
        subtitle.classList.add('subtitle');
        subtitle.innerHTML = shelves[c].toUpperCase()
        shelf.appendChild(subtitle)
        for(i in data[shelves[c]]){
            ord=data[shelves[c]][i]
            order = document.createElement('div');
            order.classList.add('order');
            order.innerHTML = `${ord.name} <b>(${(Math.round(ord.normalized_value*100)/100)})</b>`
            shelf.appendChild(order);
        }
        container.appendChild(shelf);
    }
}

/*
* Send signal to the webapp to start the incomming orders simulation
*/
function startSimulation(){
    fetch('/start_simulation', {
        method: 'post',
        body: JSON.stringify({"start":true})
    })
        .then(response =>  response.json())
        .then(data => {
            setInterval(fetchData, 300);   
        });
}

/**
 * Fetch state of the kitchen shelves and orders 
 */
function fetchData(){
    console.log("Fetching");
    fetch('/update')
        .then(response => response.json())
        .then(data => {
            renderShelves(data);
        });
}

/*
* Click btn to start simulation
*/
document.getElementById('btn-start').addEventListener('click', function (event) {
    startSimulation();
});