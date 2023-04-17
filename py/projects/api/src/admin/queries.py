import strawberry
from strawberry.tools import merge_types
from strawberry.types.info import Info

from ..app._types import UserType
from ..app.factories import UserFactory
from ._types import AdminUserType, UnverifiedLabel, VerifiedLabel
from .factories import AdminUserFactory, UnverifiedLabelFactory, VerifiedLabelFactory
from .inputs import DirectionEnum, UserFiltersInput, UserOrderByInput


@strawberry.type
class UserQuery:
    @strawberry.field
    def users(
        self,
        info: Info,
        filters: UserFiltersInput | None = None,
        order_by: UserOrderByInput | None = None,
    ) -> list[UserType]:
        users: list[UserType] = UserFactory.batch(100)
        # Filter
        if filters:
            if filters.query:
                users = list(
                    filter(
                        lambda user: filters.query.lower() in user.full_name.lower(),  # type: ignore # noqa: line-too-long
                        users,
                    )
                )
            if filters.plan:
                users = list(
                    filter(
                        lambda user: user.plan == filters.plan, users  # type: ignore
                    )
                )
        # Trim
        users = users[:10]
        # Sort
        if order_by:
            users = sorted(
                users,
                key=lambda user: getattr(user, order_by.field),  # type: ignore
                reverse=order_by.direction == DirectionEnum.DESC,
            )
        return users


@strawberry.type
class LabelingQuery:
    @strawberry.field
    def labeling_tasks(self, info: Info) -> list[UnverifiedLabel]:
        # Generate
        tasks = UnverifiedLabelFactory.batch(100)
        # Sort
        tasks = sorted(tasks, key=lambda task: task.score, reverse=False)
        # Get random slice
        tasks = tasks[:10]
        return tasks

    @strawberry.field
    def labeling_history(self, info: Info) -> list[VerifiedLabel]:
        # Generate
        tasks = VerifiedLabelFactory.batch(20)
        # Sort
        tasks = sorted(tasks, key=lambda task: task.verified_at, reverse=True)
        return tasks


@strawberry.type
class AdminQuery:
    @strawberry.field
    def admins(self, info: Info) -> list[AdminUserType]:
        return AdminUserFactory.batch(10)


Query = merge_types(name="Query", types=(UserQuery, LabelingQuery, AdminQuery))
