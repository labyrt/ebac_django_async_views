from unittest.mock import AsyncMock, patch

import httpx
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_async_view_executes_awaited_http_call(client):
    mocked_response = httpx.Response(
        status_code=200,
        request=httpx.Request("GET", "https://httpbin.org/"),
    )

    with patch(
        "config.views.http_call_async",
        new=AsyncMock(return_value=mocked_response),
    ) as mocked_call:
        response = client.get(reverse("async-view"))

    assert response.status_code == 200
    assert response.json() == {
        "message": "View assíncrona executada com sucesso",
        "upstream_status": 200,
    }
    mocked_call.assert_awaited_once_with()


def test_home_view_remains_available(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert response.content == b"Django funcionando"
