import strawberry
from strawberry.types import Info

from shared.monitoring import tracer

from ._types import (
    BullyOrderByEnum,
    BullyType,
    ChildType,
    PharosReportType,
    Platform,
    UserActionHistoryType,
    UserType,
)
from .factories import (
    BullyFactory,
    ChildFactory,
    PharosReportFactory,
    UserActionHistoryFactory,
    UserFactory,
    UserStatisticsFactory,
)
from .models import User


@strawberry.type
class Query:
    @strawberry.field
    @tracer.capture_method
    def me(self, info: Info) -> UserType:
        user: User = UserFactory.build()
        data = user.dict(include=UserType.__annotations__.keys())
        return UserType(stats=UserStatisticsFactory.build(), **data)

    @strawberry.field
    @tracer.capture_method
    def child(self, info: Info, user_id: str) -> ChildType:
        return ChildType.from_pydantic(ChildFactory.build())

    @strawberry.field
    @tracer.capture_method
    def bully(self, info: Info, handle: strawberry.ID) -> BullyType:
        return BullyFactory.build()

    @strawberry.field
    @tracer.capture_method
    def bullies(
        self,
        info: Info,
        order_by: BullyOrderByEnum = BullyOrderByEnum.DATE,
    ) -> list[BullyType]:
        bullies = BullyFactory.batch(size=10)
        match order_by:
            case BullyOrderByEnum.DATE:
                bullies.sort(
                    key=lambda tu: tu.last_message,
                    reverse=True,
                )
            case BullyOrderByEnum.FREQUENCY:
                bullies.sort(
                    key=lambda tu: tu.num_toxic_messages,
                    reverse=True,
                )
            case BullyOrderByEnum.VIRULENCE:
                pass
        return bullies

    @strawberry.field
    @tracer.capture_method
    def action_history(self, info: Info) -> list[UserActionHistoryType]:
        return [
            UserActionHistoryType.from_pydantic(action)
            for action in UserActionHistoryFactory.batch(size=10)
        ]

    @strawberry.field
    @tracer.capture_method
    def pharos_report(
        self,
        info: Info,
        platform: Platform,
        handle: strawberry.ID,
    ) -> PharosReportType:
        return PharosReportFactory.build()
