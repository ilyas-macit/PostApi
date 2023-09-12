from models.post import Post, PostUpdateDto
from datetime import datetime

def post_create_entity(item: Post) -> dict:
    return {
        'title': item.title,
        'short_description': item.short_description,
        'description': item.description,
        'tags': item.tags,
        'created_at': datetime.now(),
        'updated_at': None
    }


def post_update_entity(item: PostUpdateDto) -> dict:
    entity = {}
    if hasattr(item, "title"):
        entity['title'] = item.title
    if hasattr(item, "short_description"):
        entity['short_description'] = item.short_description
    if hasattr(item, "description"):
        entity['description'] = item.description
    if hasattr(item, "tags"):
        entity['tags'] = item.tags
    entity['updated_at'] = datetime.now()
    return entity

def post_get_entity(item) -> dict:
    return {
        'id': str(item["_id"]),
        'title': item['title'],
        'short_description': item['short_description'],
        'description': item['description'],
        'tags': item['tags'],
        'created_at': datetime.now(),
        'updated_at': None
    }


def post_get_all_entities(items) -> list:
    return [post_get_entity(item) for item in items]