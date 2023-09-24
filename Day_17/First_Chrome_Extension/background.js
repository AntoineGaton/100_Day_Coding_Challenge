// background.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
   if (message.action === 'downloadFile') {
     downloadFile(message.data);
   }
 });
 
 function downloadFile(data) {
   const jsonData = JSON.stringify(data);
   const blob = new Blob([jsonData], { type: 'application/json' });
   const filename = 'api_data.json';
 
   chrome.downloads.download({
     url: URL.createObjectURL(blob),
     filename: filename,
     saveAs: false, // Set to true if you want to prompt the user to choose a download location
   });
 }
 