/* This example includes creating a database, 
a table with a FULLTEXT index, inserting the content, and running a full-text search query.*/

create database vgt
-- drop database vgt

-- create table. 
-- FULLTEXT(title, content, tags) creates a full-text index for efficient searching across these columns.

CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    continent VARCHAR(255),
    tags TEXT,
    image_path VARCHAR(255),
    FULLTEXT(title, content, tags)
) ;

-- Step 3: Insert the Content
-- continents: North-America, South-America, Europe, Asia-Middle-East, Africa, Oceania
-- topid: nature, sea, theme park, sport, city
INSERT INTO images (title, content, continent, tags, image_path) 
VALUES 
(
    'Disneyland Paris - The Ultimate Magical Destination',
    'Disneyland Paris, located in Marne-la-Vallée, France, is Europe\'s most iconic and magical theme park destination. Opened in 1992, this resort offers an enchanting experience for visitors of all ages. It consists of two main parks: Disneyland Park and Walt Disney Studios Park, along with entertainment, shopping, and dining options at Disney Village.\n\n'
    'Disneyland Park is a realm of fairy tales and imagination. Its centerpiece, the Sleeping Beauty Castle, is surrounded by themed lands, including: '
    'Fantasyland, Adventureland, Frontierland, and Discoveryland, featuring rides like Peter Pan\'s Flight, Space Mountain, and Big Thunder Mountain.\n\n'
    'Walt Disney Studios Park immerses guests in the magic of filmmaking with attractions like Ratatouille: The Adventure, Tower of Terror, and Avengers Campus.\n\n'
    'Disney Village offers world-class dining, shopping, and entertainment.\n\n'
    'Throughout the year, Disneyland Paris hosts events such as Halloween Festival, Christmas Magic, and Marvel Summer of Superheroes.\n\n'
    'Accessible within 35 minutes from Paris, Disneyland Paris is a must-visit for families and Disney fans alike.',
    'Europe',
    'Magic, Theme Park, Family Fun, Disney, France, Travel, Attractions, Adventure, Fairy Tales, Entertainment, Europe', 
    'C:/Users/Images/DisneylandParis/'
),

(
    'Universal Studios Japan (Osaka, Japan)',
    'Universal Studios Japan is packed with exciting rides based on popular movies,\n
    including Jurassic Park, Harry Potter, and Minions. \n
    The Wizarding World of Harry Potter is especially amazing, \n
    with immersive shops and the thrilling ride Harry Potter and the Forbidden Journey. \n
    It’s perfect for an 11-year-old who loves movies and big, action-packed attractions!'
    , 'Asia-Middle-East',
    'Magic, Theme Park, Family Fun, Harry Potter, Jurassic Park, Travel, Attractions, Adventure, Wizard, Entertainment, Forbidden Journey, japan, movies', 
    'C:/Users/Images/Osaka/'
),

(
    'Six Flags Magic Mountain (Valencia, California, USA)',
    'Six Flags Magic Mountain is home to some of the most thrilling roller coasters in the world, including the intense Twisted Colossus and the heart-racing X2. \n
    It’s an adrenaline-packed adventure, with a variety of rides for all ages. \n
    This theme park is perfect for an 11-year-old who loves extreme rides, fun challenges, and exciting adventures!',
    'North-America',
    'Theme Park, Roller Coasters, Family Fun, Adventure, Thrills, X2, Twisted Colossus, Travel, Entertainment, Amusement, California, Rides',
    'C:/Users/Images/SixFlags/'
),

('Legoland Windsor (England)', 
 'Legoland Windsor is a must-visit for young LEGO fans, with themed rides, interactive shows, and amazing LEGO structures. ...', 
 'Europe', 
 'Theme Park, Family Fun, LEGO, England, Attractions', 
 'C:/Users/Images/LegolandWindsor/'
 ),

('Colosseum (Rome, Italy)', 
 'The Colosseum in Rome is an incredible historical site that kids will love exploring. ...', 
 'Europe', 
 'History, Ancient Rome, Family Fun, Travel, Landmarks', 
 'C:/Users/Images/Colosseum/'
 ),
 
 ('Efteling (Kaatsheuvel, Netherlands)', 
 'Efteling is a fairytale-themed amusement park featuring rides, shows, and magical experiences. ...', 
 'Europe', 
 'Theme Park, Fairytale, Family Fun, Netherlands', 
 'C:/Users/Images/Efteling/'
 ),

('Schönbrunn Palace (Vienna, Austria)', 
 'Explore Schönbrunn Palace and its gardens, a UNESCO World Heritage Site, with activities for kids. ...', 
 'Europe', 
 'History, Culture, Family Fun, Travel, Austria', 
 'C:/Users/Images/SchonbrunnPalace/'
 ),
 
 ('Burj Khalifa (Dubai, UAE)', 
 'The Burj Khalifa offers stunning views from the observation deck on the 148th floor. ...', 
 'Asia-Middle-East', 
 'Architecture, City View, Travel, Dubai, Adventure', 
 'C:/Users/Images/BurjKhalifa/'
 ),

('Gardens by the Bay (Singapore)', 
 'Explore the futuristic Supertree Grove and Cloud Forest, perfect for young explorers. ...', 
 'Asia-Middle-East', 
 'Nature, Family Fun, Singapore, Travel', 
 'C:/Users/Images/GardensByTheBay/'
 ),

('Hong Kong Disneyland (Hong Kong)', 
 'Hong Kong Disneyland is perfect for kids with thrilling rides and magical parades. ...', 
 'Asia-Middle-East', 
 'Magic, Theme Park, Family Fun, Hong Kong', 
 'C:/Users/Images/HongKongDisneyland/'
 ),

('Great Wall of China (China)', 
 'The Great Wall of China is a historical wonder that kids can explore. ...', 
 'Asia-Middle-East', 
 'History, Adventure, Travel, China, Exploration', 
 'C:/Users/Images/GreatWallOfChina/'
 ),
 
('Statue of Liberty (New York, USA)', 
 'The Statue of Liberty is an iconic symbol of freedom with guided tours. ...', 
 'North-America', 
 'Landmark, History, Family Fun, USA', 
 'C:/Users/Images/StatueOfLiberty/'
 ),

('Niagara Falls (USA/Canada)', 
 'Niagara Falls is a natural wonder with boat tours that thrill visitors. ...', 
 'North-America', 
 'Nature, Adventure, Travel, USA, Canada', 
 'C:/Users/Images/NiagaraFalls/'
 ),

('Disney World (Florida, USA)', 
 'Disney World in Florida is the ultimate magical experience with four parks. ...', 
 'North-America', 
 'Theme Park, Magic, Family Fun, USA', 
 'C:/Users/Images/DisneyWorld/'
 ),
 
 ('Grand Canyon (Arizona, USA)', 
 'The Grand Canyon offers incredible views and fun hiking trails. ...', 
 'North-America', 
 'Nature, Adventure, USA, Travel', 
 'C:/Users/Images/GrandCanyon/'
 ),

('Smithsonian Air and Space Museum (Washington, DC, USA)', 
 'This museum is a hit with kids interested in airplanes and space exploration. ...', 
 'North-America', 
 'Museum, Education, Family Fun, USA', 
 'C:/Users/Images/SmithsonianAirSpace/'
 ),
  
('Christ the Redeemer (Rio de Janeiro, Brazil)', 
 'The Christ the Redeemer statue offers panoramic views of Rio. ...', 
 'South-America', 
 'Landmark, Culture, Brazil, Adventure', 
 'C:/Users/Images/ChristRedeemer/'
 ),

('Iguazu Falls (Argentina/Brazil)', 
 'Iguazu Falls is a natural wonder with dramatic waterfalls. ...', 
 'South-America', 
 'Nature, Travel, Family Fun, Brazil, Argentina', 
 'C:/Users/Images/IguazuFalls/'
 ),

('Machu Picchu (Peru)', 
 'Machu Picchu is a historical Incan site with breathtaking views. ...', 
 'South-America', 
 'History, Adventure, Travel, Peru', 
 'C:/Users/Images/MachuPicchu/'
 ),
 
 ('La Paz Cable Cars (Bolivia)', 
 'The La Paz cable cars offer amazing views of the city and mountains. ...', 
 'South-America', 
 'Adventure, Travel, Bolivia, Family Fun', 
 'C:/Users/Images/LaPazCableCars/'
 ),
 
 ('Victoria Falls (Zambia/Zimbabwe)', 
 'Victoria Falls is one of the world’s largest and most stunning waterfalls. ...', 
 'Africa', 
 'Nature, Adventure, Travel, Zambia, Zimbabwe', 
 'C:/Users/Images/VictoriaFalls/'
 ),

('Maasai Mara Safari (Kenya)', 
 'A safari in Maasai Mara introduces kids to Africa\'s incredible wildlife. ...', 
 'Africa', 
 'Wildlife, Nature, Kenya, Adventure', 
 'C:/Users/Images/MaasaiMara/'
 ),

('Robben Island (South Africa)', 
 'Visit Robben Island to learn about South Africa\'s history and Nelson Mandela. ...', 
 'Africa', 
 'History, Culture, South Africa', 
 'C:/Users/Images/RobbenIsland/'
 ),

('Zanzibar Beaches (Tanzania)', 
 'Zanzibar offers beautiful beaches and cultural experiences for families. ...', 
 'Africa', 
 'Beach, Culture, Tanzania, Travel', 
 'C:/Users/Images/ZanzibarBeaches/'
 ),
 
(
    'Navagio Beach (Zakynthos, Greece)',
    'Navagio Beach, also known as Shipwreck Beach, is one of the most stunning and iconic beaches in Europe. \n
    Located on the island of Zakynthos, it features dramatic cliffs and turquoise waters, with a famous shipwreck on its golden sands. \n
    Perfect for nature lovers and beach enthusiasts, this beach offers breathtaking views and a serene escape from the everyday!',
    'Europe',
    'Beach, Nature, Travel, Greece, Island, Shipwreck, Stunning Views, Turquoise Waters, Summer, Vacation, Mediterranean, Coastal Beauty, Zakynthos',
    'C:/Users/Images/NavagioBeach/'
),

(
    'Baía do Sancho (Fernando de Noronha, Brazil)',
    'Baía do Sancho is often regarded as one of the most beautiful beaches in the world. \n
    Located on the island of Fernando de Noronha, Brazil, this pristine beach boasts crystal-clear waters, dramatic cliffs, and abundant marine life.\n
    Perfect for those seeking natural beauty and tranquility, it’s a paradise for swimmers, divers, and beach lovers alike!',
    'South-America',
    'Beach, Nature, Travel, Brazil, Fernando de Noronha, Paradise, Crystal-clear Waters, Marine Life, Diving, Island, Tropical, Vacation, Coastal Beauty',
    'C:/Users/Images/BaiaDoSancho/'
),

('Rainforest',
'A panoramic 360° view of a lush tropical rainforest with towering trees, dense green foliage, cascading vines, and sunlight filtering through the canopy',
'South-America',
'rainforest, tree, tropical, leafs, nature',
'C:/Users/Images/Rainforest/'
),

(
    'Mount Fuji (Japan)',
    'Mount Fuji, Japan’s highest and most famous peak, is a stunning and iconic mountain. \n
    It is renowned for its perfectly symmetrical cone shape and its spiritual significance in Japanese culture. \n
    Visitors can hike to the summit during the climbing season or enjoy breathtaking views of the mountain from the surrounding lakes. \n
    It’s a must-see for nature lovers, photographers, and anyone visiting Japan!',
    'Asia-Middle-East',
    'Mountain, Japan, Travel, Nature, Hiking, Fuji, Iconic Landmark, Adventure, Climbing, Beautiful Views, Lakes, Landscape, Culture, Outdoors',
    'C:/Users/Images/MountFuji/'
),

(
    'Table Mountain (Cape Town, South Africa)',
    'Table Mountain is one of the most iconic and exciting places in South Africa. \n
    Visitors can take a cable car to the top and enjoy panoramic views of Cape Town, the ocean, and the surrounding mountains. \n
    The mountain also has kid-friendly hiking trails, an amazing biodiversity of plants and animals, and a variety of fun activities to enjoy. \n
    It’s perfect for an adventurous 11-year-old who loves nature and outdoor exploration!',
    'Africa',
    'Mountain, Nature, Adventure, Hiking, Cable Car, Table Mountain, South Africa, Kids Activities, Family Fun, Cape Town, Outdoor Exploration, Scenic Views, Travel',
    'C:/Users/Images/TableMountain/'
),

(
    'Pyramids of Giza (Giza, Egypt)',
    'The Pyramids of Giza are one of the most awe-inspiring ancient wonders of the world. \n
    Located near Cairo, Egypt, these massive pyramids, including the Great Pyramid of Khufu, have stood for over 4,500 years. \n
    Kids will be fascinated by the mystery of how they were built and the nearby Sphinx. \n
    It’s an incredible historical adventure perfect for any young explorer interested in ancient history and monumental architecture!',
    'Africa',
    'Pyramids, Egypt, Ancient Wonders, History, Travel, Giza, Sphinx, Archaeology, Adventure, Family Fun, Ancient Egypt, Exploration, Iconic Landmarks',
    'C:/Users/Images/PyramidsGiza/'
),

(
    'Galapagos Islands (Ecuador)',
    'The Galapagos Islands are a unique and breathtaking archipelago located in the Pacific Ocean near Ecuador. \n
    Famous for their incredible biodiversity, these islands are home to fascinating wildlife such as giant tortoises, marine iguanas, and blue-footed boobies. \n
    Kids will love exploring the pristine beaches, snorkeling with sea lions, and learning about Charles Darwin\'s studies on evolution. \n
    It’s an unforgettable adventure perfect for any young explorer interested in nature, wildlife, and conservation!',
    'South America',
    'Galapagos, Ecuador, Wildlife, Nature, Biodiversity, Travel, Adventure, Conservation, Exploration, Family Fun, Charles Darwin, Evolution, Iconic Destinations',
    'C:/Users/Images/GalapagosIslands/'
);


select * from images
order by continent

select count(id) from images
order by continent

-- DELETE FROM images
-- WHERE id = 2;



-- Searching for Images Using a Prompt
SELECT 
id, title,content,
image_path
FROM images
WHERE MATCH(title, content, tags) 
      AGAINST('beach' IN NATURAL LANGUAGE MODE) ;

-- Step 4: Perform Full-Text Search Queries
-- Basic Full-Text Search
-- Search for "Disney" and "hamster":
SELECT id, title, image_path, MATCH(title, content, tags) AGAINST('Disney') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('Disney');

SELECT id, title, image_path, MATCH(title, content, tags) AGAINST('Hamster') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('Hamster');

-- Relevancy Sorted Results
-- Search for "theme park" and rank results by relevance:
SELECT id, title, MATCH(title, content, tags) AGAINST('theme park') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('theme park')
ORDER BY relevance DESC;


SELECT id, title, content, MATCH(title, content, tags) AGAINST('nature') AS relevance, tags
FROM images
WHERE MATCH(title, content, tags) AGAINST('nature')
ORDER BY relevance DESC;

-- Boolean Mode Search
-- Search for content that must include "nature" but exclude "forest":
SELECT id, title, content, MATCH(title, content, tags) AGAINST('+nature -forest' IN BOOLEAN MODE) AS relevance, image_path
FROM images
WHERE MATCH(title, content, tags) AGAINST('+nature -forest' IN BOOLEAN MODE)
ORDER BY relevance DESC;


-- Step 5: Advanced Search Using Query Expansion
-- Use MySQL's WITH QUERY EXPANSION to enhance search with related terms:
SELECT  id, title, content, image_path, MATCH(title, content, tags) AGAINST('Disney') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('entertainment' WITH QUERY EXPANSION)
ORDER BY relevance DESC;


-- 6. Searching with a User Input Prompt
-- In a real application, you will probably accept user input 
-- (e.g., via a search form) and then use that input in the query. 
-- For example, in Python (or another language), you would take user input, sanitize it, and pass it into the query.

