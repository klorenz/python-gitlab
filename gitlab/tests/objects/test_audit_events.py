"""
GitLab API:
https://docs.gitlab.com/ee/api/audit_events.html#project-audit-events
"""

import re

import pytest
import responses

from gitlab.v4.objects.audit_events import ProjectAudit

id = 5

audit_events_content = {
    "id": 5,
    "author_id": 1,
    "entity_id": 7,
    "entity_type": "Project",
    "details": {
        "change": "prevent merge request approval from reviewers",
        "from": "",
        "to": "true",
        "author_name": "Administrator",
        "target_id": 7,
        "target_type": "Project",
        "target_details": "twitter/typeahead-js",
        "ip_address": "127.0.0.1",
        "entity_path": "twitter/typeahead-js",
    },
    "created_at": "2020-05-26T22:55:04.230Z",
}

audit_events_url = re.compile(
    r"http://localhost/api/v4/((groups|projects)/1/)audit_events"
)

audit_events_url_id = re.compile(
    rf"http://localhost/api/v4/((groups|projects)/1/)audit_events/{id}"
)


@pytest.fixture
def resp_list_audit_events():
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url=audit_events_url,
            json=[audit_events_content],
            content_type="application/json",
            status=200,
        )
        yield rsps


@pytest.fixture
def resp_get_variable():
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url=audit_events_url_id,
            json=audit_events_content,
            content_type="application/json",
            status=200,
        )
        yield rsps


def test_list_project_audit_events(project, resp_list_audit_events):
    audit_events = project.audit_events.list()
    assert isinstance(audit_events, list)
    assert isinstance(audit_events[0], ProjectAudit)
    assert audit_events[0].id == id


def test_get_project_audit_events(project, resp_get_variable):
    audit_event = project.audit_events.get(id)
    assert isinstance(audit_event, ProjectAudit)
    assert audit_event.id == id
