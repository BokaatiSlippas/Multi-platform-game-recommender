from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session

class Base(DeclarativeBase):
    pass

# These are the class templates for each of the endpoints from the API that return arrays
class AgeRatings_ContentDescriptions(Base):
    __tablename__ = "link_age_ratings_content_descriptions"
    id: Mapped[int] = mapped_column(primary_key=True)
    age_rating_id: Mapped[int]
    age_rating_content_description_id: Mapped[int]


class Characters_Akas(Base):
    __tablename__ = "link_characters_akas"
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int]
    aka: Mapped[str]


class Characters_Games(Base):
    __tablename__ = "link_characters_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int]
    game_id: Mapped[int]


class Collections_AsChildRelations(Base):
    __tablename__ = "link_collections_as_child_relations"
    id: Mapped[int] = mapped_column(primary_key=True)
    collection_id: Mapped[int]
    collection_relation_id: Mapped[int] # as_child_relations is array of collection relation id


class Collections_AsParentRelations(Base):
    __tablename__ = "link_collections_as_parent_relations"
    id: Mapped[int] = mapped_column(primary_key=True)
    collection_id: Mapped[int]
    collection_relation_id: Mapped[int] # as_child_relations is array of collection relation id


class Collections_Games(Base):
    __tablename__ = "link_collections_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    collection_id: Mapped[int]
    game_id: Mapped[int]


class Companies_Developed(Base):
    __tablename__ = "link_companies_developed"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int]
    game_id: Mapped[int] # Developed is array of games id


class Companies_Published(Base):
    __tablename__ = "link_companies_published"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int]
    game_id: Mapped[int] # Published is array of games id


class Companies_Websites(Base):
    __tablename__ = "link_companies_websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int]
    company_website_id: Mapped[int] # Websites is array of company websites


class Events_EventNetworks(Base):
    __tablename__ = "link_events_event_networks"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int]
    event_network_id: Mapped[int]


class Events_Games(Base):
    __tablename__ = "link_events_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int]
    game_id: Mapped[int]


class Events_Videos(Base):
    __tablename__ = "link_events_videos"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int]
    game_video_id: Mapped[int]


class ExternalGames_Countries(Base):
    __tablename__ = "link_external_games_countries"
    id: Mapped[int] = mapped_column(primary_key=True)
    external_game_id: Mapped[int]
    country_id: Mapped[int]


class Franchises_Games(Base):
    __tablename__ = "link_franchises_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    franchise_id: Mapped[int]
    game_id: Mapped[int]


class Games_AgeRatings(Base):
    __tablename__ = "link_games_age_ratings"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    age_rating_id: Mapped[int]


class Games_AlternativeNames(Base):
    __tablename__ = "link_games_alternative_names"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    alternative_name_id: Mapped[int]


class Games_Artworks(Base):
    __tablename__ = "link_games_artworks"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    artwork_id: Mapped[int]


class Games_Bundles(Base):
    __tablename__ = "link_games_bundles"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    bundle_game_id: Mapped[int] # Bundles is array of games ids


class Games_Collections(Base):
    __tablename__ = "link_games_collections"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    collection_id: Mapped[int] # Bundles is array of games ids


class Games_Dlcs(Base):
    __tablename__ = "link_games_dlcs"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    dlc_game_id: Mapped[int] # dlcs is array of games ids


class Games_ExpandedGames(Base):
    __tablename__ = "link_games_expanded_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    expanded_game_id: Mapped[int] # expanded games is array of games ids


class Games_Expansions(Base):
    __tablename__ = "link_games_expansions"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    expansion_game_id: Mapped[int] # Expansions is array of games ids


class Games_ExternalGames(Base):
    __tablename__ = "link_games_external_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    external_game_id: Mapped[int] # external games is array of games ids


class Games_Forks(Base):
    __tablename__ = "link_games_forks"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    fork_game_id: Mapped[int] # forks is array of games ids


class Games_Franchises(Base):
    __tablename__ = "link_games_franchises"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    franchise_id: Mapped[int]


class Games_GameEngines(Base):
    __tablename__ = "link_games_game_engines"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    game_engine_id: Mapped[int]


class Games_GameLocalizations(Base):
    __tablename__ = "link_games_game_localizations"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    game_localization_id: Mapped[int]


class Games_GameModes(Base):
    __tablename__ = "link_games_game_modes"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    game_mode_id: Mapped[int]


class Games_Genres(Base):
    __tablename__ = "link_games_genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    genre_id: Mapped[int]


class Games_InvolvedCompanies(Base):
    __tablename__ = "link_games_involved_companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    involved_company_id: Mapped[int]


class Games_Keywords(Base):
    __tablename__ = "link_games_keywords"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    keyword_id: Mapped[int]


class Games_LanguageSupports(Base):
    __tablename__ = "link_games_language_supports"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    language_support_id: Mapped[int]


class Games_MultiplayerModes(Base):
    __tablename__ = "link_games_multiplayer_modes"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    multiplayer_mode_id: Mapped[int]


class Games_Platforms(Base):
    __tablename__ = "link_games_platforms"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    platform_id: Mapped[int]


class Games_PlayerPerspectives(Base):
    __tablename__ = "link_games_player_perspectives"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    player_perspective_id: Mapped[int]


class Games_Ports(Base):
    __tablename__ = "link_games_ports"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    port_game_id: Mapped[int] # ports is array of games ids


class Games_ReleaseDates(Base):
    __tablename__ = "link_games_release_dates"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    release_date_id: Mapped[int]


class Games_Remakes(Base):
    __tablename__ = "link_games_remakes"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    remake_game_id: Mapped[int] # remakes is array of games ids


class Games_Remasters(Base):
    __tablename__ = "link_games_remasters"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    remaster_game_id: Mapped[int] # remasters is array of games ids


class Games_Screenshots(Base):
    __tablename__ = "link_games_screenshots"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    screenshot_id: Mapped[int]


class Games_SimilarGames(Base):
    __tablename__ = "link_games_similar_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    similar_game_id: Mapped[int] # similar games is array of games ids


class Games_StandaloneExpansions(Base):
    __tablename__ = "link_games_standalone_expansions"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    standalone_expansion_game_id: Mapped[int] # standalone expansions is array of games ids


class Games_Tags(Base):
    __tablename__ = "link_games_tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    tag_id: Mapped[int]


class Games_Themes(Base):
    __tablename__ = "link_games_themes"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    theme_id: Mapped[int]


class Games_Videos(Base):
    __tablename__ = "link_games_videos"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    game_video_id: Mapped[int]


class Games_Websites(Base):
    __tablename__ = "link_games_websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    website_id: Mapped[int]


class GameEngines_Companies(Base):
    __tablename__ = "link_game_engines_companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_engine_id: Mapped[int]
    company_id: Mapped[int]


class GameEngines_Platforms(Base):
    __tablename__ = "link_game_engines_platforms"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_engine_id: Mapped[int]
    platform_id: Mapped[int]


class GameVersions_Features(Base):
    __tablename__ = "link_game_versions_features"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_version_id: Mapped[int]
    feature_id: Mapped[int]


class GameVersions_Games(Base):
    __tablename__ = "link_game_versions_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_version_id: Mapped[int]
    game_id: Mapped[int]


class GameVersionFeatures_Values(Base):
    __tablename__ = "link_game_version_features_values"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_version_feature_id: Mapped[int]
    value_id: Mapped[int]


class Platforms_Versions(Base):
    __tablename__ = "link_platforms_versions"
    id: Mapped[int] = mapped_column(primary_key=True)
    platform_id: Mapped[int]
    version_id: Mapped[int]


class Platforms_Websites(Base):
    __tablename__ = "link_platforms_websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    platform_id: Mapped[int]
    website_id: Mapped[int]


class NetworkTypes_EventNetworks(Base):
    __tablename__ = "link_network_types_event_networks"
    id: Mapped[int] = mapped_column(primary_key=True)
    network_type_id: Mapped[int]
    event_network_id: Mapped[int]


class PlatformVersions_Companies(Base):
    __tablename__ = "link_platform_versions_companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    platform_version_id: Mapped[int]
    company_id: Mapped[int]


class PlatformVersions_PlatFormVersionReleaseDates(Base):
    __tablename__ = "link_platforms_versions_platform_version_release_dates"
    id: Mapped[int] = mapped_column(primary_key=True)
    platform_version_id: Mapped[int]
    platform_version_release_date_id: Mapped[int]