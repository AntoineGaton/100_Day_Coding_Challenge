async function fetchData(){
   const url = 'https://weatherapi-com.p.rapidapi.com/forecast.json?q=Fort%20Lauderdale&days=3';
   const options = {
      method: 'GET',
      headers: {
         'X-RapidAPI-Key': '4e4d855cb7mshcab1de45d69f62ep1735a6jsnd09627127078',
         'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
      }
   };

   try {
      const response = await fetch(url, options);
      const result = await response.json();
      console.log("API Data -------------------------> ", result);
      // Send a message to the background script to trigger the download
    chrome.runtime.sendMessage({ action: 'downloadFile', data: result });
      document.getElementById('weather').innerHTML = result.current.feelslike_f;
   }catch (error){
      console.error(error);
   }
   
}

fetchData();