// Fetch XML data from a file or URL
fetch("../videogames.xml")
  .then(response => response.text())
  .then(data => {
    // Parse the XML data using DOMParser
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(data, 'application/xml');

    // Access elements and attributes
    const games = xmlDoc.getElementsByTagName('game');
    for (let i = 0; i < games.length; i++) {
      const title = games[i].getElementsByTagName('title')[0].textContent;
      const platform = games[i].getElementsByTagName('platform')[0].textContent;
      const releaseYear = games[i].getElementsByTagName('release_year')[0].textContent;
      const developer = games[i].getElementsByTagName('developer')[0].textContent;
      const rating = games[i].getElementsByTagName('rating')[0].textContent;

      console.log(`Title: ${title}`);
      console.log(`Platform: ${platform}`);
      console.log(`Release Year: ${releaseYear}`);
      console.log(`Developer: ${developer}`);
      console.log(`Rating: ${rating}`);
      console.log('');
    }
  })
  .catch(error => {
    console.error('Error fetching or parsing XML:', error);
  });
