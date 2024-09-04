import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
import logging
from requests import post
import linking_table_fields

conn_str = "mysql+pymysql://root:Arik2006@localhost/games_db?charset=utf8mb4"


def fetch(endpoint: str, fields: str, current_id: int) -> list:
    """
    Description: Fetches the data from the API for a specific endpoint from a specific id onwards
    Parameter: The endpoint to fetch data for
    Parameter: The fields to fetch data for
    Parameter: The id to fetch onwards from
    Return: The data returned from the API
    """
    logging.info(f"Scraping from {current_id}")
    return post(f'https://api.igdb.com/v4/{endpoint}', **{
        'headers': {'Client-ID': 'p7rq4acrchs40wa6wtlskvtkoh08y0',
                    'Authorization': 'Bearer e8zr7luprgx3bcxqgsu737l4ppi323'},
        'data': f'fields {fields}; offset {current_id}; limit 500; sort id asc;'})

endpoint_dict = {"age_ratings": "content_descriptions",
                 "characters": "akas,games",
                 "collections": "as_child_relations,as_parent_relations,games",
                 "companies": "developed,published,websites",
                 "events": "event_networks,games,videos",
                 "external_games": "countries",
                 "franchises": "games",
                 "games": "age_ratings,alternative_names,artworks,bundles,collections,dlcs,expanded_games,expansions,external_games,forks,franchises,game_engines,game_localizations,game_modes,genres,involved_companies,keywords,language_supports,multiplayer_modes,platforms,player_perspectives,ports,release_dates,remakes,remasters,screenshots,similar_games,standalone_expansions,tags,themes,videos,websites",
                 "game_engines": "companies,platforms",
                 "game_versions": "features,games",
                 "game_version_features": "values",
                 "platforms": "versions,websites",
                 "network_types": "event_networks",
                 "platform_versions": "companies,platform_version_release_dates"}


# Goes through every single endpoint field that has arrays returned and inserts them appropriately into the games database via sessions
for endpoint in endpoint_dict:
    fields = endpoint_dict[endpoint]
    current_id = 0
    response = fetch(endpoint=endpoint,fields=fields,current_id=current_id)
    while (response.json()) != []:
        engine = db.create_engine(conn_str)
        meta_data = db.MetaData()
        db.MetaData.reflect(meta_data, bind=engine)
        Session = sessionmaker(engine)
        with Session() as session:
            for dicti in (response.json()):
                id = dicti["id"]
                match endpoint:
                    case "age_ratings":
                        try:
                            try:
                                content_descriptions = dicti["content_descriptions"]
                            except:
                                content_descriptions = []
                            if content_descriptions!=[]:
                                for value in content_descriptions:
                                    age_rating_age_rating_content_description = linking_table_fields.AgeRatings_ContentDescriptions(
                                        age_rating_id=id,
                                        age_rating_content_description_id=value
                                    )
                                    session.add(instance=age_rating_age_rating_content_description)
                        except Exception as err:
                            print(f"{err} at age_ratings")
                    case "characters":
                        try:
                            try:
                                akas = dicti["akas"]
                            except:
                                akas = []
                            try:
                                games = dicti["games"]
                            except:
                                games = []
                            if akas!=[]:
                                for value in akas:
                                    character_aka = linking_table_fields.Characters_Akas(
                                        character_id=id,
                                        aka=value
                                    )
                                    session.add(instance=character_aka)
                            if games!=[]:
                                for value in games:
                                    character_game = linking_table_fields.Characters_Games(
                                        character_id=id,
                                        game_id=id
                                    )
                                    session.add(instance=character_game)
                        except Exception as err:
                            print(f"{err} at characters")
                    case "collections":
                        try:
                            try:
                                as_child_relations = dicti["as_child_relations"]
                            except:
                                as_child_relations = []
                            try:
                                as_parent_relations = dicti["as_parent_relations"]
                            except:
                                as_parent_relations = []
                            try:
                                games = dicti["games"]
                            except:
                                games = []
                            if as_child_relations!=[]:
                                for value in as_child_relations:
                                    collection_as_child_relation= linking_table_fields.Collections_AsChildRelations(
                                        collection_id=id,
                                        collection_relation_id=value
                                    )
                                    session.add(instance=collection_as_child_relation)
                            if as_parent_relations!=[]:
                                for value in as_parent_relations:
                                    collection_as_parent_relation = linking_table_fields.Collections_AsParentRelations(
                                        collection_id=id,
                                        collection_relation_id=value
                                    )
                                    session.add(instance=collection_as_parent_relation)
                            if games!=[]:
                                for value in games:
                                    collection_game = linking_table_fields.Collections_Games(
                                        collection_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=collection_game)
                        except Exception as err:
                            print(f"{err} at collections")
                    case "companies":
                        try:
                            try:
                                developed = dicti["developed"]
                            except:
                                developed = []
                            try:
                                published = dicti["published"]
                            except:
                                published = []
                            try:
                                websites = dicti["websites"]
                            except:
                                websites = []
                            if developed!=[]:
                                for value in developed:
                                    company_developed= linking_table_fields.Companies_Developed(
                                        company_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=company_developed)
                            if published!=[]:
                                for value in published:
                                    company_published = linking_table_fields.Companies_Published(
                                        company_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=company_published)
                            if websites!=[]:
                                for value in websites:
                                    company_website = linking_table_fields.Companies_Websites(
                                        company_id=id,
                                        company_website_id=value
                                    )
                                    session.add(instance=company_website)
                        except Exception as err:
                            print(f"{err} at companies")
                    case "events":
                        try:
                            try:
                                event_networks = dicti["event_networks"]
                            except:
                                event_networks = []
                            try:
                                games = dicti["games"]
                            except:
                                games = []
                            try:
                                videos = dicti["videos"]
                            except:
                                videos = []
                            if event_networks!=[]:
                                for value in event_networks:
                                    event_event_network = linking_table_fields.Events_EventNetworks(
                                        event_id=id,
                                        event_network_id=value
                                    )
                                    session.add(instance=event_event_network)
                            if games!=[]:
                                for value in games:
                                    event_game = linking_table_fields.Events_Games(
                                        event_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=event_game)
                            if videos!=[]:
                                for value in videos:
                                    event_video = linking_table_fields.Events_Videos(
                                        event_id=id,
                                        game_video_id=value
                                    )
                                    session.add(instance=event_video)
                        except Exception as err:
                            print(f"{err} at events")
                    case "external_games":
                        try:
                            try:
                                countries = dicti["countries"]
                            except:
                                countries = []
                            if countries!=[]:
                                for value in countries:
                                    external_game_country = linking_table_fields.ExternalGames_Countries(
                                        external_game_id=id,
                                        country_id=value
                                    )
                                    session.add(instance=external_game_country)
                        except Exception as err:
                            print(f"{err} at external_games")
                    case "franchises":
                        try:
                            try:
                                games = dicti["games"]
                            except:
                                games = []
                            if games!=[]:
                                for value in games:
                                    franchise_game = linking_table_fields.Franchises_Games(
                                        franchise_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=franchise_game)
                        except Exception as err:
                            print(f"{err} at franchises")
                    case "games":
                        try:
                            try:
                                age_ratings = dicti["age_ratings"]
                            except:
                                age_ratings = []
                            try:
                                alternative_names = dicti["alternative_names"]
                            except:
                                alternative_names = []
                            try:
                                artworks = dicti["artworks"]
                            except:
                                artworks = []
                            try:
                                bundles = dicti["bundles"]
                            except:
                                bundles = []
                            try:
                                collections = dicti["collections"]
                            except:
                                collections = []
                            try:
                                dlcs = dicti["dlcs"]
                            except:
                                dlcs = []
                            try:
                                expanded_games = dicti["expanded_games"]
                            except:
                                expanded_games = []
                            try:
                                expansions = dicti["expansions"]
                            except:
                                expansions = []
                            try:
                                external_games = dicti["external_games"]
                            except:
                                external_games = []
                            try:
                                forks = dicti["forks"]
                            except:
                                forks = []
                            try:
                                franchises = dicti["franchises"]
                            except:
                                franchises = []
                            try:
                                game_engines = dicti["game_engines"]
                            except:
                                game_engines = []
                            try:
                                game_localizations = dicti["game_localizations"]
                            except:
                                game_localizations = []
                            try:
                                game_modes = dicti["game_modes"]
                            except:
                                game_modes = []
                            try:
                                genres = dicti["genres"]
                            except:
                                genres = []
                            try:
                                involved_companies = dicti["involved_companies"]
                            except:
                                involved_companies = []
                            try:
                                keywords = dicti["keywords"]
                            except:
                                keywords = []
                            try:
                                language_supports = dicti["language_supports"]
                            except:
                                language_supports = []
                            try:
                                multiplayer_modes = dicti["multiplayer_modes"]
                            except:
                                multiplayer_modes = []
                            try:
                                platforms = dicti["platforms"]
                            except:
                                platforms = []
                            try:
                                player_perspectives = dicti["player_perspectives"]
                            except:
                                player_perspectives = []
                            try:
                                ports = dicti["ports"]
                            except:
                                ports = []
                            try:
                                release_dates = dicti["release_dates"]
                            except:
                                release_dates = []
                            try:
                                remakes = dicti["remakes"]
                            except:
                                remakes = []
                            try:
                                remasters = dicti["remasters"]
                            except:
                                remasters = []
                            try:
                                screenshots = dicti["screenshots"]
                            except:
                                screenshots = []
                            try:
                                similar_games = dicti["similar_games"]
                            except:
                                similar_games = []
                            try:
                                standalone_expansions = dicti["standalone_expansions"]
                            except:
                                standalone_expansions = []
                            try:
                                tags = dicti["tags"]
                            except:
                                tags = []
                            try:
                                themes = dicti["themes"]
                            except:
                                themes = []
                            try:
                                videos = dicti["videos"]
                            except:
                                videos = []
                            try:
                                websites = dicti["websites"]
                            except:
                                websites = []
                            if age_ratings!=[]:
                                for value in age_ratings:
                                    game_age_rating = linking_table_fields.Games_AgeRatings(
                                        game_id=id,
                                        age_rating_id=value
                                    )
                                    session.add(instance=game_age_rating)
                            if alternative_names!=[]:
                                for value in alternative_names:
                                    game_alternative_name = linking_table_fields.Games_AlternativeNames(
                                        game_id=id,
                                        alternative_name_id=value
                                    )
                                    session.add(instance=game_alternative_name)
                            if artworks!=[]:
                                for value in artworks:
                                    game_artwork = linking_table_fields.Games_Artworks(
                                        game_id=id,
                                        artwork_id=value
                                    )
                                    session.add(instance=game_artwork)
                            if bundles!=[]:
                                for value in bundles:
                                    game_bundle = linking_table_fields.Games_Bundles(
                                        game_id=id,
                                        bundle_game_id=value
                                    )
                                    session.add(instance=game_bundle)
                            if collections!=[]:
                                for value in collections:
                                    game_collection = linking_table_fields.Games_Collections(
                                        game_id=id,
                                        collection_id=value
                                    )
                                    session.add(instance=game_collection)
                            if dlcs!=[]:
                                for value in dlcs:
                                    game_dlc = linking_table_fields.Games_Dlcs(
                                        game_id=id,
                                        dlc_game_id=value
                                    )
                                    session.add(instance=game_dlc)
                            if expanded_games!=[]:
                                for value in expanded_games:
                                    game_expanded_game = linking_table_fields.Games_ExpandedGames(
                                        game_id=id,
                                        expanded_game_id=value
                                    )
                                    session.add(instance=game_expanded_game)
                            if expansions!=[]:
                                for value in expansions:
                                    game_expansion = linking_table_fields.Games_Expansions(
                                        game_id=id,
                                        expansion_game_id=value
                                    )
                                    session.add(instance=game_expansion)
                            if external_games!=[]:
                                for value in external_games:
                                    game_external_game = linking_table_fields.Games_ExternalGames(
                                        game_id=id,
                                        external_game_id=value
                                    )
                                    session.add(instance=game_external_game)
                            if forks!=[]:
                                for value in forks:
                                    game_fork = linking_table_fields.Games_Forks(
                                        game_id=id,
                                        fork_game_id=value
                                    )
                                    session.add(instance=game_fork)
                            if franchises!=[]:
                                for value in franchises:
                                    game_franchise = linking_table_fields.Games_Franchises(
                                        game_id=id,
                                        franchise_id=value
                                    )
                                    session.add(instance=game_franchise)
                            if game_engines!=[]:
                                for value in game_engines:
                                    game_game_engine = linking_table_fields.Games_GameEngines(
                                        game_id=id,
                                        game_engine_id=value
                                    )
                                    session.add(instance=game_game_engine)
                            if game_localizations!=[]:
                                for value in game_localizations:
                                    game_game_localization = linking_table_fields.Games_GameLocalizations(
                                        game_id=id,
                                        game_localization_id=value
                                    )
                                    session.add(instance=game_game_localization)
                            if game_modes!=[]:
                                for value in game_modes:
                                    game_game_mode = linking_table_fields.Games_GameModes(
                                        game_id=id,
                                        game_mode_id=value
                                    )
                                    session.add(instance=game_game_mode)
                            if genres!=[]:
                                for value in genres:
                                    game_genre = linking_table_fields.Games_Genres(
                                        game_id=id,
                                        genre_id=value
                                    )
                                    session.add(instance=game_genre)
                            if involved_companies!=[]:
                                for value in involved_companies:
                                    game_involved_company = linking_table_fields.Games_InvolvedCompanies(
                                        game_id=id,
                                        involved_company_id=value
                                    )
                                    session.add(instance=game_involved_company)
                            if keywords!=[]:
                                for value in keywords:
                                    game_keyword = linking_table_fields.Games_Keywords(
                                        game_id=id,
                                        keyword_id=value
                                    )
                                    session.add(instance=game_keyword)
                            if language_supports!=[]:
                                for value in language_supports:
                                    game_language_support = linking_table_fields.Games_LanguageSupports(
                                        game_id=id,
                                        language_support_id=value
                                    )
                                    session.add(instance=game_language_support)
                            if multiplayer_modes!=[]:
                                for value in multiplayer_modes:
                                    game_multiplayer_mode = linking_table_fields.Games_MultiplayerModes(
                                        game_id=id,
                                        multiplayer_mode_id=value
                                    )
                                    session.add(instance=game_multiplayer_mode)
                            if platforms!=[]:
                                for value in platforms:
                                    game_platform = linking_table_fields.Games_Platforms(
                                        game_id=id,
                                        platform_id=value
                                    )
                                    session.add(instance=game_platform)
                            if player_perspectives!=[]:
                                for value in player_perspectives:
                                    game_player_perspective = linking_table_fields.Games_PlayerPerspectives(
                                        game_id=id,
                                        player_perspective_id=value
                                    )
                                    session.add(instance=game_player_perspective)
                            if ports!=[]:
                                for value in ports:
                                    game_port = linking_table_fields.Games_Ports(
                                        game_id=id,
                                        port_game_id=value
                                    )
                                    session.add(instance=game_port)
                            if release_dates!=[]:
                                for value in release_dates:
                                    game_release_date = linking_table_fields.Games_ReleaseDates(
                                        game_id=id,
                                        release_date_id=value
                                    )
                                    session.add(instance=game_release_date)
                            if remakes!=[]:
                                for value in remakes:
                                    game_remake = linking_table_fields.Games_Remakes(
                                        game_id=id,
                                        remake_game_id=value
                                    )
                                    session.add(instance=game_remake)
                            if remasters!=[]:
                                for value in remasters:
                                    game_remaster = linking_table_fields.Games_Remasters(
                                        game_id=id,
                                        remaster_game_id=value
                                    )
                                    session.add(instance=game_remaster)
                            if screenshots!=[]:
                                for value in screenshots:
                                    game_screenshot = linking_table_fields.Games_Screenshots(
                                        game_id=id,
                                        screenshot_id=value
                                    )
                                    session.add(instance=game_screenshot)
                            if similar_games!=[]:
                                for value in similar_games:
                                    game_similar_game = linking_table_fields.Games_SimilarGames(
                                        game_id=id,
                                        similar_game_id=value
                                    )
                                    session.add(instance=game_similar_game)
                            if standalone_expansions!=[]:
                                for value in standalone_expansions:
                                    game_standalone_expansion = linking_table_fields.Games_StandaloneExpansions(
                                        game_id=id,
                                        standalone_expansion_game_id=value
                                    )
                                    session.add(instance=game_standalone_expansion)
                            if tags!=[]:
                                for value in tags:
                                    game_tag = linking_table_fields.Games_Tags(
                                        game_id=id,
                                        tag_id=value
                                    )
                                    session.add(instance=game_tag)
                            if themes!=[]:
                                for value in themes:
                                    game_theme = linking_table_fields.Games_Themes(
                                        game_id=id,
                                        theme_id=value
                                    )
                                    session.add(instance=game_theme)
                            if videos!=[]:
                                for value in videos:
                                    game_video = linking_table_fields.Games_Videos(
                                        game_id=id,
                                        game_video_id=value
                                    )
                                    session.add(instance=game_video)
                            if websites!=[]:
                                for value in websites:
                                    game_website = linking_table_fields.Games_Websites(
                                        game_id=id,
                                        website_id=value
                                    )
                                    session.add(instance=game_website)
                        except Exception as err:
                            print(f"{err} at games")
                    case "game_engines":
                        try:
                            try:
                                companies = dicti["companies"]
                            except:
                                companies = []
                            try:
                                platforms = dicti["platforms"]
                            except:
                                platforms = []
                            if companies!=[]:
                                for value in companies:
                                    game_engine_company = linking_table_fields.GameEngines_Companies(
                                        game_engine_id=id,
                                        company_id=value
                                    )
                                    session.add(instance=game_engine_company)
                            if platforms!=[]:
                                for value in platforms:
                                    game_engine_platform = linking_table_fields.GameEngines_Platforms(
                                        game_engine_id=id,
                                        platform_id=value
                                    )
                                    session.add(instance=game_engine_platform)
                        except Exception as err:
                            print(f"{err} at game_engines")
                    case "game_versions":
                        try:
                            try:
                                features = dicti["features"]
                            except:
                                features = []
                            try:
                                games = dicti["games"]
                            except:
                                games = []
                            if features!=[]:
                                for value in features:
                                    game_version_feature = linking_table_fields.GameVersions_Features(
                                        game_version_id=id,
                                        feature_id=value
                                    )
                                    session.add(instance=game_version_feature)
                            if games!=[]:
                                for value in games:
                                    game_version_game = linking_table_fields.GameVersions_Games(
                                        game_version_id=id,
                                        game_id=value
                                    )
                                    session.add(instance=game_version_game)
                        except Exception as err:
                            print(f"{err} at game_versions")
                    case "game_version_features":
                        try:
                            try:
                                values = dicti["values"]
                            except:
                                values = []
                            if values!=[]:
                                for value in values:
                                    game_version_feature_value = linking_table_fields.GameVersionFeatures_Values(
                                        game_version_feature_id=id,
                                        value_id=value
                                    )
                                    session.add(instance=game_version_feature_value)
                        except Exception as err:
                            print(f"{err} at game_version_features")
                    case "platforms":
                        try:
                            try:
                                versions = dicti["versions"]
                            except:
                                versions = []
                            try:
                                websites = dicti["websites"]
                            except:
                                websites = []
                            if versions!=[]:
                                for value in versions:
                                    platform_version = linking_table_fields.Platforms_Versions(
                                        platform_id=id,
                                        version_id=value
                                    )
                                    session.add(instance=platform_version)
                            if websites!=[]:
                                for value in websites:
                                    platform_website = linking_table_fields.Platforms_Websites(
                                        platform_id=id,
                                        website_id=value
                                    )
                                    session.add(instance=platform_website)
                        except Exception as err:
                            print(f"{err} at platforms")
                    case "network_types":
                        try:
                            try:
                                event_networks = dicti["event_networks"]
                            except:
                                event_networks = []
                            if event_networks!=[]:
                                for value in event_networks:
                                    network_type_event_network = linking_table_fields.NetworkTypes_EventNetworks(
                                        network_type_id=id,
                                        event_network_id=value
                                    )
                                    session.add(instance=network_type_event_network)
                        except Exception as err:
                            print(f"{err} at network_types")
                    case "platform_versions":
                        try:
                            try:
                                companies = dicti["companies"]
                            except:
                                companies = []
                            try:
                                platform_version_release_dates = dicti["platform_version_release_dates"]
                            except:
                                platform_version_release_dates = []
                            if companies!=[]:
                                for value in companies:
                                    platform_version_company = linking_table_fields.PlatformVersions_Companies(
                                        platform_version_id=id,
                                        company_id=value
                                    )
                                    session.add(instance=platform_version_company)
                            if platform_version_release_dates!=[]:
                                for value in platform_version_release_dates:
                                    platform_version_platform_version_release_date = linking_table_fields.PlatformVersions_PlatFormVersionReleaseDates(
                                        platform_version_id=id,
                                        platform_version_release_date_id=value
                                    )
                                    session.add(instance=platform_version_platform_version_release_date)
                        except Exception as err:
                            print(f"{err} at platform_versions")
            session.commit()
            logging.info(f"Added from {current_id} to {dicti['id']}")
            current_id = dicti['id']
            response = (fetch(endpoint, fields, current_id))