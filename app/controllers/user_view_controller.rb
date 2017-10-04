class UserViewController < ApplicationController
  before_action :authenticate_user!
  
  def main_page
  end

  def create_product
  end

  def newProduct
    p = Product.create!({:name=>params[:name],:description=>params[:description], :category_id=>params[:category_id], :user_id=>current_user.id})
    if params[:so_1] != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_1]})
    end
    if params[:so_2] != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_2]})
    end
    if params[:so_3] != 1
      ProductShipping.create!({:product_id=>p.id,:shipping_id=>params[:so_3]})
    end
    puts "Lo hice"
  end
end
