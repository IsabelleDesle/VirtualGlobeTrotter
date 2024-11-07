-- Create the database
CREATE DATABASE VirtualGlobeTrotter;

-- Use the database
USE VirtualGlobeTrotter;

-- Create the Music table with the Tag column as VARCHAR(999)
CREATE TABLE Music (
    MusicID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Artist VARCHAR(255) NOT NULL,
    Album VARCHAR(255),
    ReleaseYear INT,
    Tag VARCHAR(999)
);

-- Create the Image table with the Tag column as VARCHAR(999)
CREATE TABLE Image (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,
    FilePath VARCHAR(255) NOT NULL,
    Description TEXT,
    Tag VARCHAR(999)
);

-- Create the third table that connects Music and Image
CREATE TABLE MusicImage (
    MusicImageID INT AUTO_INCREMENT PRIMARY KEY,
    MusicID INT,
    ImageID INT,
    FOREIGN KEY (MusicID) REFERENCES Music(MusicID),
    FOREIGN KEY (ImageID) REFERENCES Image(ImageID)
);


INSERT INTO Image (FilePath, Description, Tag)
VALUES 
('https://github.com/IsabelleDesle/VirtualGlobeTrotter/blob/main/Database/IMG_20241106_145012.jpg', 'Aligre', 'Paris, city, church');