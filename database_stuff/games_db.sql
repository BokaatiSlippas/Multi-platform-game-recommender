SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `games_db`
--
CREATE DATABASE IF NOT EXISTS `games_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `games_db`;

-- --------------------------------------------------------

--
-- Table structure for table `age_ratings`
--

DROP TABLE IF EXISTS `age_ratings`;
CREATE TABLE IF NOT EXISTS `age_ratings` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `rating` int(100) DEFAULT NULL,
  `rating_cover_url` varchar(500) DEFAULT NULL,
  `synopsis` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `age_rating_content_descriptions`
--

DROP TABLE IF EXISTS `age_rating_content_descriptions`;
CREATE TABLE IF NOT EXISTS `age_rating_content_descriptions` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `alternative_names`
--

DROP TABLE IF EXISTS `alternative_names`;
CREATE TABLE IF NOT EXISTS `alternative_names` (
  `id` int(100) NOT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `artworks`
--

DROP TABLE IF EXISTS `artworks`;
CREATE TABLE IF NOT EXISTS `artworks` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
CREATE TABLE IF NOT EXISTS `characters` (
  `id` int(100) NOT NULL,
  `country_name` varchar(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(10000) DEFAULT NULL,
  `gender` int(5) DEFAULT NULL,
  `mug_shot` int(100) DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `slug` varchar(1000) DEFAULT NULL,
  `species` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `character_mug_shots`
--

DROP TABLE IF EXISTS `character_mug_shots`;
CREATE TABLE IF NOT EXISTS `character_mug_shots` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collections`
--

DROP TABLE IF EXISTS `collections`;
CREATE TABLE IF NOT EXISTS `collections` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collection_memberships`
--

DROP TABLE IF EXISTS `collection_memberships`;
CREATE TABLE IF NOT EXISTS `collection_memberships` (
  `id` int(100) NOT NULL,
  `collection` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `type` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collection_membership_types`
--

DROP TABLE IF EXISTS `collection_membership_types`;
CREATE TABLE IF NOT EXISTS `collection_membership_types` (
  `id` int(100) NOT NULL,
  `allowed_collection_type` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collection_relations`
--

DROP TABLE IF EXISTS `collection_relations`;
CREATE TABLE IF NOT EXISTS `collection_relations` (
  `id` int(100) NOT NULL,
  `child_collection` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `parent_collection` int(100) DEFAULT NULL,
  `type` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collection_relation_types`
--

DROP TABLE IF EXISTS `collection_relation_types`;
CREATE TABLE IF NOT EXISTS `collection_relation_types` (
  `id` int(100) NOT NULL,
  `allowed_child_type` int(100) DEFAULT NULL,
  `allowed_parent_type` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `collection_types`
--

DROP TABLE IF EXISTS `collection_types`;
CREATE TABLE IF NOT EXISTS `collection_types` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
CREATE TABLE IF NOT EXISTS `companies` (
  `id` int(100) NOT NULL,
  `change_date` bigint(100) DEFAULT NULL,
  `change_date_category` int(100) DEFAULT NULL,
  `changed_company_id` int(100) DEFAULT NULL,
  `country` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `logo` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `parent` int(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `start_date` bigint(100) DEFAULT NULL,
  `start_date_category` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `company_logos`
--

DROP TABLE IF EXISTS `company_logos`;
CREATE TABLE IF NOT EXISTS `company_logos` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `company_websites`
--

DROP TABLE IF EXISTS `company_websites`;
CREATE TABLE IF NOT EXISTS `company_websites` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `trusted` tinyint(3) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `covers`
--

DROP TABLE IF EXISTS `covers`;
CREATE TABLE IF NOT EXISTS `covers` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `game_localization` int(100) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(500) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
CREATE TABLE IF NOT EXISTS `events` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `end_time` int(100) DEFAULT NULL,
  `event_logo` int(100) DEFAULT NULL,
  `live_stream_url` varchar(500) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `start_time` int(100) DEFAULT NULL,
  `time_zone` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_logos`
--

DROP TABLE IF EXISTS `event_logos`;
CREATE TABLE IF NOT EXISTS `event_logos` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `event` int(100) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_networks`
--

DROP TABLE IF EXISTS `event_networks`;
CREATE TABLE IF NOT EXISTS `event_networks` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `event` int(100) DEFAULT NULL,
  `network_type` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `external_games`
--

DROP TABLE IF EXISTS `external_games`;
CREATE TABLE IF NOT EXISTS `external_games` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `media` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `platform` int(100) DEFAULT NULL,
  `uid` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `year` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `franchises`
--

DROP TABLE IF EXISTS `franchises`;
CREATE TABLE IF NOT EXISTS `franchises` (
  `id` int(100) NOT NULL,
  `created_at` bigint(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
CREATE TABLE IF NOT EXISTS `games` (
  `id` int(100) NOT NULL,
  `aggregated_rating` double DEFAULT NULL,
  `aggregated_rating_count` int(100) DEFAULT NULL,
  `category` int(100) DEFAULT NULL,
  `collection` int(100) DEFAULT NULL,
  `cover` int(100) DEFAULT NULL,
  `created_at` bigint(100) DEFAULT NULL,
  `first_release_date` int(100) DEFAULT NULL,
  `follows` int(100) DEFAULT NULL,
  `franchise` int(100) DEFAULT NULL,
  `hypes` int(100) DEFAULT NULL,
  `name` longtext DEFAULT NULL,
  `parent_game` int(100) DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `rating_count` int(100) DEFAULT NULL,
  `slug` longtext DEFAULT NULL,
  `status` int(100) DEFAULT NULL,
  `storyline` longtext DEFAULT NULL,
  `summary` longtext DEFAULT NULL,
  `total_rating` double DEFAULT NULL,
  `total_rating_count` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `version_parent` int(100) DEFAULT NULL,
  `version_title` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_engines`
--

DROP TABLE IF EXISTS `game_engines`;
CREATE TABLE IF NOT EXISTS `game_engines` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `logo` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_engine_logos`
--

DROP TABLE IF EXISTS `game_engine_logos`;
CREATE TABLE IF NOT EXISTS `game_engine_logos` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_localizations`
--

DROP TABLE IF EXISTS `game_localizations`;
CREATE TABLE IF NOT EXISTS `game_localizations` (
  `id` int(100) NOT NULL,
  `cover` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `region` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_modes`
--

DROP TABLE IF EXISTS `game_modes`;
CREATE TABLE IF NOT EXISTS `game_modes` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_versions`
--

DROP TABLE IF EXISTS `game_versions`;
CREATE TABLE IF NOT EXISTS `game_versions` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_version_features`
--

DROP TABLE IF EXISTS `game_version_features`;
CREATE TABLE IF NOT EXISTS `game_version_features` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `position` int(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_version_feature_values`
--

DROP TABLE IF EXISTS `game_version_feature_values`;
CREATE TABLE IF NOT EXISTS `game_version_feature_values` (
  `id` int(100) NOT NULL,
  `game` int(100) DEFAULT NULL,
  `game_feature` int(100) DEFAULT NULL,
  `included_feature` int(100) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `game_videos`
--

DROP TABLE IF EXISTS `game_videos`;
CREATE TABLE IF NOT EXISTS `game_videos` (
  `id` int(100) NOT NULL,
  `game` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `video_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
CREATE TABLE IF NOT EXISTS `genres` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `involved_companies`
--

DROP TABLE IF EXISTS `involved_companies`;
CREATE TABLE IF NOT EXISTS `involved_companies` (
  `id` int(100) NOT NULL,
  `company` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `developer` tinyint(3) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `porting` tinyint(3) DEFAULT NULL,
  `publisher` tinyint(3) DEFAULT NULL,
  `supporting` tinyint(3) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `keywords`
--

DROP TABLE IF EXISTS `keywords`;
CREATE TABLE IF NOT EXISTS `keywords` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
CREATE TABLE IF NOT EXISTS `languages` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `locale` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `native_name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `language_supports`
--

DROP TABLE IF EXISTS `language_supports`;
CREATE TABLE IF NOT EXISTS `language_supports` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `language` int(100) DEFAULT NULL,
  `language_support_type` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `language_support_types`
--

DROP TABLE IF EXISTS `language_support_types`;
CREATE TABLE IF NOT EXISTS `language_support_types` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_age_ratings_content_descriptions`
--

DROP TABLE IF EXISTS `link_age_ratings_content_descriptions`;
CREATE TABLE IF NOT EXISTS `link_age_ratings_content_descriptions` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `age_rating_id` int(100) NOT NULL,
  `age_rating_content_description_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_characters_akas`
--

DROP TABLE IF EXISTS `link_characters_akas`;
CREATE TABLE IF NOT EXISTS `link_characters_akas` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `character_id` int(100) NOT NULL,
  `aka` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_characters_games`
--

DROP TABLE IF EXISTS `link_characters_games`;
CREATE TABLE IF NOT EXISTS `link_characters_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `character_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_collections_as_child_relations`
--

DROP TABLE IF EXISTS `link_collections_as_child_relations`;
CREATE TABLE IF NOT EXISTS `link_collections_as_child_relations` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `collection_id` int(100) NOT NULL,
  `collection_relation_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_collections_as_parent_relations`
--

DROP TABLE IF EXISTS `link_collections_as_parent_relations`;
CREATE TABLE IF NOT EXISTS `link_collections_as_parent_relations` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `collection_id` int(100) NOT NULL,
  `collection_relation_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_collections_games`
--

DROP TABLE IF EXISTS `link_collections_games`;
CREATE TABLE IF NOT EXISTS `link_collections_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `collection_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_companies_developed`
--

DROP TABLE IF EXISTS `link_companies_developed`;
CREATE TABLE IF NOT EXISTS `link_companies_developed` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `company_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_companies_published`
--

DROP TABLE IF EXISTS `link_companies_published`;
CREATE TABLE IF NOT EXISTS `link_companies_published` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `company_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_companies_websites`
--

DROP TABLE IF EXISTS `link_companies_websites`;
CREATE TABLE IF NOT EXISTS `link_companies_websites` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `company_id` int(100) NOT NULL,
  `company_website_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_events_event_networks`
--

DROP TABLE IF EXISTS `link_events_event_networks`;
CREATE TABLE IF NOT EXISTS `link_events_event_networks` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `event_id` int(100) NOT NULL,
  `event_network_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_events_games`
--

DROP TABLE IF EXISTS `link_events_games`;
CREATE TABLE IF NOT EXISTS `link_events_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `event_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_events_videos`
--

DROP TABLE IF EXISTS `link_events_videos`;
CREATE TABLE IF NOT EXISTS `link_events_videos` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `event_id` int(100) NOT NULL,
  `game_video_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_external_games_countries`
--

DROP TABLE IF EXISTS `link_external_games_countries`;
CREATE TABLE IF NOT EXISTS `link_external_games_countries` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `external_game_id` int(100) NOT NULL,
  `country_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_franchises_games`
--

DROP TABLE IF EXISTS `link_franchises_games`;
CREATE TABLE IF NOT EXISTS `link_franchises_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `franchise_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_age_ratings`
--

DROP TABLE IF EXISTS `link_games_age_ratings`;
CREATE TABLE IF NOT EXISTS `link_games_age_ratings` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `age_rating_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_alternative_names`
--

DROP TABLE IF EXISTS `link_games_alternative_names`;
CREATE TABLE IF NOT EXISTS `link_games_alternative_names` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `alternative_name_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_artworks`
--

DROP TABLE IF EXISTS `link_games_artworks`;
CREATE TABLE IF NOT EXISTS `link_games_artworks` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `artwork_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_bundles`
--

DROP TABLE IF EXISTS `link_games_bundles`;
CREATE TABLE IF NOT EXISTS `link_games_bundles` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `bundle_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_collections`
--

DROP TABLE IF EXISTS `link_games_collections`;
CREATE TABLE IF NOT EXISTS `link_games_collections` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `collection_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_dlcs`
--

DROP TABLE IF EXISTS `link_games_dlcs`;
CREATE TABLE IF NOT EXISTS `link_games_dlcs` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `dlc_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_expanded_games`
--

DROP TABLE IF EXISTS `link_games_expanded_games`;
CREATE TABLE IF NOT EXISTS `link_games_expanded_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `expanded_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_expansions`
--

DROP TABLE IF EXISTS `link_games_expansions`;
CREATE TABLE IF NOT EXISTS `link_games_expansions` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `expansion_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_external_games`
--

DROP TABLE IF EXISTS `link_games_external_games`;
CREATE TABLE IF NOT EXISTS `link_games_external_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `external_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_forks`
--

DROP TABLE IF EXISTS `link_games_forks`;
CREATE TABLE IF NOT EXISTS `link_games_forks` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `fork_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_franchises`
--

DROP TABLE IF EXISTS `link_games_franchises`;
CREATE TABLE IF NOT EXISTS `link_games_franchises` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `franchise_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_game_engines`
--

DROP TABLE IF EXISTS `link_games_game_engines`;
CREATE TABLE IF NOT EXISTS `link_games_game_engines` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `game_engine_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_game_localizations`
--

DROP TABLE IF EXISTS `link_games_game_localizations`;
CREATE TABLE IF NOT EXISTS `link_games_game_localizations` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `game_localization_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_game_modes`
--

DROP TABLE IF EXISTS `link_games_game_modes`;
CREATE TABLE IF NOT EXISTS `link_games_game_modes` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `game_mode_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_genres`
--

DROP TABLE IF EXISTS `link_games_genres`;
CREATE TABLE IF NOT EXISTS `link_games_genres` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `genre_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_involved_companies`
--

DROP TABLE IF EXISTS `link_games_involved_companies`;
CREATE TABLE IF NOT EXISTS `link_games_involved_companies` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `involved_company_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_keywords`
--

DROP TABLE IF EXISTS `link_games_keywords`;
CREATE TABLE IF NOT EXISTS `link_games_keywords` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `keyword_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_language_supports`
--

DROP TABLE IF EXISTS `link_games_language_supports`;
CREATE TABLE IF NOT EXISTS `link_games_language_supports` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `language_support_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_multiplayer_modes`
--

DROP TABLE IF EXISTS `link_games_multiplayer_modes`;
CREATE TABLE IF NOT EXISTS `link_games_multiplayer_modes` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `multiplayer_mode_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_platforms`
--

DROP TABLE IF EXISTS `link_games_platforms`;
CREATE TABLE IF NOT EXISTS `link_games_platforms` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `platform_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_player_perspectives`
--

DROP TABLE IF EXISTS `link_games_player_perspectives`;
CREATE TABLE IF NOT EXISTS `link_games_player_perspectives` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `player_perspective_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_ports`
--

DROP TABLE IF EXISTS `link_games_ports`;
CREATE TABLE IF NOT EXISTS `link_games_ports` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `port_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_release_dates`
--

DROP TABLE IF EXISTS `link_games_release_dates`;
CREATE TABLE IF NOT EXISTS `link_games_release_dates` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `release_date_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_remakes`
--

DROP TABLE IF EXISTS `link_games_remakes`;
CREATE TABLE IF NOT EXISTS `link_games_remakes` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `remake_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_remasters`
--

DROP TABLE IF EXISTS `link_games_remasters`;
CREATE TABLE IF NOT EXISTS `link_games_remasters` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `remaster_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_screenshots`
--

DROP TABLE IF EXISTS `link_games_screenshots`;
CREATE TABLE IF NOT EXISTS `link_games_screenshots` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `screenshot_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_similar_games`
--

DROP TABLE IF EXISTS `link_games_similar_games`;
CREATE TABLE IF NOT EXISTS `link_games_similar_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `similar_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_standalone_expansions`
--

DROP TABLE IF EXISTS `link_games_standalone_expansions`;
CREATE TABLE IF NOT EXISTS `link_games_standalone_expansions` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `standalone_expansion_game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_tags`
--

DROP TABLE IF EXISTS `link_games_tags`;
CREATE TABLE IF NOT EXISTS `link_games_tags` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `tag_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_themes`
--

DROP TABLE IF EXISTS `link_games_themes`;
CREATE TABLE IF NOT EXISTS `link_games_themes` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `theme_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_videos`
--

DROP TABLE IF EXISTS `link_games_videos`;
CREATE TABLE IF NOT EXISTS `link_games_videos` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `game_video_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_games_websites`
--

DROP TABLE IF EXISTS `link_games_websites`;
CREATE TABLE IF NOT EXISTS `link_games_websites` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_id` int(100) NOT NULL,
  `website_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_game_engines_companies`
--

DROP TABLE IF EXISTS `link_game_engines_companies`;
CREATE TABLE IF NOT EXISTS `link_game_engines_companies` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_engine_id` int(100) NOT NULL,
  `company_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_game_engines_platforms`
--

DROP TABLE IF EXISTS `link_game_engines_platforms`;
CREATE TABLE IF NOT EXISTS `link_game_engines_platforms` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_engine_id` int(100) NOT NULL,
  `platform_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_game_versions_features`
--

DROP TABLE IF EXISTS `link_game_versions_features`;
CREATE TABLE IF NOT EXISTS `link_game_versions_features` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_version_id` int(100) NOT NULL,
  `feature_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_game_versions_games`
--

DROP TABLE IF EXISTS `link_game_versions_games`;
CREATE TABLE IF NOT EXISTS `link_game_versions_games` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_version_id` int(100) NOT NULL,
  `game_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_game_version_features_values`
--

DROP TABLE IF EXISTS `link_game_version_features_values`;
CREATE TABLE IF NOT EXISTS `link_game_version_features_values` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `game_version_feature_id` int(100) NOT NULL,
  `value_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_network_types_event_networks`
--

DROP TABLE IF EXISTS `link_network_types_event_networks`;
CREATE TABLE IF NOT EXISTS `link_network_types_event_networks` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `network_type_id` int(100) NOT NULL,
  `event_network_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_platforms_versions`
--

DROP TABLE IF EXISTS `link_platforms_versions`;
CREATE TABLE IF NOT EXISTS `link_platforms_versions` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `platform_id` int(100) NOT NULL,
  `version_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_platforms_versions_platform_version_release_dates`
--

DROP TABLE IF EXISTS `link_platforms_versions_platform_version_release_dates`;
CREATE TABLE IF NOT EXISTS `link_platforms_versions_platform_version_release_dates` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `platform_version_id` int(100) NOT NULL,
  `platform_version_release_date_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_platforms_websites`
--

DROP TABLE IF EXISTS `link_platforms_websites`;
CREATE TABLE IF NOT EXISTS `link_platforms_websites` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `platform_id` int(100) NOT NULL,
  `website_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `link_platform_versions_companies`
--

DROP TABLE IF EXISTS `link_platform_versions_companies`;
CREATE TABLE IF NOT EXISTS `link_platform_versions_companies` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `platform_version_id` int(100) NOT NULL,
  `company_id` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `multiplayer_modes`
--

DROP TABLE IF EXISTS `multiplayer_modes`;
CREATE TABLE IF NOT EXISTS `multiplayer_modes` (
  `id` int(100) NOT NULL,
  `campaigncoop` tinyint(3) DEFAULT NULL,
  `dropin` tinyint(3) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `lancoop` tinyint(3) DEFAULT NULL,
  `offlinecoop` tinyint(3) DEFAULT NULL,
  `offlinecoopmax` int(100) DEFAULT NULL,
  `offlinemax` int(100) DEFAULT NULL,
  `onlinecoop` tinyint(3) DEFAULT NULL,
  `onlinecoopmax` int(100) DEFAULT NULL,
  `onlinemax` int(100) DEFAULT NULL,
  `platform` int(100) DEFAULT NULL,
  `splitscreen` tinyint(3) DEFAULT NULL,
  `splitscreenonline` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `network_types`
--

DROP TABLE IF EXISTS `network_types`;
CREATE TABLE IF NOT EXISTS `network_types` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platforms`
--

DROP TABLE IF EXISTS `platforms`;
CREATE TABLE IF NOT EXISTS `platforms` (
  `id` int(100) NOT NULL,
  `abbreviation` varchar(100) DEFAULT NULL,
  `alternative_name` varchar(100) DEFAULT NULL,
  `category` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `generation` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `platform_family` int(100) DEFAULT NULL,
  `platform_logo` int(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `summary` longtext DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_families`
--

DROP TABLE IF EXISTS `platform_families`;
CREATE TABLE IF NOT EXISTS `platform_families` (
  `id` int(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_logos`
--

DROP TABLE IF EXISTS `platform_logos`;
CREATE TABLE IF NOT EXISTS `platform_logos` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_versions`
--

DROP TABLE IF EXISTS `platform_versions`;
CREATE TABLE IF NOT EXISTS `platform_versions` (
  `id` int(100) NOT NULL,
  `connectivity` varchar(1000) DEFAULT NULL,
  `cpu` varchar(1000) DEFAULT NULL,
  `graphics` varchar(1000) DEFAULT NULL,
  `main_manufacturer` int(100) DEFAULT NULL,
  `media` varchar(1000) DEFAULT NULL,
  `memory` varchar(1000) DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `os` varchar(1000) DEFAULT NULL,
  `output` varchar(1000) DEFAULT NULL,
  `platform_logo` int(100) DEFAULT NULL,
  `resolutions` varchar(1000) DEFAULT NULL,
  `slug` varchar(1000) DEFAULT NULL,
  `sound` varchar(1000) DEFAULT NULL,
  `storage` varchar(1000) DEFAULT NULL,
  `summary` longtext DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_version_companies`
--

DROP TABLE IF EXISTS `platform_version_companies`;
CREATE TABLE IF NOT EXISTS `platform_version_companies` (
  `id` int(100) NOT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `company` int(100) DEFAULT NULL,
  `developer` tinyint(3) DEFAULT NULL,
  `manufacturer` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_version_release_dates`
--

DROP TABLE IF EXISTS `platform_version_release_dates`;
CREATE TABLE IF NOT EXISTS `platform_version_release_dates` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `date` int(100) DEFAULT NULL,
  `human` varchar(100) DEFAULT NULL,
  `m` int(100) DEFAULT NULL,
  `platform_version` int(100) DEFAULT NULL,
  `region` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `y` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `platform_websites`
--

DROP TABLE IF EXISTS `platform_websites`;
CREATE TABLE IF NOT EXISTS `platform_websites` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `trusted` tinyint(3) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `player_perspectives`
--

DROP TABLE IF EXISTS `player_perspectives`;
CREATE TABLE IF NOT EXISTS `player_perspectives` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
CREATE TABLE IF NOT EXISTS `regions` (
  `id` int(100) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `identifier` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `release_dates`
--

DROP TABLE IF EXISTS `release_dates`;
CREATE TABLE IF NOT EXISTS `release_dates` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `created_at` int(100) DEFAULT NULL,
  `date` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `human` varchar(100) DEFAULT NULL,
  `m` int(100) DEFAULT NULL,
  `platform` int(100) DEFAULT NULL,
  `region` int(100) DEFAULT NULL,
  `status` int(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `y` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `release_date_statuses`
--

DROP TABLE IF EXISTS `release_date_statuses`;
CREATE TABLE IF NOT EXISTS `release_date_statuses` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `screenshots`
--

DROP TABLE IF EXISTS `screenshots`;
CREATE TABLE IF NOT EXISTS `screenshots` (
  `id` int(100) NOT NULL,
  `alpha_channel` tinyint(3) DEFAULT NULL,
  `animated` tinyint(3) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `height` int(100) DEFAULT NULL,
  `image_id` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `width` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `search`
--

DROP TABLE IF EXISTS `search`;
CREATE TABLE IF NOT EXISTS `search` (
  `id` int(100) NOT NULL,
  `alternative_name` varchar(1000) DEFAULT NULL,
  `character` int(100) DEFAULT NULL,
  `collection` int(100) DEFAULT NULL,
  `company` int(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `platform` int(100) DEFAULT NULL,
  `published_at` int(100) DEFAULT NULL,
  `test_dummy` int(100) DEFAULT NULL,
  `theme` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `themes`
--

DROP TABLE IF EXISTS `themes`;
CREATE TABLE IF NOT EXISTS `themes` (
  `id` int(100) NOT NULL,
  `created_at` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL,
  `updated_at` int(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `websites`
--

DROP TABLE IF EXISTS `websites`;
CREATE TABLE IF NOT EXISTS `websites` (
  `id` int(100) NOT NULL,
  `category` int(100) DEFAULT NULL,
  `game` int(100) DEFAULT NULL,
  `trusted` tinyint(3) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;
