class HomeController < ApplicationController
  def index
    #@recentlyUpdated = Product.order(:created_at).group("category_id, created_at").maximum("created_at")
    @recentlyUpdated = Product.connection.execute("SELECT MAX(id) as id, name, category_id, user_id, created_at, block FROM products GROUP BY category_id, name, user_id, created_at, block")
    #print "#{@recentlyUpdated}"
    #@recentlyUpdated = @recentlyUpdated[0]
  end
end
