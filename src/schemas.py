from dataclasses import dataclass
from typing import Optional, Any, List, Dict

from marshmallow import EXCLUDE


@dataclass
class User:
    id: Optional[Any] = None
    avatar: Optional[Any] = None
    name: Optional[Any] = None
    isReal: Optional[bool] = None
    isGuest: Optional[bool] = None
    level: Optional[int] = None
    administrativeStatus: Optional[Any] = None
    popoverUrl: Optional[Any] = None
    fingerPrint: Optional[Any] = None
    highlinghtName: Optional[bool] = None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Source:
    id: Optional[int] = None
    title: Optional[Any] = None
    url: Optional[Any] = None
    isExternal: Optional[bool] = None


@dataclass
class CharacterisricGrade:
    id: Optional[Any] = None
    title: Optional[Any] = None
    value: Optional[int] = None


@dataclass
class Image:
    id: Optional[Any] = None
    thumbUrl: Optional[Any] = None


@dataclass
class Opinion:
    id: Optional[Any] = None
    objectId: Optional[Any] = None
    objectUrl: Optional[Any] = None
    objectName: Optional[Any] = None
    user: Optional[User] = None
    insertStamp: Optional[Any] = None
    insertStampFormatted: Optional[Any] = None
    updateStamp: Optional[Any] = None
    rating: Optional[int] = None
    source: Optional[Source] = None
    multiCardSpecs: Optional[Any] = None
    period: Optional[Any] = None
    characteristicGrades: Optional[List[CharacterisricGrade]] = None
    plus: Optional[Any] = None
    minus: Optional[Any] = None
    comment: Optional[Any] = None
    usersCommentsCount: Optional[int] = None
    images: Optional[List[Image]] = None
    isEditable: Optional[bool] = None
    additions: Optional[Any] = None
    isCanBeSupplemented: Optional[bool] = None

