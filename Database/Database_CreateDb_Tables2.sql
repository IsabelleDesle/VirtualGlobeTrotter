/* Here is how you can implement the Disneyland Paris content example in MySQL with full-text search. 
The example includes creating a database, 
a table with a FULLTEXT index, inserting the content, and running a full-text search query.*/

create database vgt2
-- drop database vgt2

-- create table. 
-- FULLTEXT(title, content, tags) creates a full-text index for efficient searching across these columns.

CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    tags TEXT,
    image_path VARCHAR(255),
    FULLTEXT(title, content, tags)
) ENGINE=InnoDB;




-- Step 3: Insert the Content

INSERT INTO images (title, content, tags, image_path) 
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
    'Magic, Theme Park, Family Fun, Disney, France, Travel, Attractions, Adventure, Fairy Tales, Entertainment, Europe', 
    'C:/Users/desle/OneDrive/2S1_005_TEAM_PROJECT/Images_4K/Disney'
);

INSERT INTO images (title, content, tags, image_path) 
VALUES
('Sunset at the Beach', 
'A beautiful sunset over the ocean with vibrant colors.', 
'sunset, beach, ocean, nature', 
'C:/Users/desle/OneDrive/2S1_005_TEAM_PROJECT/Images_4K/Beach')
;

INSERT INTO images (title, content, tags, image_path) 
VALUES
('Rainforest',
'A panoramic 360° view of a lush tropical rainforest with towering trees, dense green foliage, cascading vines, and sunlight filtering through the canopy',
'rainforest, tree, tropical, leafs, nature',
'C:/Users/desle/OneDrive/2S1_005_TEAM_PROJECT/Images_4K/Rainforest')
;
/*
-- Searching for Images Using a Prompt
SELECT 
id, title,content, 
image_path
FROM images
WHERE MATCH(title, content, tags) 
      AGAINST('beach' IN NATURAL LANGUAGE MODE) ;

-- Step 4: Perform Full-Text Search Queries
-- Basic Full-Text Search
-- Search for "Disney":
SELECT id, title, image_path, MATCH(title, content, tags) AGAINST('Disney') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('Disney');

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
-- Search for content that must include "beach" but exclude "Halloween":
SELECT id, title, content, image_path, MATCH(title, content, tags) AGAINST('Disney') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('+beach -Halloween' IN BOOLEAN MODE);


-- Step 5: Advanced Search Using Query Expansion
-- Use MySQL's WITH QUERY EXPANSION to enhance search with related terms:
SELECT  id, title, content, image_path, MATCH(title, content, tags) AGAINST('Disney') AS relevance
FROM images
WHERE MATCH(title, content, tags) AGAINST('entertainment' WITH QUERY EXPANSION);


-- 6. Searching with a User Input Prompt
-- In a real application, you will probably accept user input 
-- (e.g., via a search form) and then use that input in the query. 
-- For example, in Python (or another language), you would take user input, sanitize it, and pass it into the query.

*/


