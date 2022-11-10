-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: dataBucket
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logs` (
  `dateTime` datetime DEFAULT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `rewardClaimed` varchar(255) DEFAULT NULL,
  `billTotal` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
INSERT INTO `logs` VALUES ('2022-11-08 14:23:26','pooshpal','True',400),('2022-11-08 14:23:26','pooshpal','False',100),('2022-11-08 14:23:26','tom','True',500),('2022-11-08 14:23:26','tom','False',400),('2022-11-08 14:52:11','pooshpal','True',1375),('2022-11-08 14:54:36','pooshpal','True',700),('2022-11-08 14:57:55','tom','False',650),('2022-11-08 14:57:55','tom','True',490),('2022-11-08 14:57:55','pooshpal','True',850),('2022-11-08 15:11:40','mihir','False',850),('2022-11-08 15:11:40','mihir','True',185),('2022-11-08 15:13:39','naman','False',1100),('2022-11-08 15:17:12','naman','False',350),('2022-11-08 17:06:51','pooshpal','True',410),('2022-11-09 09:02:15','naman','False',150),('2022-11-10 08:26:36','meghana','False',300),('2022-11-10 08:26:36','meghana','True',480),('2022-11-10 09:30:21','medha','False',750);
/*!40000 ALTER TABLE `logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `productCode` varchar(255) DEFAULT NULL,
  `productName` varchar(255) DEFAULT NULL,
  `productPrice` int DEFAULT NULL,
  `unitsSold` int DEFAULT NULL,
  `unitsSold_reward` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('LP','Laptop',250,6,1),('CP','CPU',450,7,0),('MN','Monitor',150,10,0),('CA','Cables',50,10,0),('KB','Keyboard',100,7,2),('MO','Mouse',75,2,0),('RM','RAM',300,3,2),('GP','GPU',350,2,2);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rewards`
--

DROP TABLE IF EXISTS `rewards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rewards` (
  `dateTime_allocated` datetime DEFAULT NULL,
  `dateTime_claimed` datetime DEFAULT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `rewardToken` varchar(255) DEFAULT NULL,
  `category` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rewards`
--

LOCK TABLES `rewards` WRITE;
/*!40000 ALTER TABLE `rewards` DISABLE KEYS */;
INSERT INTO `rewards` VALUES ('2022-11-08 14:23:26','2022-11-08 14:57:55','pooshpal','LP%20',2,'CLAIMED'),('2022-11-08 14:23:26',NULL,'pooshpal','CP%30',3,'ACTIVE'),('2022-11-08 14:23:26',NULL,'tom','MN%10',1,'ACTIVE'),('2022-11-08 14:23:26',NULL,'tom','CP%30',3,'ACTIVE'),('2022-11-08 14:49:45',NULL,'pooshpal','LP%0',0,'ACTIVE'),('2022-11-08 14:52:11',NULL,'pooshpal','LP%0',0,'ACTIVE'),('2022-11-08 14:54:36',NULL,'pooshpal','GP%30',3,'ACTIVE'),('2022-11-08 14:57:55','2022-11-08 14:57:55','tom','GP%30',3,'CLAIMED'),('2022-11-08 14:57:55',NULL,'tom','GP%20',2,'ACTIVE'),('2022-11-08 14:57:55','2022-11-08 17:06:51','pooshpal','KB%40',4,'CLAIMED'),('2022-11-08 15:11:40','2022-11-08 15:11:40','mihir','KB%40',4,'CLAIMED'),('2022-11-08 15:11:40',NULL,'mihir','KB%10',1,'ACTIVE'),('2022-11-08 15:13:39',NULL,'naman','RM%50',5,'ACTIVE'),('2022-11-08 15:17:12',NULL,'naman','RM%20',2,'ACTIVE'),('2022-11-08 17:06:51',NULL,'pooshpal','RM%20',2,'ACTIVE'),('2022-11-09 09:02:15',NULL,'naman','RM%10',1,'ACTIVE'),('2022-11-10 08:26:36','2022-11-10 08:26:36','meghana','RM%20',2,'CLAIMED'),('2022-11-10 08:26:36','2022-11-10 08:26:36','meghana','RM%20',2,'CLAIMED'),('2022-11-10 09:30:21',NULL,'medha','MO%40',4,'ACTIVE');
/*!40000 ALTER TABLE `rewards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-10  9:42:17
