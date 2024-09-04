from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session

class Base(DeclarativeBase):
    pass

# These are the class templates for each of the endpoints from the API that do not return arrays
class AgeRating(Base):
    __tablename__ = "age_ratings"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    rating: Mapped[int]
    rating_cover_url: Mapped[str]
    synopsis: Mapped[str]


class AgeRatingContentDescription(Base):
    __tablename__ = "age_rating_content_descriptions"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    description: Mapped[str]


class AlternativeName(Base):
    __tablename__ = "alternative_names"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]
    game: Mapped[int]
    name: Mapped[str]


class Artwork(Base):
    __tablename__ = "artworks"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    game: Mapped[int]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class Character(Base):
            
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    country_name: Mapped[str]
    created_at: Mapped[int]
    description: Mapped[str]
    gender: Mapped[int]
    mug_shot: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    species: Mapped[int]
    updated_at: Mapped[int]
    url: Mapped[str]


class CharacterMugShot(Base):
            
    __tablename__ = "character_mug_shots"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class Collection(Base):
            
    __tablename__ = "collections"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class CollectionMembership(Base):
            
    __tablename__ = "collection_memberships"
    id: Mapped[int] = mapped_column(primary_key=True)
    collection: Mapped[int]
    created_at: Mapped[int]
    game: Mapped[int]
    type: Mapped[int]
    updated_at: Mapped[int]


class CollectionMembershipType(Base):
            
    __tablename__ = "collection_membership_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    allowed_collection_type: Mapped[int]
    created_at: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    updated_at: Mapped[int]


class CollectionRelation(Base):
            
    __tablename__ = "collection_relations"
    id: Mapped[int] = mapped_column(primary_key=True)
    child_collection: Mapped[int]
    created_at: Mapped[int]
    parent_collection: Mapped[int]
    type: Mapped[int]
    updated_at: Mapped[int]


class CollectionRelationType(Base):
            
    __tablename__ = "collection_relation_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    allowed_child_type: Mapped[int]
    allowed_parent_type: Mapped[int]
    created_at: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    updated_at: Mapped[int]


class CollectionType(Base):
            
    __tablename__ = "collection_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    updated_at: Mapped[int]


class Company(Base):
            
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    change_date: Mapped[int]
    change_date_category: Mapped[int]
    changed_company_id: Mapped[int]
    country: Mapped[int]
    created_at: Mapped[int]
    description: Mapped[str]
    logo: Mapped[int]
    name: Mapped[str]
    parent: Mapped[int]
    slug: Mapped[str]
    start_date: Mapped[int]
    start_date_category: Mapped[int]
    updated_at: Mapped[int]
    url: Mapped[str]


class CompanyLogo(Base):
            
    __tablename__ = "company_logos"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class CompanyWebsite(Base):
            
    __tablename__ = "company_websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    trusted: Mapped[bool]
    url: Mapped[str]


class Cover(Base):
            
    __tablename__ = "covers"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    game: Mapped[int]
    game_localization: Mapped[int]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class Event(Base):
            
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    description: Mapped[str]
    end_time: Mapped[int]
    event_logo: Mapped[int]
    live_stream_url: Mapped[str]
    name: Mapped[str]
    slug: Mapped[str]
    start_time: Mapped[int]
    time_zone: Mapped[str]
    updated_at: Mapped[int]


class EventLogo(Base):
            
    __tablename__ = "event_logos"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    created_at: Mapped[int]
    event: Mapped[int]
    height: Mapped[int]
    image_id: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]
    width: Mapped[int]


class EventNetwork(Base):
            
    __tablename__ = "event_networks"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    event: Mapped[int]
    network_type: Mapped[int]
    updated_at: Mapped[int]
    url: Mapped[str]


class ExternalGame(Base):
            
    __tablename__ = "external_games"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    created_at: Mapped[int]
    game: Mapped[int]
    media: Mapped[int]
    name: Mapped[str]
    platform: Mapped[int]
    uid: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]
    year: Mapped[int]


class Franchise(Base):
            
    __tablename__ = "franchises"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]



class Game(Base):
            
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)
    aggregated_rating: Mapped[float]
    aggregated_rating_count: Mapped[int]
    category: Mapped[int]
    collection: Mapped[int]
    cover: Mapped[int]
    created_at: Mapped[int]
    first_release_date: Mapped[int]
    follows: Mapped[int]
    franchise: Mapped[int]
    hypes: Mapped[int]
    name: Mapped[str]
    parent_game: Mapped[int]
    rating: Mapped[float]
    rating_count: Mapped[int]
    slug: Mapped[str]
    status: Mapped[int]
    storyline: Mapped[str]
    summary: Mapped[str]
    total_rating: Mapped[float]
    total_rating_count: Mapped[int]
    updated_at: Mapped[int]
    url: Mapped[str]
    version_parent: Mapped[int]
    version_title: Mapped[str]


class GameEngine(Base):
            
    __tablename__ = "game_engines"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    description: Mapped[str]
    logo: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class GameEngineLogo(Base):
            
    __tablename__ = "game_engine_logos"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class GameLocalization(Base):
            
    __tablename__ = "game_localizations"
    id: Mapped[int] = mapped_column(primary_key=True)
    cover: Mapped[int]
    created_at: Mapped[int]
    game: Mapped[int]
    name: Mapped[str]
    region: Mapped[int]
    updated_at: Mapped[int]


class GameMode(Base):
            
    __tablename__ = "game_modes"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class GameVersion(Base):
            
    __tablename__ = "game_versions"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    game: Mapped[int]
    updated_at: Mapped[int]
    url: Mapped[str]


class GameVersionFeature(Base):
            
    __tablename__ = "game_version_features"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    description: Mapped[str]
    position: Mapped[int]
    title: Mapped[str]


class GameVersionFeatureValue(Base):
            
    __tablename__ = "game_version_feature_values"
    id: Mapped[int] = mapped_column(primary_key=True)
    game: Mapped[int]
    game_feature: Mapped[int]
    included_feature: Mapped[int]
    note: Mapped[str]


class GameVideo(Base):
            
    __tablename__ = "game_videos"
    id: Mapped[int] = mapped_column(primary_key=True)
    game: Mapped[int]
    name: Mapped[str]
    video_id: Mapped[str]


class Genre(Base):
            
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class InvolvedCompany(Base):
            
    __tablename__ = "involved_companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    company: Mapped[int]
    created_at: Mapped[int]
    developer: Mapped[bool]
    game: Mapped[int]
    porting: Mapped[bool]
    publisher: Mapped[bool]
    supporting: Mapped[bool]
    updated_at: Mapped[int]


class Keyword(Base):
            
    __tablename__ = "keywords"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class Language(Base):
            
    __tablename__ = "languages"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    locale: Mapped[str]
    name: Mapped[str]
    native_name: Mapped[str]
    updated_at: Mapped[int]


class LanguageSupport(Base):
            
    __tablename__ = "language_supports"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    game: Mapped[int]
    language: Mapped[int]
    language_support_type: Mapped[int]
    updated_at: Mapped[int]


class MultiplayerMode(Base):
            
    __tablename__ = "multiplayer_modes"
    id: Mapped[int] = mapped_column(primary_key=True)
    campaigncoop: Mapped[bool]
    dropin: Mapped[bool]
    game: Mapped[int]
    lancoop: Mapped[bool]
    offlinecoop: Mapped[bool]
    offlinecoopmax: Mapped[int]
    offlinemax: Mapped[int]
    onlinecoop: Mapped[bool]
    onlinecoopmax: Mapped[int]
    onlinemax: Mapped[int]
    platform: Mapped[int]
    splitscreen: Mapped[bool]
    splitscreenonline: Mapped[bool]



class Platform(Base):
            
    __tablename__ = "platforms"
    id: Mapped[int] = mapped_column(primary_key=True)
    abbreviation: Mapped[str]
    alternative_name: Mapped[str]
    category: Mapped[int]
    created_at: Mapped[int]
    generation: Mapped[int]
    name: Mapped[str]
    platform_family: Mapped[int]
    platform_logo: Mapped[int]
    slug: Mapped[str]
    summary: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class LanguageSupportType(Base):
            
    __tablename__ = "language_support_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    updated_at: Mapped[int]


class PlatformFamily(Base):
            
    __tablename__ = "platform_families"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    slug: Mapped[str]


class NetworkType(Base):
            
    __tablename__ = "network_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    updated_at: Mapped[int]


class PlatformLogo(Base):
            
    __tablename__ = "platform_logos"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class PlatformVersionCompany(Base):
            
    __tablename__ = "platform_version_companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]
    company: Mapped[int]
    developer: Mapped[bool]
    manufacturer: Mapped[bool]


class PlatformVersion(Base):
            
    __tablename__ = "platform_versions"
    id: Mapped[int] = mapped_column(primary_key=True)
    connectivity: Mapped[str]
    cpu: Mapped[str]
    graphics: Mapped[str]
    main_manufacturer: Mapped[int]
    media: Mapped[str]
    memory: Mapped[str]
    name: Mapped[str]
    os: Mapped[str]
    output: Mapped[str]
    platform_logo: Mapped[int]
    resolutions: Mapped[str]
    slug: Mapped[str]
    sound: Mapped[str]
    storage: Mapped[str]
    summary: Mapped[str]
    url: Mapped[str]


class PlatformWebsite(Base):
            
    __tablename__ = "platform_websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    trusted: Mapped[bool]
    url: Mapped[str]


class PlatformVersionReleaseDate(Base):
            
    __tablename__ = "platform_version_release_dates"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    created_at: Mapped[int]
    date: Mapped[int]
    human: Mapped[str]
    m: Mapped[int]
    platform_version: Mapped[int]
    region: Mapped[int]
    updated_at: Mapped[int]
    y: Mapped[int]


class PlayerPerspective(Base):
            
    __tablename__ = "player_perspectives"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]


class Region(Base):
            
    __tablename__ = "regions"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str]
    created_at: Mapped[int]
    identifier: Mapped[str]
    name: Mapped[str]
    updated_at: Mapped[int]


class ReleaseDate(Base):
            
    __tablename__ = "release_dates"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    created_at: Mapped[int]
    date: Mapped[int]
    game: Mapped[int]
    human: Mapped[str]
    m: Mapped[int]
    platform: Mapped[int]
    region: Mapped[int]
    status: Mapped[int]
    updated_at: Mapped[int]
    y: Mapped[int]


class ReleaseDateStatus(Base):
            
    __tablename__ = "release_date_statuses"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    updated_at: Mapped[int]


class Screenshot(Base):
            
    __tablename__ = "screenshots"
    id: Mapped[int] = mapped_column(primary_key=True)
    alpha_channel: Mapped[bool]
    animated: Mapped[bool]
    game: Mapped[int]
    height: Mapped[int]
    image_id: Mapped[str]
    url: Mapped[str]
    width: Mapped[int]


class Search(Base):
            
    __tablename__ = "search"
    id: Mapped[int] = mapped_column(primary_key=True)
    alternative_name: Mapped[str]
    character: Mapped[int]
    collection: Mapped[int]
    company: Mapped[int]
    description: Mapped[str]
    game: Mapped[int]
    name: Mapped[str]
    platform: Mapped[int]
    published_at: Mapped[int]
    test_dummy: Mapped[int]
    theme: Mapped[int]


class Website(Base):
            
    __tablename__ = "websites"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    game: Mapped[int]
    trusted: Mapped[bool]
    url: Mapped[str]


class Theme(Base):
            
    __tablename__ = "themes"
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[int]
    name: Mapped[str]
    slug: Mapped[str]
    updated_at: Mapped[int]
    url: Mapped[str]