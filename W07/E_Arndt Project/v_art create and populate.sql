-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: v_art
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP SCHEMA IF EXISTS v_art;
CREATE SCHEMA IF NOT EXISTS v_art;
USE v_art;
--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `artist` (
  `artist_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `mname` varchar(20) DEFAULT NULL,
  `lname` varchar(25) NOT NULL,
  `dob` int(4) NOT NULL,
  `dod` int(4) DEFAULT NULL,
  `country` varchar(25) NOT NULL,
  `local` enum('y','n') DEFAULT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES (1,'Vincent',NULL,'van Gogh',1853,1890,'France','n'),(2,'Rembrandt','Harmenszoon','van Rijn',1606,1669,'Netherlands','n'),(3,'Leonardo',NULL,'da Vinci',1452,1519,'Italy','n'),(4,'Venture','Lonzo','Coy',1965,NULL,'United States','y'),(5,'Deborah',NULL,'Gill',1970,NULL,'United States','y'),(6,'Claude',NULL,'Monet',1840,1926,'France','n'),(7,'Pablo',NULL,'Picasso',1904,1973,'Spain','n'),(8,'Michelangelo','di Lodovico','Simoni',1475,1564,'Italy','n');
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artwork`
--

DROP TABLE IF EXISTS `artwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `artwork` (
  `artwork_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `artyear` int(4) NOT NULL,
  `period` varchar(25) DEFAULT NULL,
  `artdescription` varchar(200) DEFAULT NULL,
  `arttype` varchar(50) DEFAULT NULL,
  `artlocation` varchar(100) DEFAULT NULL,
  `donated` varchar(75) DEFAULT NULL,
  `artfile` varchar(25) NOT NULL,
  `artist_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_id`),
  KEY `fk_artwork_artist_idx` (`artist_id`),
  CONSTRAINT `fk_artwork_artist` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`artist_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artwork`
--

LOCK TABLES `artwork` WRITE;
/*!40000 ALTER TABLE `artwork` DISABLE KEYS */;
INSERT INTO `artwork` VALUES (1,'Irises',1889,'Impressionism',NULL,'Oil','J. Paul Getty Museum',NULL,'irises.jpg',1),(2,'Starry Night',1889,'Post-impressionism',NULL,'Oil','Museum of Modern Art','Lillie P. Bliss Bequest','starrynight.jpg',1),(3,'Sunflowers',1888,'Post-impressionism',NULL,'Oil on canvas','London National Gallery',NULL,'sunflowers.jpg',1),(4,'Night Watch',1642,'Baroque','The Night Watch is one of the most famous Dutch paintings','Oil on canvas','Amsterdam Museum',NULL,'nightwatch.jpg',2),(5,'Storm on the Sea of Galilee',1633,'Dutch Golden Age',NULL,'Oil paint','Isabelle Stewart Gardner Museum',NULL,'stormgalilee.jpg',2),(6,'Head of a Woman',1508,'High Renaissance','also known as La Scapigliata','Oil paint','Galleria Nazionale di Parma',NULL,'headwoman.jpg',3),(7,'Last Supper',1498,'Renaissance',NULL,'Tempra','Santa Maria delle Grazie','Chester Dale','lastsupper.jpg',3),(8,'Mona Lisa',1517,'Renaissance','The Mona Lisa is acclaimed as the best known, and the most visited','Oil','Louvre',NULL,'monalisa.jpg',3),(9,'Hillside Stream',2005,'Modern',NULL,'Oil',NULL,NULL,'hillsidestream.jpg',4),(10,'Old Barn',1992,'Modern',NULL,'Oil',NULL,NULL,'oldbarn.jpg',4),(11,'Beach Baby',1999,'Modern',NULL,'Watercolor','Gill Gallery',NULL,'beachbaby.jpg',5),(12,'Women in the Garden',1866,'Impressionism',NULL,'Oil','Musee d-Orsay',NULL,'womengarden.jpg',6),(13,'Old Guitartist',1904,'Modern',NULL,'Oil','Art Institute of Chicago',NULL,'guitarist.jpg',7),(14,'Sistine Chapel Ceiling',1512,'Renaissance',NULL,'Fresco','Sistine Chapel, Vatican City',NULL,'chapel.jpg',8),(15,'Madonna della Pietà',1499,'Renaissance','The only work of art Michelangelo ever signed','Marble','St. Peter\'s Basilica, Vatican City',NULL,'pieta.jpg',8),(16,'The Conversion of Saul',1545,'Renaissance',NULL,'Fresco','Cappella Paolina Chapel, Vatican City',NULL,'saul.jpg',8);
/*!40000 ALTER TABLE `artwork` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artwork_keyword`
--

DROP TABLE IF EXISTS `artwork_keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `artwork_keyword` (
  `artwork_id` int(11) NOT NULL,
  `keyword_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_id`,`keyword_id`),
  KEY `fk_artwork_has_keyword_keyword1_idx` (`keyword_id`),
  KEY `fk_artwork_has_keyword_artwork1_idx` (`artwork_id`),
  CONSTRAINT `fk_artwork_has_keyword_artwork1` FOREIGN KEY (`artwork_id`) REFERENCES `artwork` (`artwork_id`),
  CONSTRAINT `fk_artwork_has_keyword_keyword1` FOREIGN KEY (`keyword_id`) REFERENCES `keyword` (`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artwork_keyword`
--

LOCK TABLES `artwork_keyword` WRITE;
/*!40000 ALTER TABLE `artwork_keyword` DISABLE KEYS */;
INSERT INTO `artwork_keyword` VALUES (1,1),(3,1),(12,1),(2,2),(13,2),(2,3),(9,3),(10,3),(12,3),(4,4),(6,4),(8,4),(15,4),(4,5),(5,5),(6,5),(7,5),(8,5),(11,5),(12,5),(13,5),(14,5),(15,5),(16,5),(4,6),(5,7),(5,8),(9,8),(11,8),(5,9),(7,9),(14,9),(15,9),(16,9),(7,10),(11,11);
/*!40000 ALTER TABLE `artwork_keyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keyword`
--

DROP TABLE IF EXISTS `keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `keyword` (
  `keyword_id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(15) NOT NULL,
  PRIMARY KEY (`keyword_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keyword`
--

LOCK TABLES `keyword` WRITE;
/*!40000 ALTER TABLE `keyword` DISABLE KEYS */;
INSERT INTO `keyword` VALUES (1,'flowers'),(2,'blue'),(3,'landscape'),(4,'girl'),(5,'people'),(6,'battle'),(7,'boat'),(8,'water'),(9,'Christ'),(10,'food'),(11,'baby');
/*!40000 ALTER TABLE `keyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'v_art'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-07  8:27:15

-- END OF v_art