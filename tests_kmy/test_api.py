# import pytest
#
# @pytest.mark.parametrize(
#     ("user", "status_code"),
#     [
#         ("admin", 200),
#         ("guest", 403),
#         ("", 401)
#     ]
# )
# def test_access_control(user, status_code):
#     response = api.login(user)
#     assert response.status_code == status_code