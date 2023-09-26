import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("../videogames.xml")

# Get the root element
root = tree.getroot()

# Access elements and attributes
for game in root.findall("game"):
    title = game.find("title").text
    platform = game.find("platform").text
    release_year = game.find("release_year").text
    developer = game.find("developer").text
    rating = game.find("rating").text

    print(f"Title: {title}")
    print(f"Platform: {platform}")
    print(f"Release Year: {release_year}")
    print(f"Developer: {developer}")
    print(f"Rating: {rating}")
    print()
