###Schema
DROP DATABASE geek_text_db;
CREATE DATABASE geek_text_db;
USE geek_text_db;

-- Authors table structure
CREATE TABLE Authors
(
    idAuthors       int(11)      NOT NULL PRIMARY KEY,
    authorFirstName varchar(45)  NOT NULL,
    authorLastName  varchar(150) NOT NULL,
    authorPublisher varchar(255) DEFAULT NULL,
    authorBiography text
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- Author's table data:
INSERT INTO Authors (idAuthors, authorFirstName, authorLastName, authorPublisher, authorBiography)
VALUES (1, 'Nikole', 'Hannah-Jones', 'New York : One World',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),
       (2, 'Fu', 'Jiqi', 'Bradford, West Yorkshire : Emerald Publishing Limited',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),
       (3, 'Gabriella', 'Marfe', 'BENTHAM Science PUBLISHER',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.');

-- Books table structure
CREATE TABLE Books
(
    isbn              varchar(55)  NOT NULL PRIMARY KEY,
    idAuthors         int(11)      NOT NULL,
    bookTitle         varchar(100) NOT NULL,
    bookDescription   text,
    bookPrice         double       NOT NULL,
    bookGenre         varchar(80)  NOT NULL,
    bookPublisher     varchar(255) NOT NULL,
    bookYearPublished int(11)      NOT NULL,
    unitsSold         int(11)      NOT NULL,
    bookRating        double       NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- Book's table data:
INSERT INTO Books (isbn, idAuthors, bookTitle, bookDescription, bookPrice, bookGenre, bookPublisher, bookYearPublished,
                   unitsSold, bookRating)
VALUES ('9780567830572', 3, 'HAZARDOUS WASTE MANAGEMENT AND HEALTH RISKS',
        ' 	\r\nHazardous Waste Management and Health Risks presents a systematic overview of evaluating solid and hazardous waste management practices. The book introduces readers to the basic principles of hazardous waste management and progresses into related topics that allow managers to assess environmental quality. These topics include heavy metal pollution, reproductive biomarkers as signals of environmental pressure',
        21, 'Electronic', 'BENTHAM Science PUBLISHER', 2020, 6, 4.5),
       ('9780593230572', 1, 'The 1619 Project : a new origin story',
        'The animating idea of The 1619 Project is that our national narrative is more accurately told if we begin not on July 4, 1776, but in late August of 1619, when a ship arrived in Jamestown bearing a cargo of twenty to thirty enslaved people from Africa. Their arrival inaugurated a barbaric and unprecedented system of chattel slavery that would last for the next 250 years.',
        16.99, 'History', 'New York : One World', 2021, 4, 4.5),
       ('9781800710026', 1, 'And the mountains echoed',
        'Presents a story inspired by human love, how people take care of one another, and how choices resonate through subsequent generations. Afghanistan, 1952. Abdullah and his sister Pari live with their father and step-mother in the small village of Shadbagh. Their father, Saboor, is constantly in search of work and they struggle together through poverty and brutal winters.',
        35.99, 'Domestic fiction', 'New York : Riverhead Books', 2013, 9, 5),
       ('9781800711853', 1, 'Damage Mechanisms in Materials and Structures and Numerical Analysis in Engineering',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        47, 'Electronic', 'Bradford, West Yorkshire : Emerald Publishing Limited', 2020, 2, 5),
       ('9781839822834', 2, 'The Fourth Industrial Revolution (Industry 4. 0)',
        'Exploring blockchain implementation in the supply chain --\r\nIndustry 4.0 adoption as a moderator of the impact of lean production practices on operational performance improvement --\r\nUnderstanding supply chain analytics capabilities and agility for data-rich environments --\r\nThe interplay between smart manufacturing technologies and work organization --\r\nThe impact of 3D printing implementation on stock returns --\r\nLeveraging open-standard interorganizational information systems for process adaptability and alignment --\r\nBlockchain-driven customer order management',
        34.99, 'Electronic', 'Bradford, West Yorkshire : Emerald Publishing Limited', 2019, 1, 5);

-- Rating Comments table structure
CREATE TABLE RatingComments
(
    idRatingComments int(11)      NOT NULL PRIMARY KEY,
    isbn             varchar(55)  NOT NULL,
    idUsers          int(11)      NOT NULL,
    ratingNumber     int(11)      NOT NULL,
    title            varchar(255) NOT NULL,
    comments         text,
    createdAt        datetime     NOT NULL,
    modifiedAt       datetime     DEFAULT NULL,
    status           tinyint(1)   NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- RatingComments' Table data:
INSERT INTO RatingComments (idRatingComments, isbn, idUsers, ratingNumber, title, comments, createdAt, modifiedAt,
                            status)
VALUES (1, '9780567830572', 1, 4, 'Why do we use it?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-27 00:00:00', NULL, 0),
       (2, '9780567830572', 6, 5, 'Where can I get some?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-27 00:00:00', NULL, 0),
       (3, '9780567830572', 4, 5, 'Where does it come from?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-27 00:00:00', NULL, 0),
       (4, '9780593230572', 2, 5, 'Where does it come from?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-27 00:00:00', NULL, 0),
       (5, '9780593230572', 5, 5, 'Where can I get some?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-18 00:00:00', NULL, 0),
       (6, '9780593230572', 1, 3, 'Why do we use it?',
        'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        '2022-01-19 00:00:00', NULL, 0),
       (7, '9781839822834', 6, 1, 'Description based upon print version of record',
        'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.',
        '2022-01-26 00:00:00', NULL, 0),
       (8, '9781839822834', 2, 2, 'Most popular items for December 2021',
        'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.',
        '2022-01-20 00:00:00', NULL, 0);

-- Shopping Cart Items table structure
CREATE TABLE ShoppingCartItems
(
    idShoppingCartItems int(11)     NOT NULL PRIMARY KEY,
    idShoppingCarts     int(11)     NOT NULL,
    isbn                varchar(55) NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ShoppingCartItems table data:
INSERT INTO ShoppingCartItems (idShoppingCartItems, idShoppingCarts, isbn)
VALUES (1, 1, '9780567830572'),
       (2, 1, '9780593230572'),
       (3, 2, '9781800710026'),
       (4, 3, '9781839822834');

-- Shopping Carts table structure
CREATE TABLE ShoppingCarts
(
    idShoppingCarts int(11) NOT NULL PRIMARY KEY,
    idUsers         int(11) NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ShoppingCarts table data:
INSERT INTO ShoppingCarts (idShoppingCarts, idUsers)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6);

-- Credit Cards table structure
CREATE TABLE UserCreditCards
(
    idUserCreditCards    int(11)      NOT NULL PRIMARY KEY,
    idUsers              int(11)      NOT NULL,
    creditCardNumber     varchar(16)  NOT NULL,
    expirationMonth      int(4)       NOT NULL,
    expirationYear       int(8)       NOT NULL,
    securityCode         int(11)      NOT NULL,
    billingStreetAddress varchar(255) NOT NULL,
    billingCity          varchar(255) NOT NULL,
    billingState         varchar(4)   NOT NULL,
    billingZipCode       int(7)       NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- UserCreditCards table data
INSERT INTO UserCreditCards (idUserCreditCards, idUsers, creditCardNumber, expirationMonth, expirationYear,
                             securityCode, billingStreetAddress, billingCity, billingState, billingZipCode)
VALUES (3, 1, '1234567891234569', 12, 2025, 896, '1 Main St.', 'Miami', 'FL', 33123),
       (4, 1, '1234567891234560', 12, 2023, 896, '826 Syracuse Ave.', 'New York', 'NY', 10011),
       (13, 2, '0000000000000000', 01, 2025, 123, '2 Main St.', 'Springfield', 'AL', 12345),
       (14, 2, '9876543219876543', 02, 2025, 456, '3 Main St.', 'Austin', 'TX', 77727),
       (15, 2, '4563219876541236', 03, 2023, 987, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765),
       (16, 3, '3698521478523698', 04, 2023, 963, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765),
       (17, 3, '7412589633698521', 05, 2026, 741, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765),
       (18, 4, '7896541236231569', 06, 2025, 852, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765),
       (19, 5, '1233214566547899', 07, 2025, 147, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765),
       (20, 6, '5698741236985236', 05, 2026, 987, '22232 N. Atlantic Blvd', 'San Diego', 'CA', 98765);

-- Users table structure
CREATE TABLE Users
(
    idUsers      int(11)      NOT NULL PRIMARY KEY,
    first_name   varchar(255) NOT NULL,
    last_name    varchar(255) NOT NULL,
    username     varchar(45)  NOT NULL,
    emailAddress varchar(255) NOT NULL,
    addressLine1 varchar(255) DEFAULT NULL,
    addressLine2 varchar(255) DEFAULT NULL,
    city         varchar(45)  DEFAULT NULL,
    state        varchar(45)  DEFAULT NULL,
    zipcode      int(11)      DEFAULT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- Users table data:

INSERT INTO Users (idUsers, first_name, last_name, username, emailAddress, addressLine1, addressLine2, city, state,
                   zipcode)
VALUES (1, 'Diamond', 'Forbes', 'diamond', 'dforbes@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL', 33199),
       (2, 'Kevin', 'Forero', 'kforero', 'kforero@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL', 33199),
       (3, 'Antonio', 'Franceschi', 'afranceschi', 'afranceschi@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL',
        33199),
       (4, 'Ariadna', 'Franchino', 'afranchino', 'afranchino@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL',
        33199),
       (5, 'Nicole', 'Gentil', 'ngentil', 'ngentil@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL', 33199),
       (6, 'Carlos', 'Gonzalez', 'cmdelapaz', 'cgonz683@fiu.edu', '11200 SW 8th Street', NULL, 'Miami', 'FL', 33199);

-- Wish List Items table structure
CREATE TABLE WishListItems
(
    idWishLists      int(11)     NOT NULL,
    isbn             varchar(55) NOT NULL,
    idWishListsItems int(11)     NOT NULL PRIMARY KEY
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- Wish List Items table data:
INSERT INTO WishListItems (idWishLists, isbn, idWishListsItems)
VALUES (1, '9780567830572', 1),
       (1, '9780593230572', 2),
       (2, '9781800710026', 3),
       (2, '9780567830572', 4),
       (2, '9781839822834', 5),
       (3, '9781839822834', 6);

-- WishLists Table structure
CREATE TABLE WishLists
(
    idWishLists int(11)     NOT NULL PRIMARY KEY,
    idUsers     int(11)     NOT NULL,
    name        varchar(45) NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

INSERT INTO WishLists (idWishLists, idUsers, name)
VALUES (1, 4, 'Christmas List'),
       (2, 6, 'Birthday List'),
       (3, 4, 'Summer List');


-- Add Keys and Auto Increments
ALTER TABLE Authors
    MODIFY idAuthors int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 4;

ALTER TABLE Books
    ADD KEY fk_Books_Authors1_idx (idAuthors);

ALTER TABLE `RatingComments`
    ADD KEY `fk_RatingComments_Books1_idx` (`isbn`),
    ADD KEY `fk_RatingComments_Users1_idx` (`idUsers`),
    MODIFY idRatingComments int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 9;

ALTER TABLE ShoppingCartItems
    ADD KEY fk_ShoppingCartItems_ShoppingCarts1_idx (idShoppingCarts),
    ADD KEY fk_ShoppingCartItems_Books1_idx (isbn),
    MODIFY idShoppingCartItems int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 5;

ALTER TABLE ShoppingCarts
    ADD KEY fk_ShoppingCarts_Users_idx (idUsers),
    MODIFY idShoppingCarts int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 7;

ALTER TABLE UserCreditCards
    ADD UNIQUE KEY creditCardNumber (creditCardNumber),
    ADD KEY fk_USerCreditCards_Users1_idx (idUsers),
    MODIFY idUserCreditCards int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 21;

ALTER TABLE Users
    MODIFY idUsers int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 7;

ALTER TABLE WishListItems
    ADD KEY fk_WishListItems_Books1_idx (isbn),
    ADD KEY fk_WishLIstItems_WishLists1_idx (idWishLists),
    MODIFY idWishListsItems int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 7;

ALTER TABLE WishLists
    ADD KEY fk_WishLists_Users1_idx (idUsers),
    MODIFY idWishLists int(11) NOT NULL AUTO_INCREMENT,
    AUTO_INCREMENT = 4;

-- Table Restrictions
-- Book Table filters
ALTER TABLE Books
    ADD CONSTRAINT fk_Books_Authors1 FOREIGN KEY (idAuthors) REFERENCES Authors (idAuthors) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- RatingComments Table filters
ALTER TABLE RatingComments
    ADD CONSTRAINT fk_RatingComments_Books1 FOREIGN KEY (isbn) REFERENCES Books (isbn) ON DELETE NO ACTION ON UPDATE NO ACTION,
    ADD CONSTRAINT fk_RatingComments_Users1 FOREIGN KEY (idUsers) REFERENCES Users (idUsers) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Shopping Cart Items Table filters
ALTER TABLE ShoppingCartItems
    ADD CONSTRAINT fk_ShoppingCartItems_Books1 FOREIGN KEY (isbn) REFERENCES Books (isbn) ON DELETE NO ACTION ON UPDATE NO ACTION,
    ADD CONSTRAINT fk_ShoppingCartItems_ShoppingCarts1 FOREIGN KEY (idShoppingCarts) REFERENCES ShoppingCarts (idShoppingCarts) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Shopping Carts Table filters
ALTER TABLE ShoppingCarts
    ADD CONSTRAINT fk_ShoppingCarts_Users FOREIGN KEY (idUsers) REFERENCES Users (idUsers) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- User Credit Cards table filters
ALTER TABLE UserCreditCards
    ADD CONSTRAINT fk_UserCreditCards_Users1 FOREIGN KEY (idUsers) REFERENCES Users (idUsers) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Wish List Items table filters
ALTER TABLE WishListItems
    ADD CONSTRAINT fk_WishListItems_Books1 FOREIGN KEY (isbn) REFERENCES Books (isbn) ON DELETE NO ACTION ON UPDATE NO ACTION,
    ADD CONSTRAINT fk_WishListItems_WishLists1 FOREIGN KEY (idWishLists) REFERENCES WishLists (idWishLists) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Wish List table filters
ALTER TABLE WishLists
    ADD CONSTRAINT fk_WishLists_Users1 FOREIGN KEY (idUsers) REFERENCES Users (idUsers) ON DELETE NO ACTION ON UPDATE NO ACTION;
