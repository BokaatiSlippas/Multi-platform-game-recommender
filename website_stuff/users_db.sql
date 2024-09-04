-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 11, 2024 at 08:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users_db`
--
CREATE DATABASE IF NOT EXISTS `users_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `users_db`;

-- --------------------------------------------------------

--
-- Table structure for table `sync_requests`
--

DROP TABLE IF EXISTS `sync_requests`;
CREATE TABLE IF NOT EXISTS `sync_requests` (
  `user_id` int(100) NOT NULL,
  `request_id` int(100) NOT NULL,
  `request_timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `request_int` int(100) DEFAULT NULL,
  `complete` int(5) NOT NULL DEFAULT 0,
  `server_output` int(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`request_timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `verification_code` int(11) NOT NULL,
  `time_verification_code_sent` datetime DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `email_verified_at` datetime DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `age` int(11) DEFAULT NULL,
  `gender` int(4) DEFAULT NULL,
  `pro_package` tinyint(4) NOT NULL DEFAULT 0,
  `daily_recommendations_num` int(11) NOT NULL DEFAULT 3,
  `user_steam_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `date` (`date`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_games`
--

DROP TABLE IF EXISTS `users_games`;
CREATE TABLE IF NOT EXISTS `users_games` (
  `user_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  `playtime` int(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
