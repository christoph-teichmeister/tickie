from ..models import profile_image_upload_location


def test_profile_image_upload_location(user):
    filename = "test image.jpg"
    expected_path = f"user_{user.id}/test_image.jpg"

    result = profile_image_upload_location(user, filename)

    assert result == expected_path


def test_profile_image_upload_location_with_special_chars(user):
    filename = "test!@#$%^&*() image.jpg"
    expected_path = f"user_{user.id}/test_image.jpg"

    result = profile_image_upload_location(user, filename)

    assert result == expected_path
