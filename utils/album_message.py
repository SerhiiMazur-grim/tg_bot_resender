from __future__ import annotations

from typing import List

from aiogram.types import (
    Message,
    InputMedia,
    InputMediaPhoto,
    InputMediaVideo,
    InputMediaAudio,
    InputMediaAnimation,
    InputMediaDocument,
    MessageEntity)



def to_input_media(messages: List[Message]) -> List[InputMedia]:
    media_list = []
    for media_message in messages:
        message: Message = media_message
        caption: str | None = media_message.caption
        caption_entities: List[MessageEntity] | None = media_message.caption_entities
        
        if message.content_type == "photo":
            cls = InputMediaPhoto
            media = message.photo[-1].file_id
        elif message.content_type == "video":
            cls = InputMediaVideo
            media = message.video.file_id
        elif message.content_type == "audio":
            cls = InputMediaAudio
            media = message.audio.file_id
        elif message.content_type == "document":
            cls = InputMediaDocument
            media = message.document.file_id
        elif message.content_type == "animation":
            cls = InputMediaAnimation
            media = message.animation.file_id
        else:
            raise ValueError(f"Unsupported media type {message.content_type}")
        media_data: InputMedia = cls(
            media=media,
            caption=caption,
            caption_entities=caption_entities,
        )
        media_list.append(media_data)
    
    return media_list
