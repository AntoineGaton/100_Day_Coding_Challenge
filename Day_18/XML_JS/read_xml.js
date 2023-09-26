// Fetch XML data from a file or URL
fetch("../videogames.xml")
  .then(response => response.text())
  .then(data => {
    // Parse the XML data using DOMParser
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(data, 'application/xml');

    const tbody = document.querySelector('tbody');

   // Clear existing table content
   tbody.innerHTML = '';

   // Loop through each 'game' element and create a table row
   xmlDoc.querySelectorAll('game').forEach(game => {
      const row = document.createElement('tr');
      const title = game.querySelector('title').textContent;
      const platform = game.querySelector('platform').textContent;
      const releaseYear = game.querySelector('release_year').textContent;
      const developer = game.querySelector('developer').textContent;
      const rating = game.querySelector('rating').textContent;

      // Create table cells and populate with data
      row.innerHTML = `
         <td>${title}</td>
         <td>${platform}</td>
         <td>${releaseYear}</td>
         <td>${developer}</td>
         <td>${rating}</td>
      `;

      tbody.appendChild(row);
   })
})
  .catch(error => {
    console.error('Error fetching or parsing XML:', error);
  });
