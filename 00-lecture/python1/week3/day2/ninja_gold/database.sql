CREATE DATABASE  IF NOT EXISTS `ninja_gold_december` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ninja_gold_december`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: ninja_gold_december
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gold_amount` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_activities_users_idx` (`user_id`),
  KEY `fk_activities_locations1_idx` (`location_id`),
  CONSTRAINT `fk_activities_locations1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_activities_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (1,-35,'2018-12-11 18:46:46','2018-12-11 18:46:46',1,4),(2,25,'2018-12-11 18:46:54','2018-12-11 18:46:54',2,4),(3,7,'2018-12-11 18:47:13','2018-12-11 18:47:13',3,1),(4,7,'2018-12-18 18:56:44','2018-12-18 18:56:44',5,1),(5,-20,'2018-12-18 18:57:03','2018-12-18 18:57:03',5,4),(6,-20,'2018-12-20 18:07:31','2018-12-20 18:07:31',5,4),(7,5,'2018-12-20 18:38:26','2018-12-20 18:38:26',5,3),(8,2,'2018-12-20 18:38:27','2018-12-20 18:38:27',5,3),(9,12,'2018-12-20 18:38:29','2018-12-20 18:38:29',5,2),(10,12,'2018-12-20 18:38:30','2018-12-20 18:38:30',5,2),(11,19,'2018-12-20 18:38:31','2018-12-20 18:38:31',5,2),(12,20,'2018-12-20 18:38:31','2018-12-20 18:38:31',5,2),(13,9,'2018-12-20 18:38:32','2018-12-20 18:38:32',5,1),(14,10,'2018-12-20 18:38:33','2018-12-20 18:38:33',5,1),(15,-21,'2018-12-20 18:38:34','2018-12-20 18:38:34',5,4),(16,-11,'2018-12-20 18:38:35','2018-12-20 18:38:35',5,4),(17,-28,'2018-12-20 18:38:36','2018-12-20 18:38:36',5,4),(18,-34,'2018-12-20 18:38:37','2018-12-20 18:38:37',5,4),(19,-35,'2018-12-20 18:38:37','2018-12-20 18:38:37',5,4),(20,11,'2018-12-20 18:38:38','2018-12-20 18:38:38',5,4),(21,22,'2018-12-20 18:38:39','2018-12-20 18:38:39',5,4),(22,10,'2018-12-20 18:38:39','2018-12-20 18:38:39',5,4),(23,2,'2018-12-20 18:38:40','2018-12-20 18:38:40',5,4),(24,31,'2018-12-20 18:38:41','2018-12-20 18:38:41',5,4),(25,-20,'2018-12-20 18:38:42','2018-12-20 18:38:42',5,4),(26,12,'2018-12-20 18:38:45','2018-12-20 18:38:45',5,2),(27,5,'2018-12-20 18:38:46','2018-12-20 18:38:46',5,3),(28,7,'2018-12-20 18:38:47','2018-12-20 18:38:47',5,1),(29,19,'2018-12-20 18:38:47','2018-12-20 18:38:47',5,2),(30,3,'2018-12-20 18:38:49','2018-12-20 18:38:49',5,3),(31,4,'2018-12-20 18:38:49','2018-12-20 18:38:49',5,3),(32,4,'2018-12-20 18:38:50','2018-12-20 18:38:50',5,3),(33,2,'2018-12-20 18:38:50','2018-12-20 18:38:50',5,3),(34,41,'2018-12-20 18:38:51','2018-12-20 18:38:51',5,4),(35,20,'2018-12-20 18:38:52','2018-12-20 18:38:52',5,4),(36,-8,'2018-12-20 18:38:52','2018-12-20 18:38:52',5,4),(37,22,'2018-12-20 18:38:52','2018-12-20 18:38:52',5,4),(38,-36,'2018-12-20 18:38:53','2018-12-20 18:38:53',5,4);
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `min_gold` int(11) NOT NULL,
  `max_gold` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'cave',5,10,'2018-12-11 18:45:20','2018-12-11 18:45:20'),(2,'farm',10,20,'2018-12-11 18:45:29','2018-12-11 18:45:29'),(3,'house',2,5,'2018-12-11 18:45:39','2018-12-11 18:45:39'),(4,'casino',-50,50,'2018-12-11 18:45:50','2018-12-11 18:45:50');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gold` int(11) NOT NULL DEFAULT '0',
  `pw_hash` varchar(500) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Wes','Harper','wharper@codingdojo.com',0,'password','2018-12-11 18:43:20','2018-12-11 18:43:20'),(2,'Chris','Honeycutt','choneycutt@test.com',0,'password','2018-12-11 18:43:55','2018-12-11 18:43:55'),(3,'Ulises','Gomez','ugomez@test.com',0,'password','2018-12-11 18:44:12','2018-12-11 18:44:12'),(5,'Wes','Harper','wes@wes.com',121,'$2b$12$pVEXqNzJpSD/MA9pS3ytoOrlC6ao2TdmCsBO4oswnhZ0O7OOtha9i','2018-12-13 18:52:22','2018-12-13 18:52:22'),(6,'Other','Other','other@other.com',0,'$2b$12$pLNB9Tb3xbEJ4K6ZPejp/O/ztgBivCttwm.LlbufVi1qlKxBdIQ6C','2018-12-13 19:04:14','2018-12-13 19:04:14');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-20 18:53:02
