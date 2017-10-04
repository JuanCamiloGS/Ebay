require 'test_helper'

class UserViewControllerTest < ActionDispatch::IntegrationTest
  test "should get main_page" do
    get user_view_main_page_url
    assert_response :success
  end

end
