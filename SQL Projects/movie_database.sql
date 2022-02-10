-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: movies
-- ------------------------------------------------------
-- Server version	8.0.15

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

--
-- Table structure for table `financial_info`
--
DROP DATABASE IF EXISTS movies;
CREATE DATABASE movies;
USE movies; 

DROP TABLE IF EXISTS `financial_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `financial_info` (
  `id` int(11) DEFAULT NULL,
  `budget` int(11) DEFAULT NULL,
  `revenue` int(11) DEFAULT NULL,
  KEY `id` (`id`),
  CONSTRAINT `financial_info_ibfk_1` FOREIGN KEY (`id`) REFERENCES `titles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `financial_info`
--

LOCK TABLES `financial_info` WRITE;
/*!40000 ALTER TABLE `financial_info` DISABLE KEYS */;
INSERT INTO `financial_info` VALUES (862,30000000,373554033),(8844,65000000,262797249),(15602,0,0),(31357,16000000,81452156),(11862,0,76578911),(949,60000000,187436818),(11860,58000000,0),(45325,0,0),(9091,35000000,64350171),(710,58000000,352194034),(9087,62000000,107879496),(12110,0,0),(21032,0,11348324),(10858,44000000,13681765),(1408,98000000,10017322),(524,52000000,116112375),(4584,16500000,135000000),(5,4000000,4300000),(9273,30000000,212385533),(11517,60000000,35431113);
/*!40000 ALTER TABLE `financial_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `genre` (
  `movie_id` int(11) DEFAULT NULL,
  `genre` set('Action','Adventure','Animation','Comedy','Crime','Drama','Family','Fantasy','History','Horror','Romance','Thriller') DEFAULT NULL,
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `genre_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `titles` (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Animation,Comedy,Family'),(2,'Adventure,Family,Fantasy'),(3,'Comedy,Romance'),(4,'Comedy,Drama,Romance'),(5,'Comedy'),(6,'Action,Drama,Thriller'),(7,'Comedy,Romance'),(8,'Action,Adventure,Drama,Family'),(9,'Action,Adventure,Thriller'),(10,'Action,Adventure,Thriller'),(11,'Comedy,Drama,Romance'),(12,'Comedy,Horror'),(13,'Adventure,Animation,Family'),(14,'Drama,History'),(15,'Action,Adventure'),(16,'Crime,Drama'),(17,'Drama,Romance'),(18,'Comedy,Crime'),(19,'Adventure,Comedy,Crime'),(20,'Action,Adventure,Comedy');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_crew`
--

DROP TABLE IF EXISTS `movie_crew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `movie_crew` (
  `imdb_id` varchar(20) DEFAULT NULL,
  `director` varchar(30) DEFAULT NULL,
  `main_char` varchar(20) DEFAULT NULL,
  `leading_actor` varchar(20) DEFAULT NULL,
  KEY `imdb_id` (`imdb_id`),
  CONSTRAINT `movie_crew_ibfk_1` FOREIGN KEY (`imdb_id`) REFERENCES `titles` (`imdb_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_crew`
--

LOCK TABLES `movie_crew` WRITE;
/*!40000 ALTER TABLE `movie_crew` DISABLE KEYS */;
INSERT INTO `movie_crew` VALUES ('tt0114709','John Lasseter','Woody','Tom Hanks'),('tt0113497','Larry J Franco','Alan Parrish','Robin Williams'),('tt0113228','Howard Deutch','Max Goldman','Walter Mathhau'),('tt0114885','Forest Whitaker','Savannah Vannah','Whitney Houston'),('tt0113041','Alan Silvestri','George Banks','Steve Martin'),('tt0113277','Michael Mann','Vincent Hanna','Al Pacino'),('tt0114319','Sydney Pollack','Linus Larrabee','Harrison Ford'),('tt0112302','David Loughery','Tom Sawyer','Jonathan Taylor'),('tt0114576','Peter Hyams','Darren Thomas','Jean-Claude Van'),('tt0113189','Martin Campbell','James Bond','Pierce Brosnan'),('tt0112346','John Seale','Andrew Shepard','Michael Douglas'),('tt0112896','Adam Weiss','Dracula','Leslie Nielsen'),('tt0112453','Steven Spielberg','Balto','Kevin Bacon'),('tt0113987','Oliver Stone','Richard Nixon','Anthony Hopkins'),('tt0112760','Peter Levy','Morgan Adams','Greena Davis'),('tt0112641','Martin Scorsese','Sam Ace','Robert De Niro'),('tt0114388','Ang Lee','Marianne Dashwood','Kate Winslet'),('tt0113101','Combustible Edison','Ted the Bellhop','Tim Roth'),('tt0112281','Steve Oedekerk','Ace Ventura','Jim Carrey'),('tt0113845','Joseph Ruben','John','Wesley Snipes');
/*!40000 ALTER TABLE `movie_crew` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_summary`
--

DROP TABLE IF EXISTS `movie_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `movie_summary` (
  `movie_id` int(11) DEFAULT NULL,
  `overview` varchar(1000) DEFAULT NULL,
  `adult` char(7) DEFAULT NULL,
  `runtime` int(11) DEFAULT NULL,
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `movie_summary_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `titles` (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_summary`
--

LOCK TABLES `movie_summary` WRITE;
/*!40000 ALTER TABLE `movie_summary` DISABLE KEYS */;
INSERT INTO `movie_summary` VALUES (1,'Led by Woody, Andy\'s toys live happily in his room until Andy\'s birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy\'s heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.','False',81),(2,'When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who\'s been trapped inside the game for 26 years -- into their living room. Alan\'s only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.','False',104),(3,'A family wedding reignites the ancient feud between next-door neighbors and fishing buddies John and Max. Meanwhile, a sultry Italian divorcée opens a restaurant at the local bait shop, alarming the locals who worry she\'ll scare the fish away. But she\'s less interested in seafood than she is in cooking up a hot time with Max.','False',101),(4,'Cheated on, mistreated and stepped on, the women are holding their breath, waiting for the elusive \"good man\" to break a string of less-than-stellar lovers. Friends and confidants Vannah, Bernie, Glo and Robin talk it all out, determined to find a better way to breathe.','False',127),(5,'Just when George Banks has recovered from his daughter\'s wedding, he receives the news that she\'s pregnant ... and that George\'s wife, Nina, is expecting too. He was planning on selling their home, but that\'s a plan that -- like George -- will have to change with the arrival of both a grandchild and a kid of his own.','False',106),(6,'Obsessive master thief, Neil McCauley leads a top-notch crew on various insane heists throughout Los Angeles while a mentally unstable detective, Vincent Hanna pursues him without rest. Each man recognizes and respects the ability and the dedication of the other even though they are aware their cat-and-mouse game may end in violence.','False',170),(7,'An ugly duckling having undergone a remarkable change, still harbors feelings for her crush: a carefree playboy, but not before his business-focused brother has something to say about it.','False',127),(8,'A mischievous young boy, Tom Sawyer, witnesses a murder by the deadly Injun Joe. Tom becomes friends with Huckleberry Finn, a boy with no future and no family. Tom has to choose between honoring a friendship or honoring an oath because the town alcoholic is accused of the murder. Tom and Huck go through several adventures trying to retrieve evidence.','False',97),(9,'International action superstar Jean Claude Van Damme teams with Powers Boothe in a Tension-packed, suspense thriller, set against the back-drop of a Stanley Cup game.Van Damme portrays a father whose daughter is suddenly taken during a championship hockey game. With the captors demanding a billion dollars by game\'s end, Van Damme frantically sets a plan in motion to rescue his daughter and abort an impending explosion before the final buzzer...','False',106),(10,'James Bond must unmask the mysterious head of the Janus Syndicate and prevent the leader from utilizing the GoldenEye weapons system to inflict devastating revenge on Britain.','False',130),(11,'Widowed U.S. president Andrew Shepherd, one of the world\'s most powerful men, can have anything he wants -- and what he covets most is Sydney Ellen Wade, a Washington lobbyist. But Shepherd\'s attempts at courting her spark wild rumors and decimate his approval ratings.','False',106),(12,'When a lawyer shows up at the vampire\'s doorstep, he falls prey to his charms and joins him in his search for fresh blood. Enter Dr. van Helsing, who may be the only one able to vanquish the count.','False',88),(13,'An outcast half-wolf risks his life to prevent a deadly epidemic from ravaging Nome, Alaska.','False',78),(14,'An all-star cast powers this epic look at American President Richard M. Nixon, a man carrying the fate of the world on his shoulders while battling the self-destructive demands within. Spanning his troubled boyhood in California to the shocking Watergate scandal that would end his presidency.','False',192),(15,'Morgan Adams and her slave, William Shaw, are on a quest to recover the three portions of a treasure map. Unfortunately, the final portion is held by her murderous uncle, Dawg. Her crew is skeptical of her leadership abilities, so she must complete her quest before they mutiny against her. This is made yet more difficult by the efforts of the British crown to end her pirate raids.','False',119),(16,'The life of the gambling paradise – Las Vegas – and its dark mafia underbelly.','False',178),(17,'Rich Mr. Dashwood dies, leaving his second wife and her daughters poor by the rules of inheritance. Two daughters are the titular opposites.','False',136),(18,'It\'s Ted the Bellhop\'s first night on the job...and the hotel\'s very unusual guests are about to place him in some outrageous predicaments. It seems that this evening\'s room service is serving up one unbelievable happening after another.','False',98),(19,'Summoned from an ashram in Tibet, Ace finds himself on a perilous journey into the jungles of Africa to find Shikaka, the missing sacred animal of the friendly Wachati tribe. He must accomplish this before the wedding of the Wachati\'s Princess to the prince of the warrior Wachootoos. If Ace fails, the result will be a vicious tribal war.','False',90),(20,'A vengeful New York transit cop decides to steal a trainload of subway fares; his foster brother, a fellow cop, tries to protect him.','False',103);
/*!40000 ALTER TABLE `movie_summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production_company`
--

DROP TABLE IF EXISTS `production_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `production_company` (
  `imdb_id` varchar(20) DEFAULT NULL,
  `prod_comp` varchar(50) DEFAULT NULL,
  `prod_country` varchar(50) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  KEY `imdb_id` (`imdb_id`),
  CONSTRAINT `production_company_ibfk_1` FOREIGN KEY (`imdb_id`) REFERENCES `titles` (`imdb_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production_company`
--

LOCK TABLES `production_company` WRITE;
/*!40000 ALTER TABLE `production_company` DISABLE KEYS */;
INSERT INTO `production_company` VALUES ('tt0114709','Pixar Animation Studios','USA','1995-10-30'),('tt0113497','Tristar Pictures','USA','1995-12-15'),('tt0113228','Warner Bros','USA','1995-12-22'),('tt0114885','Twentieth Century Fox Film','USA','1995-12-22'),('tt0113041','Sandollar Productions','USA','1995-02-10'),('tt0113277','Regency Enterprises','USA','1995-12-15'),('tt0114319','Paramount Pictures','USA, Germany','1995-12-15'),('tt0112302','Walt Disney Pictures','USA','1995-12-22'),('tt0114576','Universal Pictures','USA','1995-12-22'),('tt0113189','United Artist','USA, United Kingdom','1995-11-16'),('tt0112346','Columbia Pictures','USA','1995-11-17'),('tt0112896','Columbia Pictures','USA, France','1995-12-22'),('tt0112453','Universal Pictures','USA','1995-12-22'),('tt0113987','Hollywood Pictures','USA','1995-12-22'),('tt0112760','Le Studio Canal + Mark Productions','USA, Germany, France','1995-12-22'),('tt0112641','Universal Pictures','USA, France','1995-11-22'),('tt0114388','Columbia Pictures','USA, United Kingdom','1995-12-13'),('tt0113101','Miramax Films','USA','1995-12-09'),('tt0112281','Warner Bros','USA','1995-11-10'),('tt0113845','Columbia Pictures','USA','1995-11-21');
/*!40000 ALTER TABLE `production_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ratings` (
  `id` int(11) DEFAULT NULL,
  `popularity` decimal(9,4) DEFAULT NULL,
  KEY `id` (`id`),
  CONSTRAINT `ratings_ibfk_1` FOREIGN KEY (`id`) REFERENCES `titles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
INSERT INTO `ratings` VALUES (862,21.9469),(8844,17.0155),(15602,11.7129),(31357,3.8595),(11862,8.3875),(949,17.9249),(11860,6.6773),(45325,2.5612),(9091,5.2316),(710,14.6860),(9087,6.3184),(12110,5.4303),(21032,12.1407),(10858,5.0920),(1408,7.2845),(524,10.1374),(4584,10.6732),(5,9.0266),(9273,8.2054),(11517,7.3379);
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `titles`
--

DROP TABLE IF EXISTS `titles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `titles` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `imdb_id` varchar(20) DEFAULT NULL,
  `title` varchar(200) DEFAULT 'Unkown Name',
  PRIMARY KEY (`id`),
  UNIQUE KEY `movie_id` (`movie_id`),
  UNIQUE KEY `imdb_id` (`imdb_id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `titles`
--

LOCK TABLES `titles` WRITE;
/*!40000 ALTER TABLE `titles` DISABLE KEYS */;
INSERT INTO `titles` VALUES (5,18,'tt0113101','Four Rooms'),(524,16,'tt0112641','Casino'),(710,10,'tt0113189','GoldenEye'),(862,1,'tt0114709','Toy Story'),(949,6,'tt0113277','Heat'),(1408,15,'tt0112760','Cutthroat Island'),(4584,17,'tt0114388','Sense and Sensibility'),(8844,2,'tt0113497','Jumanji'),(9087,11,'tt0112346','The American President'),(9091,9,'tt0114576','Sudden Death'),(9273,19,'tt0112281','Ace Ventura: When Nature Calls'),(10858,14,'tt0113987','Nixon'),(11517,20,'tt0113845','Money Train'),(11860,7,'tt0114319','Sabrina'),(11862,5,'tt0113041','Father of the Bride Part II'),(12110,12,'tt0112896','Dracula: Dead and Loving It'),(15602,3,'tt0113228','Grumpier Old Men'),(21032,13,'tt0112453','Balto'),(31357,4,'tt0114885','Waiting to Exhale'),(45325,8,'tt0112302','Tom and Huck');
/*!40000 ALTER TABLE `titles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'movies'
--

--
-- Dumping routines for database 'movies'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-04 22:56:09
