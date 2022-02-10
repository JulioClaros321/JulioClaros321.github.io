-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: assign_four
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
-- Table structure for table `aggregatedata`
--

DROP TABLE IF EXISTS `aggregatedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `aggregatedata` (
  `theDate` date DEFAULT NULL,
  `theTime` time DEFAULT NULL,
  `totalCustomers` int(11) DEFAULT NULL,
  `meanAge` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aggregatedata`
--

LOCK TABLES `aggregatedata` WRITE;
/*!40000 ALTER TABLE `aggregatedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `aggregatedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customers` (
  `name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `phone_numb` varchar(12) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `street_numb` int(11) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `city` varchar(15) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `zip_code` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('Julio','Claros',21,'301-580-3642','julio.claros321@gmail.com',123,'Street','Silver Spring','MD',20901),('Ronald','Hernandez',18,'301-796-4040','R.Hernandez@gmailcom',4323,'Sligo Way','Silver Spring','MD',20394),('David','Yeezy',31,'401-304-3020','David.Y21@yahoo.com',321,'Wayne Ave.','Chevy Chase','MD',34031),('Fifa','Champion',30,'312-391-2121','Chamption.F123@gmail.com',432,'Give Me An A Strre','Please','MD',20310),('Ronny','Lel',16,'301-432-1313','Lel_Ronny@gmail.com',523,'Loft Lane','Clarksburg','CA',23232);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-03 13:11:09
