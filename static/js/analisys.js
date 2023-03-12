getData();
addListenersForFilterRequest();
//setYearsInFilter();

function getData(period = "this"){

    const url = `http://127.0.0.1:8000/profile_data_visualisation/?period=${period}`;
    fetch(url,{
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);

      document.getElementById('expenses_sum').innerText = addDecimalPlaces(data.total_expenses)+" $";
      document.getElementById('incomes_sum').innerText = addDecimalPlaces(data.total_incomes)+" $";

      drawPieChart("piechart_expenses", "Structure of expences", data.expenses_by_categories);
      drawPieChart("piechart_incomes", "Structure of incomes", data.incomes_by_categories);

      drawBarChart(data.incomes_by_period, data.expenses_by_period);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function addDecimalPlaces(number){
    let text = `${number}`;
    var index = text.indexOf('.');
    if(index == -1) return text.concat(".00");
    else if(index == text.length - 2) return text.concat("0");
    else return text;
}

function drawPieChart(objectID, title, data){

    var keys = Object.keys(data);
    var values = Object.values(data);

    var xArray = keys;
    var yArray = values;
    
    var layout = {
      title:{
          text:title,
          font: {
              family: 'Impact',
              size: 38
          },
      },
      legend: {
        "orientation": "h",
        y: -0.1,
      },
      height: 600,
      width: 500,
      margin: {
        b: 0,
        r: 40,
        l: 40,
        t: 70
      }
    };
    
    var data = [{
      labels:xArray,
      values:yArray,
      hole:.2,
      type:"pie",
      rotation: 70,
    }];
    
    Plotly.newPlot(objectID, data, layout);
}
function drawBarChart(income_data, expense_data){
    var trace1 = {
      x: Object.keys(income_data),
      y: Object.values(income_data),
      name: 'Incomes',
      type: 'bar'
    };
    
    var trace2 = {
      x: Object.keys(expense_data),
      y: Object.values(expense_data),
      name: 'Expenses',
      type: 'bar'
    };
    
    var data = [trace1, trace2];
    
    var layout = {
      title:{
        text:"Summary",
        font: {
            family: 'Impact',
            size: 38
        },
    },
      barmode: 'group'
    };
    
    Plotly.newPlot('barChart', data, layout);
  
}

function setYearsInFilter(){
    document.getElementById('currentYear').innerText = new Date().getFullYear();
    document.getElementById('currentYear-1').innerText = new Date().getFullYear()-1;
    document.getElementById('currentYear-2').innerText = new Date().getFullYear()-2;
    document.getElementById('currentYear-3').innerText = new Date().getFullYear()-3;
    document.getElementById('currentYear-4').innerText = new Date().getFullYear()-4;
}
function uncheckRadios(){
    for(let i = 1; i <= 5; i++){
        document.getElementById(`btnradio${i}`).removeAttribute("checked");
    }
}

function addListenersForFilterRequest(){
    const array = ["this", "last", "last3", "lasty", "all"]

    for(let i = 1; i <= 5; i++){
        document.getElementById(`radio${i}`).addEventListener('click', function (e){
            e.preventDefault();
            uncheckRadios();
            document.getElementById(`btnradio${i}`).setAttribute('checked', true);
            getData(array[i-1]);
        })
    }
}