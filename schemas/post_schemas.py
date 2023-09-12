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
    if item.title is not None:
        entity['title'] = item.title
    if item.short_description is not None:
        entity['short_description'] = item.short_description
    if item.description is not None:
        entity['description'] = item.description
    if item.tags is not None:
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
        'created_at': item['created_at'],
        'updated_at': item['updated_at']
    }


def post_get_all_entities(items) -> list:
    return [post_get_entity(item) for item in items]