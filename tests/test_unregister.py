def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": existing_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from {activity_name}"

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert existing_email not in participants


def test_unregister_rejects_participant_not_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    not_enrolled_email = "not.enrolled@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": not_enrolled_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    unknown_activity_name = "Unknown Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{unknown_activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
