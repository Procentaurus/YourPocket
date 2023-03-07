getData();

function getData(){
    const url = `http://127.0.0.1:8000/profile_data_visualisation/?period=all`;
    fetch(url,{
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      let totalIncomes = data.total_incomes;
      let totalExspenses = data.total_expenses;

      document.getElementById('expenses_sum').innerText = addDecimalPlaces(totalExspenses);
      document.getElementById('incomes_sum').innerText = addDecimalPlaces(totalIncomes);

      drawPieChart("piechart_expenses", "Structure of expences", data.expenses_by_categories);
      drawPieChart("piechart_incomes", "Structure of incomes", data.incomes_by_categories);
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
        r: 10,
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