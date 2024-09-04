import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
import logging
from requests import post
import table_fields

conn_str = "mysql+pymysql://root:@localhost/games_db?charset=utf8mb4"


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
                    'Authorization': 'Bearer xraxecs24z2qdvp7rbk4iz3635cj3z'},
        'data': f'fields {fields}; offset {current_id}; limit 500; sort id asc;'})


endpoint_dict = {"age_ratings": "category,checksum,content_descriptions,rating,rating_cover_url",
                 "age_rating_content_descriptions": "category,checksum,description",
                 "alternative_names": "checksum,comment,game,name",
                 "artworks": "alpha_channel,animated,checksum,game,height,image_id,url,width",
                 "characters": "akas,checksum,country_name,created_at,description,games,gender,mug_shot,name,slug,species,updated_at,url",
                 "character_mug_shots": "alpha_channel,animated,checksum,height,image_id,url,width",
                 "collections": "checksum,created_at,games,name,slug,updated_at,url",
                 "collection_memberships": "checksum,collection,created_at,game,type,updated_at",
                 "collection_membership_types": "allowed_collection_type,checksum,created_at,description,name,updated_at",
                 "collection_relations": "checksum,child_collection,created_at,parent_collection,type,updated_at",
                 "collection_relation_types": "allowed_child_type,allowed_parent_type,checksum,created_at,description,name,updated_at",
                 "collection_types": "checksum,created_at,description,name,updated_at",
                 "companies": "change_date,change_date_category,changed_company_id,checksum,country,created_at,description,developed,logo,name,parent,published,slug,start_date,start_date_category,updated_at,url,websites",
                 "company_logos": "alpha_channel,animated,checksum,height,image_id,url,width",
                 "company_websites": "category,checksum,trusted,url",
                 "covers": "alpha_channel,animated,checksum,game,game_localization,height,image_id,url,width",
                 "events": "checksum,created_at,description,end_time,event_logo,event_networks,games,live_stream_url,name,slug,start_time,time_zone,updated_at,videos",
                 "event_logos": "alpha_channel,animated,checksum,created_at,event,height,image_id,updated_at,url,width",
                 "event_networks": "checksum,created_at,event,network_type,updated_at,url",
                 "external_games": "category,checksum,countries,created_at,game,media,name,platform,uid,updated_at,url,year",
                 "franchises": "checksum,created_at,games,name,slug,updated_at,url",
                 "games": "age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchise,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites",
                 "game_engines": "checksum,companies,created_at,description,logo,name,platforms,slug,updated_at,url",
                 "game_engine_logos": "alpha_channel,animated,checksum,height,image_id,url,width",
                 "game_localizations": "checksum,cover,created_at,game,name,region,updated_at",
                 "game_modes": "checksum,created_at,name,slug,updated_at,url",
                 "game_versions": "checksum,created_at,features,game,games,updated_at,url",
                 "game_version_features": "category,checksum,description,position,title,values",
                 "game_version_feature_values": "checksum,game,game_feature,included_feature,note",
                 "game_videos": "checksum,game,name,video_id",
                 "genres": "checksum,created_at,name,slug,updated_at,url",
                 "involved_companies": "checksum,company,created_at,developer,game,porting,publisher,supporting,updated_at",
                 "keywords": "checksum,created_at,name,slug,updated_at,url",
                 "languages": "checksum,created_at,locale,name,native_name,updated_at",
                 "language_supports": "checksum,created_at,game,language,language_support_type,updated_at",
                 "multiplayer_modes": "campaigncoop,checksum,dropin,game,lancoop,offlinecoop,offlinecoopmax,offlinemax,onlinecoop,onlinecoopmax,onlinemax,platform,splitscreen,splitscreenonline",
                 "platforms": "abbreviation,alternative_name,category,checksum,created_at,generation,name,platform_family,platform_logo,slug,summary,updated_at,url,versions,websites",
                 "language_support_types": "checksum,created_at,name,updated_at",
                 "platform_families": "checksum,name,slug",
                 "network_types": "checksum,created_at,event_networks,name,updated_at",
                 "platform_logos": "alpha_channel,animated,checksum,height,image_id,url,width",
                 "platform_version_companies": " checksum,comment,company,developer,manufacturer",
                 "platform_versions": "checksum,companies,connectivity,cpu,graphics,main_manufacturer,media,memory,name,online,os,output,platform_logo,platform_version_release_dates,resolutions,slug,sound,storage,summary,url",
                 "platform_websites": "category,checksum,trusted,url",
                 "platform_version_release_dates": "category,checksum,created_at,date,human,m,platform_version,region,updated_at,y",
                 "player_perspectives": "checksum,created_at,name,slug,updated_at,url",
                 "regions": "category,checksum,created_at,identifier,name,updated_at",
                 "release_dates": "category,checksum,created_at,date,game,human,m,platform,region,status,updated_at,y",
                 "release_date_statuses": "checksum,created_at,description,name,updated_at",
                 "screenshots": "alpha_channel,animated,checksum,game,height,image_id,url,width",
                 "search": "alternative_name,character,checksum,collection,company,description,game,name,platform,published_at,test_dummy,theme",
                 "themes": "checksum,created_at,name,slug,updated_at,url",
                 "websites": "category,checksum,game,trusted,url"}


# Goes through every endpoint field that has no arrays returned and inserts the data into the games database via sessions
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
                            category = dicti["category"]
                        except:
                            category = None
                        #try:
                        #    content_descriptions = dicti["content_descriptions"]
                        #except:
                        #    content_descriptions = None
                        try:
                            rating = dicti["rating"]
                        except:
                            rating = None
                        try:
                            rating_cover_url = dicti["rating_cover_url"]
                        except:
                            rating_cover_url = None
                        try:
                            synopsis = dicti["synopsis"]
                        except:
                            synopsis = None
                        instance = session.query(table_fields.AgeRating).filter_by(id=id).first()
                        if not instance:
                            age_rating = table_fields.AgeRating(
                                id=id,
                                category=category,
                                rating=rating,
                                rating_cover_url=rating_cover_url,
                                synopsis=synopsis
                            )
                            session.add(instance=age_rating)
                    case "age_rating_content_descriptions":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        instance = session.query(table_fields.AgeRatingContentDescription).filter_by(id=id).first()
                        if not instance:
                            age_rating_content_description = table_fields.AgeRatingContentDescription(
                                id=id,
                                category=category,
                                description=description
                            )
                            session.add(instance=age_rating_content_description)
                    case "alternative_names":
                        try:
                            comment = dicti["comment"]
                        except:
                            comment = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        instance = session.query(table_fields.AlternativeName).filter_by(id=id).first()
                        if not instance:
                            alternative_name = table_fields.AlternativeName(
                                id=id,
                                comment=comment,
                                game=game,
                                name=name
                            )
                            session.add(instance=alternative_name)
                    case "artworks":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.Artwork).filter_by(id=id).first()
                        if not instance:
                            artwork = table_fields.Artwork(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                game=game,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=artwork)
                    case "characters":
                        #try:
                        #    akas = dicti["akas"]
                        #except:
                        #    akas = None
                        try:
                            country_name = dicti["country_name"]
                        except:
                            country_name = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        #try:
                        #    games = dicti["games"]
                        #except:
                        #    games = None
                        try:
                            gender = dicti["gender"]
                        except:
                            gender = None
                        try:
                            mug_shot = dicti["mug_shot"]
                        except:
                            mug_shot = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            species = dicti["species"]
                        except:
                            species = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Character).filter_by(id=id).first()
                        if not instance:
                            character = table_fields.Character(
                                id=id,
                                country_name=country_name,
                                created_at=created_at,
                                description=description,
                                gender=gender,
                                mug_shot=mug_shot,
                                name=name,
                                slug=slug,
                                species=species,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=character)
                    case "character_mug_shots":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.CharacterMugShot).filter_by(id=id).first()
                        if not instance:
                            character_mug_shot = table_fields.CharacterMugShot(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=character_mug_shot)
                    case "collections":
    #                   try:
    #                       as_child_relations = dicti["as_child_relations"]
    #                   except:
    #                       as_child_relations = None
    #                   try:
    #                       as_parent_relations = dicti["as_parent_relations"]
    #                   except:
    #                       as_parent_relations = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
    #                   try:
    #                       games = dicti["games"]
    #                   except:
    #                            games = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Collection).filter_by(id=id).first()
                        if not instance:
                            collection = table_fields.Collection(
                                id=id,
                                #as_child_relations=as_child_relations,
                                #as_parent_relations,as_parent_relations,
                                created_at=created_at,
                                #games=games,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=collection)
                    case "collection_memberships":
                        try:
                            collection = dicti["collection"]
                        except:
                            collection = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            type = dicti["type"]
                        except:
                            type = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.CollectionMembership).filter_by(id=id).first()
                        if not instance:
                            collection_membership = table_fields.CollectionMembership(
                                id=id,
                                collection=collection,
                                created_at=created_at,
                                game=game,
                                type=type,
                                updated_at=updated_at
                            )
                            session.add(instance=collection_membership)
                    case "collection_membership_types":
                        try:
                            allowed_collection_type = dicti["allowed_collection_type"]
                        except:
                            allowed_collection_type = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.CollectionMembershipType).filter_by(id=id).first()
                        if not instance:
                            collection_membership_type = table_fields.CollectionMembershipType(
                                id=id,
                                allowed_collection_type=allowed_collection_type,
                                created_at=created_at,
                                description=description,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=collection_membership_type)
                    case "collection_relations":
                        try:
                            child_collection = dicti["child_collection"]
                        except:
                            child_collection = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            parent_collection = dicti["parent_collection"]
                        except:
                            parent_collection = None
                        try:
                            type = dicti["type"]
                        except:
                            type = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.CollectionRelation).filter_by(id=id).first()
                        if not instance:
                            collection_relation = table_fields.CollectionRelation(
                                id=id,
                                child_collection=child_collection,
                                created_at=created_at,
                                parent_collection=parent_collection,
                                type=type,
                                updated_at=updated_at
                            )
                            session.add(instance=collection_relation)
                    case "collection_relation_types":
                        try:
                            allowed_child_type = dicti["allowed_child_type"]
                        except:
                            allowed_child_type = None
                        try:
                            allowed_parent_type = dicti["allowed_parent_type"]
                        except:
                            allowed_parent_type = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.CollectionRelationType).filter_by(id=id).first()
                        if not instance:
                            collection_relation_type = table_fields.CollectionRelationType(
                                id=id,
                                allowed_child_type=allowed_child_type,
                                allowed_parent_type=allowed_parent_type,
                                created_at=created_at,
                                description=description,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=collection_relation_type)
                    case "collection_types":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.CollectionType).filter_by(id=id).first()
                        if not instance:
                            collection_type = table_fields.CollectionType(
                                id=id,
                                created_at=created_at,
                                description=description,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=collection_type)
                    case "companies":
                        #does like half of them
                        try:
                            change_date = dicti["change_date"]
                        except:
                            change_date = None
                        try:
                            change_date_category = dicti["change_date_category"]
                        except:
                            change_date_category = None
                        try:
                            changed_company_id = dicti["changed_company_id"]
                        except:
                            changed_company_id = None
                        try:
                            country = dicti["country"]
                        except:
                            country = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        #try:
                        #    developed = dicti["developed"]
                        #except:
                        #    developed = None
                        try:
                            logo = dicti["logo"]
                        except:
                            logo = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            parent = dicti["parent"]
                        except:
                            parent = None
                        #try:
                        #    published = dicti["published"]
                        #except:
                        #    published = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            start_date = dicti["start_date"]
                        except:
                            start_date = None
                        try:
                            start_date_category = dicti["start_date_category"]
                        except:
                            start_date_category = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        #try:
                        #    websites = dicti["websites"]
                        #except:
                        #    websites = None
                        instance = session.query(table_fields.Company).filter_by(id=id).first()
                        if not instance:
                            company = table_fields.Company(
                                id=id,
                                change_date=change_date,
                                change_date_category=change_date_category,
                                changed_company_id=changed_company_id,
                                country=country,
                                created_at=created_at,
                                description=description,
                                #developed=developed,
                                logo=logo,
                                name=name,
                                parent=parent,
                                #published=published,
                                slug=slug,
                                start_date=start_date,
                                start_date_category=start_date_category,
                                updated_at=updated_at,
                                url=url
                                #websites=websites
                            )
                            session.add(instance=company)
                    case "company_logos":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.CompanyLogo).filter_by(id=id).first()
                        if not instance:
                            company_logo = table_fields.CompanyLogo(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=company_logo)
                    case "company_websites":
                        try:
                            trusted = dicti["trusted"]
                        except:
                            trusted = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.CompanyWebsite).filter_by(id=id).first()
                        if not instance:
                            company_website = table_fields.CompanyWebsite(
                                id=id,
                                trusted=trusted,
                                url=url
                            )
                            session.add(instance=company_website)
                    case "covers":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            game_localization = dicti["game_localization"]
                        except:
                            game_localization = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.Cover).filter_by(id=id).first()
                        if not instance:
                            cover = table_fields.Cover(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                game=game,
                                game_localization=game_localization,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=cover)
                    case "events":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            end_time = dicti["end_time"]
                        except:
                            end_time = None
                        try:
                            event_logo = dicti["event_logo"]
                        except:
                            event_logo = None
                        #try:
                        #    event_networks = dicti["event_networks"]
                        #except:
                        #    event_networks = None
                        #try:
                        #    games = dicti["games"]
                        #except:
                        #    games = None
                        try:
                            live_stream_url = dicti["live_stream_url"]
                        except:
                            live_stream_url = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            start_time = dicti["start_time"]
                        except:
                            start_time = None
                        try:
                            time_zone = dicti["time_zone"]
                        except:
                            time_zone = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        #try:
                        #    videos = dicti["videos"]
                        #except:
                        #    videos = None
                        instance = session.query(table_fields.Event).filter_by(id=id).first()
                        if not instance:
                            event = table_fields.Event(
                                id=id,
                                created_at=created_at,
                                description=description,
                                end_time=end_time,
                                event_logo=event_logo,
                                #event_networks=event_networks,
                                #games=games,
                                live_stream_url=live_stream_url,
                                name=name,
                                slug=slug,
                                start_time=start_time,
                                time_zone=time_zone,
                                updated_at=updated_at
                                #videos=videos
                            )
                            session.add(instance=event)
                    case "event_logos":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            event = dicti["event"]
                        except:
                            event = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.EventLogo).filter_by(id=id).first()
                        if not instance:
                            event_logo = table_fields.EventLogo(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                created_at=created_at,
                                event=event,
                                height=height,
                                image_id=image_id,
                                updated_at=updated_at,
                                url=url,
                                width=width
                            )
                            session.add(instance=event_logo)
                    case "event_networks":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            event = dicti["event"]
                        except:
                            event = None
                        try:
                            network_type = dicti["network_type"]
                        except:
                            network_type = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.EventNetwork).filter_by(id=id).first()
                        if not instance:
                            event_network = table_fields.EventNetwork(
                                id=id,
                                created_at=created_at,
                                event=event,
                                network_type=network_type,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=event_network)
                    case "external_games":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        #try:
                        #    countries = dicti["countries"]
                        #except:
                        #    countries = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            media = dicti["media"]
                        except:
                            media = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            platform = dicti["platform"]
                        except:
                            platform = None
                        try:
                            uid = dicti["uid"]
                        except:
                            uid = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            year = dicti["year"]
                        except:
                            year = None
                        instance = session.query(table_fields.ExternalGame).filter_by(id=id).first()
                        if not instance:
                            external_game = table_fields.ExternalGame(
                                id=id,
                                category=category,
                                #countries=countries,
                                created_at=created_at,
                                game=game,
                                media=media,
                                name=name,
                                platform=platform,
                                uid=uid,
                                updated_at=updated_at,
                                url=url,
                                year=year
                            )
                            session.add(instance=external_game)
                    case "franchises":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        #try:
                        #    games = dicti["games"]
                        #except:
                        #    games = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Franchise).filter_by(id=id).first()
                        if not instance:
                            franchise = table_fields.Franchise(
                                id=id,
                                created_at=created_at,
                                #games=games,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=franchise)
                    case "games":
                        #try:
                        #    age_ratings = dicti["age_ratings"]
                        #except:
                        #    age_ratings = None
                        try:
                            aggregated_rating = dicti["aggregated_rating"]
                        except:
                            aggregated_rating = None
                        try:
                            aggregated_rating_count = dicti["aggregated_rating_count"]
                        except:
                            aggregated_rating_count = None
                        #try:
                        #    alternative_names = dicti["alternative_names"]
                        #except:
                        #    alternative_names = None
                        #try:
                        #    artworks = dicti["artworks"]
                        #except:
                        #    artworks = None
                        #try:
                        #    bundles = dicti["bundles"]
                        #except:
                        #    bundles = None
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            collection = dicti["collection"]
                        except:
                            collection = None
                        try:
                            cover = dicti["cover"]
                        except:
                            cover = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        #try:
                        #    dlcs = dicti["dlcs"]
                        #except:
                        #    dlcs = None
                        #try:
                        #    expanded_games = dicti["expanded_games"]
                        #except:
                        #    expanded_games = None
                        #try:
                        #    expansions = dicti["expansions"]
                        #except:
                        #    expansions = None
                        #try:
                        #    external_games = dicti["external_games"]
                        #except:
                        #    external_games = None
                        try:
                            first_release_date = dicti["first_release_date"]
                        except:
                            first_release_date = None
                        try:
                            follows = dicti["follows"]
                        except:
                            follows = None
                        #try:
                        #    forks = dicti["forks"]
                        #except:
                        #    forks = None
                        try:
                            franchise = dicti["franchise"]
                        except:
                            franchise = None
                        #try:
                        #    game_engines = dicti["game_engines"]
                        #except:
                        #    game_engines = None
                        #try:
                        #    game_localizations = dicti["game_localizations"]
                        #except:
                        #    game_localizations = None
                        #try:
                        #    game_modes = dicti["game_modes"]
                        #except:
                        #    game_modes = None
                        #try:
                        #    genres = dicti["genres"]
                        #except:
                        #    genres = None
                        try:
                            hypes = dicti["hypes"]
                        except:
                            hypes = None
                        #try:
                        #    involved_companies = dicti["involved_companies"]
                        #except:
                        #    involved_companies = None
                        #try:
                        #    keywords = dicti["keywords"]
                        #except:
                        #    keywords = None
                        #try:
                        #    language_supports = dicti["language_supports"]
                        #except:
                        #    language_supports = None
                        #try:
                        #    multiplayer_modes = dicti["multiplayer_modes"]
                        #except:
                        #    multiplayer_modes = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            parent_game = dicti["parent_game"]
                        except:
                            parent_game = None
                        #try:
                        #    platforms = dicti["platforms"]
                        #except:
                        #    platforms = None
                        #try:
                        #    player_perspectives = dicti["player_perspectives"]
                        #except:
                        #    player_perspectives = None
                        #try:
                        #    ports = dicti["ports"]
                        #except:
                        #    ports = None
                        try:
                            rating = dicti["rating"]
                        except:
                            rating = None
                        try:
                            rating_count = dicti["rating_count"]
                        except:
                            rating_count = None
                        #try:
                        #    release_dates = dicti["release_dates"]
                        #except:
                        #    release_dates = None
                        #try:
                        #    remakes = dicti["remakes"]
                        #except:
                        #    remakes = None
                        #try:
                        #    remasters = dicti["remasters"]
                        #except:
                        #    remasters = None
                        #try:
                        #    screenshots = dicti["screenshots"]
                        #except:
                        #    screenshots = None
                        #try:
                        #    similar_games = dicti["similar_games"]
                        #except:
                        #    similar_games = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        #try:
                        #    standalone_expansions = dicti["standalone_expansions"]
                        #except:
                        #    standalone_expansions = None
                        try:
                            status = dicti["status"]
                        except:
                            status = None
                        try:
                            storyline = dicti["storyline"]
                        except:
                            storyline = None
                        try:
                            summary = dicti["summary"]
                        except:
                            summary = None
                        #try:
                        #    tags = dicti["tags"]
                        #except:
                        #    tags = None
                        #try:
                        #    themes = dicti["themes"]
                        #except:
                        #    themes = None
                        try:
                            total_rating = dicti["total_rating"]
                        except:
                            total_rating = None
                        try:
                            total_rating_count = dicti["total_rating_count"]
                        except:
                            total_rating_count = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            version_parent = dicti["version_parent"]
                        except:
                            version_parent = None
                        try:
                            version_title = dicti["version_title"]
                        except:
                            version_title = None
                        #try:
                        #    videos = dicti["videos"]
                        #except:
                        #    videos = None
                        #try:
                        #    websites = dicti["websites"]
                        #except:
                        #    websites = None
                        instance = session.query(table_fields.Game).filter_by(id=id).first()
                        if not instance:
                            game = table_fields.Game(
                                id=id,
                                #age_ratings=age_ratings,
                                aggregated_rating=aggregated_rating,
                                aggregated_rating_count=aggregated_rating_count,
                                #alternative_names=alternative_names,
                                #artworks=artworks,
                                #bundles=bundles,
                                category=category,
                                collection=collection,
                                cover=cover,
                                created_at=created_at,
                                #dlcs=dlcs,
                                #expanded_games=expanded_games,
                                #expansions=expansions,
                                #external_games=external_games,
                                first_release_date=first_release_date,
                                follows=follows,
                                #forks=forks,
                                franchise=franchise,
                                #game_engines=game_engines,
                                #game_localizations=game_localizations,
                                #game_modes=game_modes,
                                #genres=genres,
                                hypes=hypes,
                                #involved_companies=involved_companies,
                                #keywords=keywords,
                                #language_supports=language_supports,
                                #multiplayer_modes=multiplayer_modes,
                                name=name,
                                parent_game=parent_game,
                                #platforms=platforms,
                                #player_perspectives=player_perspectives,
                                #ports=ports,
                                rating=rating,
                                rating_count=rating_count,
                                #release_date=release_date
                                #remakes=remakes,
                                #remasters=remasters,
                                #screenshots=screenshots,
                                #similar_games=similar_games,
                                slug=slug,
                                #standalone_expansions=standalone_expansions,
                                status=status,
                                storyline=storyline,
                                summary=summary,
                                #tags=tags,
                                #themes=themes,
                                total_rating=total_rating,
                                total_rating_count=total_rating_count,
                                updated_at=updated_at,
                                url=url,
                                version_parent=version_parent,
                                version_title=version_title
                                #videos=videos,
                                #websites=websites
                            )
                            session.add(instance=game)
                    case "game_engines":
                        #try:
                        #    companies = dicti["companies"]
                        #except:
                        #    companies = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            logo = dicti["logo"]
                        except:
                            logo = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        #try:
                        #    platforms = dicti["platforms"]
                        #except:
                        #    platforms = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.GameEngine).filter_by(id=id).first()
                        if not instance:
                            game_engine = table_fields.GameEngine(
                                id=id,
                                created_at=created_at,
                                #games=games,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=game_engine)
                    case "game_engine_logos":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.GameEngineLogo).filter_by(id=id).first()
                        if not instance:
                            game_engine_logo = table_fields.GameEngineLogo(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=game_engine_logo)
                    case "game_localizations":
                        try:
                            cover = dicti["cover"]
                        except:
                            cover = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            region = dicti["region"]
                        except:
                            region = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.GameLocalization).filter_by(id=id).first()
                        if not instance:
                            game_localization = table_fields.GameLocalization(
                                id=id,
                                cover=cover,
                                created_at=created_at,
                                game=game,
                                name=name,
                                region=region,
                                updated_at=updated_at
                            )
                            session.add(instance=game_localization)
                    case "game_modes":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.GameMode).filter_by(id=id).first()
                        if not instance:
                            game_mode = table_fields.GameMode(
                                id=id,
                                created_at=created_at,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=game_mode)
                    case "game_versions":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        #try:
                        #    features = dicti["features"]
                        #except:
                        #    features = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        #try:
                        #    games = dicti["games"]
                        #except:
                        #    games = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.GameVersion).filter_by(id=id).first()
                        if not instance:
                            game_version = table_fields.GameVersion(
                                id=id,
                                created_at=created_at,
                                #features=features,
                                game=game,
                                #games=games,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=game_version)
                    case "game_version_features":
                        try:
                            category = dicti["crtegory"]
                        except:
                            category = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            position = dicti["position"]
                        except:
                            position = None
                        try:
                            title = dicti["title"]
                        except:
                            title = None
                        #try:
                        #    values = dicti["values"]
                        #except:
                        #    values = None
                        instance = session.query(table_fields.GameVersionFeature).filter_by(id=id).first()
                        if not instance:
                            game_version_feature = table_fields.GameVersionFeature(
                                id=id,
                                category=category,
                                description=description,
                                position=position,
                                title=title
                                #values=values,
                            )
                            session.add(instance=game_version_feature)
                    case "game_version_feature_values":
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            game_feature = dicti["game_feature"]
                        except:
                            game_feature = None
                        try:
                            included_feature = dicti["included_feature"]
                        except:
                            included_feature = None
                        try:
                            note = dicti["note"]
                        except:
                            note = None
                        instance = session.query(table_fields.GameVersionFeatureValue).filter_by(id=id).first()
                        if not instance:
                            game_version_feature_value = table_fields.GameVersionFeatureValue(
                                id=id,
                                game=game,
                                game_feature=game_feature,
                                included_feature=included_feature,
                                note=note
                            )
                            session.add(instance=game_version_feature_value)
                    case "game_videos":
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            video_id = dicti["video_id"]
                        except:
                            video_id = None
                        instance = session.query(table_fields.GameVideo).filter_by(id=id).first()
                        if not instance:
                            game_video = table_fields.GameVideo(
                                id=id,
                                game=game,
                                name=name,
                                video_id=video_id
                            )
                            session.add(instance=game_video)
                    case "genres":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Genre).filter_by(id=id).first()
                        if not instance:
                            genre = table_fields.Genre(
                                id=id,
                                created_at=created_at,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=genre)
                    case "involved_companies":
                        try:
                            company = dicti["company"]
                        except:
                            company = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            developer = dicti["developer"]
                        except:
                            developer = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            porting = dicti["porting"]
                        except:
                            porting = None
                        try:
                            publisher = dicti["publisher"]
                        except:
                            publisher = None
                        try:
                            supporting = dicti["supporting"]
                        except:
                            supporting = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.InvolvedCompany).filter_by(id=id).first()
                        if not instance:
                            involved_company = table_fields.InvolvedCompany(
                                id=id,
                                company=company,
                                created_at=created_at,
                                developer=developer,
                                game=game,
                                porting=porting,
                                publisher=publisher,
                                supporting=supporting,
                                updated_at=updated_at
                            )
                            session.add(instance=involved_company)
                    case "keywords":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Keyword).filter_by(id=id).first()
                        if not instance:
                            keyword = table_fields.Keyword(
                                id=id,
                                created_at=created_at,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=keyword)
                    case "languages":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            locale = dicti["locale"]
                        except:
                            locale = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            native_name = dicti["native_name"]
                        except:
                            native_name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.Language).filter_by(id=id).first()
                        if not instance:
                            language = table_fields.Language(
                                id=id,
                                created_at=created_at,
                                locale=locale,
                                name=name,
                                native_name=native_name,
                                updated_at=updated_at
                            )
                            session.add(instance=language)
                    case "language_supports":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            language = dicti["language"]
                        except:
                            language = None
                        try:
                            language_support_type = dicti["language_support_type"]
                        except:
                            language_support_type = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.LanguageSupport).filter_by(id=id).first()
                        if not instance:
                            language_support = table_fields.LanguageSupport(
                                id=id,
                                created_at=created_at,
                                game=game,
                                language=language,
                                language_support_type=language_support_type,
                                updated_at=updated_at
                            )
                            session.add(instance=language_support)
                    case "multiplayer_modes":
                        try:
                            campaigncoop = dicti["campaigncoop"]
                        except:
                            campaigncoop = None
                        try:
                            dropin = dicti["dropin"]
                        except:
                            dropin = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            lancoop = dicti["lancoop"]
                        except:
                            lancoop = None
                        try:
                            offlinecoop = dicti["offlinecoop"]
                        except:
                            offlinecoop = None
                        try:
                            offlinecoopmax = dicti["offlinecoopmax"]
                        except:
                            offlinecoopmax = None
                        try:
                            offlinemax = dicti["offlinemax"]
                        except:
                            offlinemax = None
                        try:
                            onlinecoop = dicti["onlinecoop"]
                        except:
                            onlinecoop = None
                        try:
                            onlinecoopmax = dicti["onlinecoopmax"]
                        except:
                            onlinecoopmax = None
                        try:
                            onlinemax = dicti["onlinemax"]
                        except:
                            onlinemax = None
                        try:
                            platform = dicti["platform"]
                        except:
                            platform = None
                        try:
                            splitscreen = dicti["splitscreen"]
                        except:
                            splitscreen = None
                        try:
                            splitscreenonline = dicti["splitscreenonline"]
                        except:
                            splitscreenonline = None
                        instance = session.query(table_fields.MultiplayerMode).filter_by(id=id).first()
                        if not instance:
                            multiplayer_mode = table_fields.MultiplayerMode(
                                id=id,
                                campaigncoop=campaigncoop,
                                dropin=dropin,
                                game=game,
                                lancoop=lancoop,
                                offlinecoop=offlinecoop,
                                offlinecoopmax=offlinecoopmax,
                                offlinemax=offlinemax,
                                onlinecoop=onlinecoop,
                                onlinecoopmax=onlinecoopmax,
                                onlinemax=onlinemax,
                                platform=platform,
                                splitscreen=splitscreen,
                                splitscreenonline=splitscreenonline
                            )
                            session.add(instance=multiplayer_mode)
                    case "platforms":
                        try:
                            abbreviation = dicti["abbreviation"]
                        except:
                            abbreviation = None
                        try:
                            alternative_name = dicti["alternative_name"]
                        except:
                            alternative_name = None
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            generation = dicti["generation"]
                        except:
                            generation = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            platform_family = dicti["platform_family"]
                        except:
                            platform_family = None
                        try:
                            platform_logo = dicti["platform_logo"]
                        except:
                            platform_logo = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            summary = dicti["summary"]
                        except:
                            summary = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        #try:
                        #    versions = dicti["versions"]
                        #except:
                        #    versions = None
                        #try:
                        #    websites = dicti["websites"]
                        #except:
                        #    websites = None
                        instance = session.query(table_fields.Platform).filter_by(id=id).first()
                        if not instance:
                            platform = table_fields.Platform(
                                id=id,
                                abbreviation=abbreviation,
                                alternative_name=alternative_name,
                                category=category,
                                created_at=created_at,
                                generation=generation,
                                name=name,
                                platform_family=platform_family,
                                platform_logo=platform_logo,
                                slug=slug,
                                summary=summary,
                                updated_at=updated_at,
                                url=url
                                #versions=versions,
                                #websites=websites
                            )
                            session.add(instance=platform)
                    case "language_support_types":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.LanguageSupportType).filter_by(id=id).first()
                        if not instance:
                            language_support_type = table_fields.LanguageSupportType(
                                id=id,
                                created_at=created_at,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=language_support_type)
                    case "platform_families":
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        instance = session.query(table_fields.PlatformFamily).filter_by(id=id).first()
                        if not instance:
                            platform_family = table_fields.PlatformFamily(
                                id=id,
                                name=name,
                                slug=slug
                            )
                            session.add(instance=platform_family)
                    case "network_types":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        #try:
                        #    event_networks = dicti["event_networks"]
                        #except:
                        #    event_networks = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.NetworkType).filter_by(id=id).first()
                        if not instance:
                            network_type = table_fields.NetworkType(
                                id=id,
                                created_at=created_at,
                                #event_networks=event_networks,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=network_type)
                    case "platform_logos":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.PlatformLogo).filter_by(id=id).first()
                        if not instance:
                            platform_logo = table_fields.PlatformLogo(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=platform_logo)
                    case "platform_version_companies":
                        try:
                            comment = dicti["comment"]
                        except:
                            comment = None
                        try:
                            company = dicti["company"]
                        except:
                            company = None
                        try:
                            developer = dicti["developer"]
                        except:
                            developer = None
                        try:
                            manufacturer = dicti["manufacturer"]
                        except:
                            manufacturer = None
                        instance = session.query(table_fields.PlatformVersionCompany).filter_by(id=id).first()
                        if not instance:
                            platform_version_company = table_fields.PlatformVersionCompany(
                                id=id,
                                comment=comment,
                                company=company,
                                developer=developer,
                                manufacturer=manufacturer
                            )
                            session.add(instance=platform_version_company)
                    case "platform_versions":
                        #try:
                        #    companies = dicti["companies"]
                        #except:
                        #    companies = None
                        try:
                            connectivity = dicti["connectivity"]
                        except:
                            connectivity = None
                        try:
                            cpu = dicti["cpu"]
                        except:
                            cpu = None
                        try:
                            graphics = dicti["graphics"]
                        except:
                            graphics = None
                        try:
                            main_manufacturer = dicti["main_manufacturer"]
                        except:
                            main_manufacturer = None
                        try:
                            media = dicti["media"]
                        except:
                            media = None
                        try:
                            memory = dicti["memory"]
                        except:
                            memory = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            os = dicti["os"]
                        except:
                            os = None
                        try:
                            output = dicti["output"]
                        except:
                            output = None
                        try:
                            platform_logo = dicti["platform_logo"]
                        except:
                            platform_logo = None
                        #try:
                        #    platform_version_release_dates = dicti["platform_version_release_dates"]
                        #except:
                        #    platform_version_release_dates = None
                        try:
                            resolutions = dicti["resolutions"]
                        except:
                            resolutions = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            sound = dicti["sound"]
                        except:
                            sound = None
                        try:
                            storage = dicti["storage"]
                        except:
                            storage = None
                        try:
                            summary = dicti["summary"]
                        except:
                            summary = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.PlatformVersion).filter_by(id=id).first()
                        if not instance:
                            platform_version = table_fields.PlatformVersion(
                                id=id,
                                #companies=companies,
                                connectivity=connectivity,
                                cpu=cpu,
                                graphics=graphics,
                                main_manufacturer=main_manufacturer,
                                media=media,
                                memory=memory,
                                name=name,
                                os=os,
                                output=output,
                                platform_logo=platform_logo,
                                #platform_version_release_dates=platform_version_release_dates,
                                resolutions=resolutions,
                                slug=slug,
                                sound=sound,
                                storage=storage,
                                summary=summary,
                                url=url
                            )
                            session.add(instance=platform_version)
                    case "platform_websites":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            trusted = dicti["trusted"]
                        except:
                            trusted = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.PlatformWebsite).filter_by(id=id).first()
                        if not instance:
                            platform_website = table_fields.PlatformWebsite(
                                id=id,
                                category=category,
                                trusted=trusted,
                                url=url
                            )
                            session.add(instance=platform_website)
                    case "platform_version_release_dates":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            date = dicti["date"]
                        except:
                            date = None
                        try:
                            human = dicti["human"]
                        except:
                            human = None
                        try:
                            m = dicti["m"]
                        except:
                            m = None
                        try:
                            platform_version = dicti["platform_version"]
                        except:
                            platform_version = None
                        try:
                            region = dicti["region"]
                        except:
                            region = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            y = dicti["y"]
                        except:
                            y = None
                        instance = session.query(table_fields.PlatformVersionReleaseDate).filter_by(id=id).first()
                        if not instance:
                            platform_version_release_date = table_fields.PlatformVersionReleaseDate(
                                id=id,
                                category=category,
                                created_at=created_at,
                                date=date,
                                human=human,
                                m=m,
                                platform_version=platform_version,
                                region=region,
                                updated_at=updated_at,
                                y=y
                            )
                            session.add(instance=platform_version_release_date)
                    case "player_perspectives":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.PlayerPerspective).filter_by(id=id).first()
                        if not instance:
                            player_perspective = table_fields.PlayerPerspective(
                                id=id,
                                created_at=created_at,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=player_perspective)
                    case "regions":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            identifier = dicti["identifier"]
                        except:
                            identifier = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.Region).filter_by(id=id).first()
                        if not instance:
                            region = table_fields.Region(
                                id=id,
                                category=category,
                                created_at=created_at,
                                identifier=identifier,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=region)
                    case "release_dates":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            date = dicti["date"]
                        except:
                            date = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            human = dicti["human"]
                        except:
                            human = None
                        try:
                            m = dicti["m"]
                        except:
                            m = None
                        try:
                            platform = dicti["platform"]
                        except:
                            platform = None
                        try:
                            region = dicti["region"]
                        except:
                            region = None
                        try:
                            status = dicti["status"]
                        except:
                            status = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            y = dicti["y"]
                        except:
                            y = None
                        instance = session.query(table_fields.ReleaseDate).filter_by(id=id).first()
                        if not instance:
                            release_date = table_fields.ReleaseDate(
                                id=id,
                                category=category,
                                created_at=created_at,
                                date=date,
                                game=game,
                                human=human,
                                m=m,
                                platform=platform,
                                region=region,
                                status=status,
                                updated_at=updated_at,
                                y=y
                            )
                            session.add(instance=release_date)
                    case "release_date_statuses":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        instance = session.query(table_fields.ReleaseDateStatus).filter_by(id=id).first()
                        if not instance:
                            release_date_status = table_fields.ReleaseDateStatus(
                                id=id,
                                created_at=created_at,
                                description=description,
                                name=name,
                                updated_at=updated_at
                            )
                            session.add(instance=release_date_status)
                    case "screenshots":
                        try:
                            alpha_channel = dicti["alpha_channel"]
                        except:
                            alpha_channel = None
                        try:
                            animated = dicti["animated"]
                        except:
                            animated = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            height = dicti["height"]
                        except:
                            height = None
                        try:
                            image_id = dicti["image_id"]
                        except:
                            image_id = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        try:
                            width = dicti["width"]
                        except:
                            width = None
                        instance = session.query(table_fields.Screenshot).filter_by(id=id).first()
                        if not instance:
                            screenshot = table_fields.Screenshot(
                                id=id,
                                alpha_channel=alpha_channel,
                                animated=animated,
                                game=game,
                                height=height,
                                image_id=image_id,
                                url=url,
                                width=width
                            )
                            session.add(instance=screenshot)
                    case "search":
                        try:
                            alternative_name = dicti["alternative_name"]
                        except:
                            alternative_name = None
                        try:
                            character = dicti["character"]
                        except:
                            character = None
                        try:
                            collection = dicti["collection"]
                        except:
                            collection = None
                        try:
                            company = dicti["company"]
                        except:
                            company = None
                        try:
                            description = dicti["description"]
                        except:
                            description = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            platform = dicti["platform"]
                        except:
                            platform = None
                        try:
                            published_at = dicti["published_at"]
                        except:
                            published_at = None
                        try:
                            test_dummy = dicti["test_dummy"]
                        except:
                            test_dummy = None
                        try:
                            theme = dicti["theme"]
                        except:
                            theme = None
                        instance = session.query(table_fields.Search).filter_by(id=id).first()
                        if not instance:
                            search = table_fields.Search(
                                id=id,
                                alternative_name=alternative_name,
                                character=character,
                                collection=collection,
                                company=company,
                                description=description,
                                game=game,
                                name=name,
                                platform=platform,
                                published_at=published_at,
                                test_dummy=test_dummy,
                                theme=theme
                            )
                            session.add(instance=search)
                    case "themes":
                        try:
                            created_at = dicti["created_at"]
                        except:
                            created_at = None
                        try:
                            name = dicti["name"]
                        except:
                            name = None
                        try:
                            slug = dicti["slug"]
                        except:
                            slug = None
                        try:
                            updated_at = dicti["updated_at"]
                        except:
                            updated_at = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Theme).filter_by(id=id).first()
                        if not instance:
                            theme = table_fields.Theme(
                                id=id,
                                created_at=created_at,
                                name=name,
                                slug=slug,
                                updated_at=updated_at,
                                url=url
                            )
                            session.add(instance=theme)
                    case "websites":
                        try:
                            category = dicti["category"]
                        except:
                            category = None
                        try:
                            game = dicti["game"]
                        except:
                            game = None
                        try:
                            trusted = dicti["trusted"]
                        except:
                            trusted = None
                        try:
                            url = dicti["url"]
                        except:
                            url = None
                        instance = session.query(table_fields.Website).filter_by(id=id).first()
                        if not instance:
                            website = table_fields.Website(
                                id=id,
                                category=category,
                                game=game,
                                trusted=trusted,
                                url=url
                            )
                            session.add(instance=website)
            session.commit()
            logging.info(f"Added from {current_id} to {dicti['id']}")
            current_id = dicti['id'] + 1
            response = (fetch(endpoint, fields, current_id))