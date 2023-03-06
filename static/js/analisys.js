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
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}