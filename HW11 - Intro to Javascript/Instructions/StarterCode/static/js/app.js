// from data.js
var tableData = data;

// YOUR CODE HERE!
//Grab tbody information
tbody = d3.select("tbody")

function displayData(data){
    tbody.text("")
    data.forEach(function(sighting){
    new_tr = tbody.append("tr")
    Object.entries(sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)
    })
})}

displayData(tableData)

//Selecting web user's input; filter button
var date_input = d3.select("#datetime")
var button = d3.select("filter-btn")

//Filter the data by date of user's input
function clickSelect(){
    //Don't refresh the page!
    d3.event.preventDefault();
    //Print input value
    console.log(date_input.property("value"));
    //Create new table based on filtered data
    var new_table = tableData.filter(incident => incident.datetime===date_input.property("value")))
    //Display the new table
    showtable(new_table);
}

date_input.on("change", clickSelect)