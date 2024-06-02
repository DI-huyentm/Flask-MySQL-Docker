-- Create the books table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    price INT,
    image VARCHAR(255),
    description VARCHAR(1000)
);

-- Create the stores table
CREATE TABLE stores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the bookstore table (junction table for many-to-many relationship)
CREATE TABLE bookstore (
    book_id INT,
    store_id INT,
    quantity INT DEFAULT 0,
    PRIMARY KEY (book_id, store_id),
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (store_id) REFERENCES stores(id) ON DELETE CASCADE
);


INSERT INTO stores (name) VALUES
('Hanoi'),
('HaiPhong'),
('QuangNinh'),
('HoChiMinh');


INSERT INTO books (title, author, price, image, description) VALUES
('Empire Of The Senseless', 'Acker Kathy', 170000, 'https://m.media-amazon.com/images/I/51kS07+nDwL.jpg', 'Set in the near future, in a Paris devastated by revolution and disease, Empire of the Senseless is narrated by two terrorists and occasional lovers, Thivai, a pirate, and Abhor, part-robot part-human. Together and apart, the two undertake an odyssey of carnage, a holocaust of erotic. \"An elegy for the world of our fathers,\" as Kathy Acker calls it, where the terrorists and the wretched of the earth are in command, marching down a road charted by Genet to a Marseillaise composed by Sade.'),
('In Memoriam To Identity', 'Acosta Oscar Zeta', 210000, 'https://m.media-amazon.com/images/I/71G-8a7RpKL._AC_UF1000,1000_QL80_.jpg', 'In this characteristically sexy, daring, and hyperliterate novel, Kathy Acker interweaves the stories of three characters who share the same tragic flaw: a predilection for doomed, obsessive love. Rimbaud, the delinquent symbolist prodigy, is deserted by his lover Verlaine time and time again. Airplane takes a job dancing at Fun City, the seventh tier of the sex industry, in order to support her good-for-nothing boyfriend.'),
('Art Attack: A Short Cultural History of the Avant-Garde', 'Richard Brautigan', 130000,'https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/HawklineMonster.JPG/220px-HawklineMonster.JPG', 'In the army, the advance guard is the first wave of soldiers who rush into enemy territory, risking their lives to map out the terrain. In the arts, the avant-garde consists of people who have devoted their talents, even their lives, to seeing the future and to confronting others with their visions. This intriguing introduction to modern art examines the avant-garde from its nineteenth-century origins in Paris to its meaning and influence today. It presents the visionaries who took the greatest risks, who saw the furthest, and who made the most challenging art-art that changed how we imagine our world. From cubism to pop art and beyond, this is the story not only of those risk takers, but of their creations and of the times in which they lived. Notes, bibliography, index.'),
('Gang Of Souls: A Generation Of Beat Poets', 'Davis Stephen', 100000, 'https://upload.wikimedia.org/wikipedia/en/a/a6/Cover_of_Richard_Brautigan%27s_June_30th%2C_June_30th.jpg', 'Maria Beatty documentary exploring the insights and influences of the American Beat Poets. The film conveys their consciousness and sensibility through interviews with William Burroughs, Allen Ginsberg, Diane Di Prima, among others. Also weaves in additional commentary from contemporary musicians, poets and writers such as Marianne Faithfull, Richard Hell, Lydia Lunch and Henry Rollins. Also expands upon how the poets reached new levels of creativity and inspired social change.'),
('Women Of The Left Bank: Paris 1900-1940', 'Franck Dan', 100000,  'https://m.media-amazon.com/images/I/81bGWDiGWpL._AC_UF1000,1000_QL80_.jpg', 'These women were part of the artistic community that formed on the Paris Left Bank early in the twentieth century. Their literary contributions—which include major works of prose, poetry, drama, critical and journalistic essays, autobiographies, pensées, and memoirs—display wide-ranging interests and diverse talents. In addition to their own writing activities, several of these women set up bookshops, publishing houses, hand presses, little magazines, and artistic salons through which they advertised and marketed the products of literary Paris.'),
('The Goncourt Brothers', 'Franklin Benjamin V ed.', 220000, 'https://upload.wikimedia.org/wikipedia/en/2/24/RommelDrivesOnDeepIntoEgypt.jpg', 'To trace the roots of the expatriate womans experience in Paris, we must return to a period in history that appears to share as little with Paris between the world wars as Henry James’s New York shares with contemporary Greenwich Village. We must begin with James’s good friend, Edith Wharton, herself a product of Old New York. On a bleak December afternoon in 1893, she stood at the door of a house on the rue Barbet-de-Jouy, a street intersecting the fashionable rue de Varenne, in the heart of the Faubourg St. Germain on the Paris Left Bank.'),
('My Life and Loves in Greenwich Village', 'Frees Paul', 150000,  'https://upload.wikimedia.org/wikipedia/en/c/c7/SombreroFallout.jpg', 'The second phase of the belle époque, between 1900 and the Great War, was marked by advances and retreats, by an emerging Modernism and a clinging to old ways. The twentieth century was ushered into France with the Paris Exhibition. Among the technological advances on display for the world’s fair were the first stone bridge (the Alexandre III), completed just in time for the exhibition, the Paris Metropolitain, which gave underground rides across the city, and two glass exhibition halls, the Grand Palais and the Petit Palais. Seen today, these monuments display a rather quaint and Old World quality, suggesting...'),
('My Sisters Hand In Mine', 'French Warren', 270000,  'https://1960sdaysofrage.files.wordpress.com/2017/06/brautigancover.jpeg', 'Much about the Paris described in previous chapters was unknown to the Americans who invaded the city following World War I: these newcomers were little interested in the “French” aspect of Paris. They sought respite from an America they found to be politically naive, puritanically restrictive, and culturally deprived. For some, the need for escape was itself a sign of self-destructive tendencies. For others, expatriation meant real liberation. For women, America was a particularly oppressive environment, and among the expatriate women were those who took up Edith Whartons “argument with America” on “the woman question,” finding in...'),
('Two Serious Ladies', 'Fritz James', 100000,  'https://mpd-biblio-covers.imgix.net/9780312277109.jpg?w=300', 'Gertrude Stem wrote in Paris France that “every century has a beginning and a middle and an ending. ... it begins that is it has a childhood it has an adolescence it has an adult life, it has a middle life and an older life and then it ends” (116). The birth of the twentieth century coincided with Stein emergence into adulthood; by the time the twentieth century reached its middle age, Stein was dead of cancer in Paris. When she arrived in that city in 1903, the nineteenth century was in its death throes; Paris, like other Kuropean...');

INSERT INTO bookstore(book_id, store_id, quantity) VALUES
(1,1,100),
(2,1,100),
(3,2,400),
(4,1,300),
(5,2,200),
(6,3,600),
(7,4,200),
(8,3,500),
(9,4,800);