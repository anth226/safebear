from faker import Faker
from polyfactory.factories.dataclass_factory import DataclassFactory
from polyfactory.factories.pydantic_factory import ModelFactory

from shared.settings import admin_settings

from ._types import UnverifiedLabel, VerifiedLabel
from .models import AdminUser


class UnverifiedLabelFactory(DataclassFactory[UnverifiedLabel]):
    __model__ = UnverifiedLabel
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=admin_settings.faker.locale)

    @classmethod
    def score(cls) -> float:
        return cls.__faker__.pyfloat(
            min_value=0.0,
            max_value=1.0,
            right_digits=2,
        )

    @classmethod
    def message(cls) -> str:
        return cls.__faker__.paragraph()


class VerifiedLabelFactory(UnverifiedLabelFactory):
    __model__ = VerifiedLabel
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=admin_settings.faker.locale)

    @classmethod
    def verified_by(cls) -> str:
        return cls.__faker__.first_name()


class AdminUserFactory(ModelFactory[AdminUser]):
    __model__ = AdminUser
    __set_as_default_factory_for_type__ = True
    __faker__ = Faker(locale=admin_settings.faker.locale)

    @classmethod
    def first_name(cls) -> str:
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls) -> str:
        return cls.__faker__.last_name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()
