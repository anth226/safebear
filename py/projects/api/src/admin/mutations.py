import strawberry
from strawberry.tools import merge_types
from strawberry.types.info import Info

from .inputs import UpdateUserInput


@strawberry.type
class UserMutation:
    @strawberry.mutation
    def update_user(
        self,
        info: Info,
        user_id: strawberry.ID,
        input: UpdateUserInput,
    ) -> bool:
        return True

    @strawberry.mutation
    def delete_user(self, info: Info, user_id: strawberry.ID) -> bool:
        return True

    @strawberry.mutation
    def disable_user(self, info: Info, user_id: strawberry.ID) -> bool:
        return True

    @strawberry.mutation
    def delete_users(
        self,
        info: Info,
        user_ids: list[strawberry.ID],
    ) -> bool:
        return True

    @strawberry.mutation
    def disable_users(
        self,
        info: Info,
        user_ids: list[strawberry.ID],
    ) -> bool:
        return True


@strawberry.type
class LabelingMutation:
    @strawberry.mutation(description="Accept a label for a message")
    def accept_label(
        self,
        info: Info,
        message_id: strawberry.ID,
    ) -> bool:
        return True

    @strawberry.mutation(description="Refuse a label for a message")
    def refuse_label(
        self,
        info: Info,
        message_id: strawberry.ID,
    ) -> bool:
        return True

    @strawberry.mutation(description="Skip a label, e.g. because you're not sure")
    def skip_label(
        self,
        info: Info,
        message_id: strawberry.ID,
    ) -> bool:
        return True


@strawberry.type
class AdminMutation:
    @strawberry.mutation
    def update_admin(
        self, info: Info, admin_id: strawberry.ID, input: UpdateUserInput
    ) -> bool:
        return True

    @strawberry.mutation
    def disable_admin(self, info: Info, admin_id: strawberry.ID) -> bool:
        return True

    @strawberry.mutation
    def delete_admin(self, info: Info, admin_id: strawberry.ID) -> bool:
        return True


Mutation = merge_types(
    name="Mutation",
    types=(UserMutation, LabelingMutation, AdminMutation),
)
