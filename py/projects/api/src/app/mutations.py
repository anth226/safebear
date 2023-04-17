import strawberry
from strawberry.file_uploads import Upload
from strawberry.types.info import Info

from shared.monitoring import tracer

from ._types import Plan, Platform
from .inputs import (
    RegisterInput,
    UpdateProfileInput,
    UploadIdentityDocumentInput,
    UserInvitationInput,
)


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Create a user account")
    @tracer.capture_method
    def register(self, info: Info, input: RegisterInput) -> str:
        return "todo"

    @strawberry.mutation(description="Add a parent to a child's account")
    @tracer.capture_method
    def invite_parent(
        self,
        info: Info,
        input: UserInvitationInput,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Add a child to a parent's account")
    @tracer.capture_method
    def invite_child(
        self,
        info: Info,
        input: UserInvitationInput,
    ) -> str:
        return "todo"

    @strawberry.mutation(
        description="Upload an identity document to verify a user's identity"
    )
    @tracer.capture_method
    def upload_identity_document(
        self,
        info: Info,
        input: UploadIdentityDocumentInput,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Send a user's selfie to verify their identity")
    @tracer.capture_method
    def verify_identity(self, info: Info, image_bytes: Upload) -> str:
        return "todo"

    @strawberry.mutation(description="Select a subscription plan")
    @tracer.capture_method
    def select_plan(self, info: Info, plan: Plan) -> str:
        return "todo"

    @strawberry.mutation(description="Request to access a child's messages")
    @tracer.capture_method
    def access_messages(
        self,
        info: Info,
        conversation_id: strawberry.ID,
    ) -> str:
        # TODO: send email to child asking for the approval to access messages
        # with a deep link to the app that shows a yes/no modal
        return "todo"

    @strawberry.mutation(description="Approve a parent's request to access messages")
    @tracer.capture_method
    def approve_access_messages(
        self,
        info: Info,
        conversation_id: strawberry.ID,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Link a platform to a user's account")
    @tracer.capture_method
    def link_platform(
        self,
        info: Info,
        platform: Platform,
        oauth_token: str,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Unlink a platform from a user's account")
    @tracer.capture_method
    def unlink_platform(
        self,
        info: Info,
        platform: Platform,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Update a user's profile")
    @tracer.capture_method
    def update_profile(
        self,
        info: Info,
        input: UpdateProfileInput,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Delete a user's account")
    @tracer.capture_method
    def delete_account(self, info: Info) -> str:
        return "todo"

    @strawberry.mutation(description="Log out a user")
    @tracer.capture_method
    def logout(self, info: Info) -> str:
        return "todo"

    @strawberry.mutation(description="Block a user")
    @tracer.capture_method
    def block_user(
        self,
        info: Info,
        platform: Platform,
        handle: str,
    ) -> str:
        return "todo"

    @strawberry.mutation(description="Unblock a user")
    @tracer.capture_method
    def unblock_user(
        self,
        info: Info,
        platform: Platform,
        handle: str,
    ) -> str:
        return "todo"
