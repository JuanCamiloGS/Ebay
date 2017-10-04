class UserViewController < ApplicationController
  before_action :authenticate_user!

  def main_page
  end

  def create_product
  end

  def newProduct
    p = Product.create!({:name=>params[:name],:description=>params[:description], :category_id=>params[:category_id], :user_id=>current_user.id})
    if params[:so_1].to_i != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_1]})
    end
    if params[:so_2].to_i != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_2]})
    end
    if params[:so_3].to_i != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_3]})
    end
    puts "Lo hice"
  end

  def others_page
    @userId = params['user']
    @username = User.find(@userId).name
    @userdesc = User.find(@userId).description
  end

  def product_profile
    @productId = params['product']
    @productname = Product.find(@productId).name
    @productdesc = Product.find(@productId).description
    @productcat = Category.find(Product.find(@productId).category_id).name
  end

  def buy_product
    SellCalification.create!({:target_user => Product.find(params['productId']),:origin_user => current_user.id, :rating => params['grade']})
  end
end
