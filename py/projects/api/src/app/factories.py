from faker import Faker
from polyfactory import Use
from polyfactory.factories.dataclass_factory import DataclassFactory
from polyfactory.factories.pydantic_factory import ModelFactory

from shared.settings import app_settings

from ._types import (
    BullyType,
    Label,
    PharosReportType,
    StatisticsType,
    UserStatisticsType,
)
from .models import Conversation, User, UserActionHistory


class UserFactory(ModelFactory[User]):
    __model__ = User
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=app_settings.faker.locale)

    @classmethod
    def first_name(cls) -> str:
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls) -> str:
        return cls.__faker__.last_name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    @classmethod
    def birthday(cls) -> str:
        return cls.__faker__.date_of_birth(minimum_age=13, maximum_age=65)

    @classmethod
    def avatar_url(cls) -> str:
        return cls.__faker__.image_url(width=256, height=256)

    @classmethod
    def identity_document_url(cls) -> str:
        return cls.__faker__.image_url(width=256, height=256)

    @classmethod
    def created_at(cls) -> str:
        return cls.__faker__.date_time_this_year()

    @classmethod
    def updated_at(cls) -> str:
        return cls.__faker__.date_time_this_month()


class ChildFactory(UserFactory):
    @classmethod
    def birthday(cls) -> str:
        return cls.__faker__.date_of_birth(minimum_age=13, maximum_age=18)


class ConversationFactory(ModelFactory[Conversation]):
    __model__ = Conversation
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=app_settings.faker.locale)

    @classmethod
    def author(cls) -> str:
        return cls.__faker__.user_name()

    @classmethod
    def body(cls) -> str:
        return cls.__faker__.paragraph()

    @classmethod
    def timestamp(cls) -> str:
        return cls.__faker__.date_time_this_year()


class UserActionHistoryFactory(ModelFactory[UserActionHistory]):
    __model__ = UserActionHistory
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=app_settings.faker.locale)

    @classmethod
    def title(cls) -> str:
        return cls.__faker__.word()

    @classmethod
    def body(cls) -> str:
        return cls.__faker__.paragraph()

    @classmethod
    def timestamp(cls) -> str:
        return cls.__faker__.date_time_this_year()


class BullyFactory(DataclassFactory[BullyType]):
    __model__ = BullyType
    __faker__ = Faker(locale=app_settings.faker.locale)

    @classmethod
    def labels(cls) -> list:
        return cls.__faker__.random_elements(
            elements=list(Label), length=cls.__random__.randint(0, 3), unique=True
        )

    @classmethod
    def handle(cls) -> str:
        return cls.__faker__.user_name()


class StatisticsFactory(DataclassFactory[StatisticsType]):
    __model__ = StatisticsType
    __faker__ = Faker(locale=app_settings.faker.locale)
    __set_as_default_factory_for_type__ = True

    blocked_messages = Use(
        DataclassFactory.__faker__.pyint,
        min_value=0,  # type: ignore
        max_value=100,
    )
    toxic_messages = Use(
        DataclassFactory.__faker__.pyint,
        min_value=100,  # type: ignore
        max_value=200,
    )
    total_messages = Use(
        DataclassFactory.__faker__.pyint,
        min_value=200,  # type: ignore
        max_value=500,
    )


class UserStatisticsFactory(DataclassFactory[UserStatisticsType]):
    __model__ = UserStatisticsType
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=app_settings.faker.locale)


class PharosReportFactory(DataclassFactory[PharosReportType]):
    __model__ = PharosReportType
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=app_settings.faker.locale)

    @classmethod
    def first_name(cls) -> str:
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls) -> str:
        return cls.__faker__.last_name()

    @classmethod
    def gender(cls) -> str:
        return cls.__faker__.simple_profile()["sex"]

    @classmethod
    def age(cls) -> int:
        return cls.__faker__.pyint(min_value=13, max_value=65)

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    @classmethod
    def city(cls) -> str:
        return cls.__faker__.city()

    @classmethod
    def country(cls) -> str:
        return cls.__faker__.country()

    @classmethod
    def platform_url(cls) -> str:
        return cls.__faker__.url()

    @classmethod
    def body(cls) -> str:
        return cls.__faker__.text(max_nb_chars=3950)
