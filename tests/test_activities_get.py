def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activity_name in payload


def test_get_activities_returns_activity_details_shape(client):
    # Arrange
    sample_activity_name = "Programming Class"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    activity = payload[sample_activity_name]

    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)
