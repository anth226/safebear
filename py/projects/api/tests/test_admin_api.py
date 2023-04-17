from pathlib import Path

import pytest

from src.admin.schema import schema

gql_folder = Path(__file__).parents[1] / "gql" / "admin"
admins_gql = (gql_folder / "admins.gql").read_text()


@pytest.mark.asyncio
async def test_get_admins():
    operation_name = "getAdmins"
    resp = schema.execute_sync(
        query=admins_gql,
        operation_name=operation_name,
    )

    assert resp.errors is None
    assert resp.data
    print(resp.data)
    assert resp.data["admins"][0]["firstName"] == "Audrey"


@pytest.mark.asyncio
async def test_update_admins():
    operation_name = "updateAdmin"
    resp = schema.execute_sync(
        query=admins_gql,
        operation_name=operation_name,
        variable_values={"adminId": "foo"},
    )

    assert resp.errors is None
    assert resp.data
    print(resp.data)
    assert resp.data[operation_name] is True


@pytest.mark.asyncio
async def test_disable_admins():
    operation_name = "disableAdmin"
    resp = schema.execute_sync(
        query=admins_gql,
        operation_name=operation_name,
        variable_values={"adminId": "foo"},
    )

    assert resp.errors is None
    assert resp.data
    print(resp.data)
    assert resp.data[operation_name] is True


@pytest.mark.asyncio
async def test_delete_admins():
    operation_name = "deleteAdmin"
    resp = schema.execute_sync(
        query=admins_gql,
        operation_name=operation_name,
        variable_values={"adminId": "foo"},
    )

    assert resp.errors is None
    assert resp.data
    print(resp.data)
    assert resp.data[operation_name] is True
