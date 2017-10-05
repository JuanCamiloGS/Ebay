class UserViewController < ApplicationController
  before_action :authenticate_user!

  def main_page
    total = 0
    SellCalification.where("target_user = ?", current_user.id).each do |row|
      puts "entré"
      total = row['rating'].to_i + total
    end
    number = SellCalification.where("target_user = ?", current_user.id).count
    if number == 0
      @sellgrade = 5
    else
      @sellgrade = total.to_f/number
    end
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

    total = 0
    SellCalification.where("target_user = ?", @userId).each do |row|
      total = row['rating'].to_i + total
    end
    number = SellCalification.where("target_user = ?", @userId).count
    if number == 0
      @sellgrade = 5
    else
      @sellgrade = total.to_f/number
    end
  end

  def product_profile
    @productId = params['product']
    @productname = Product.find(@productId).name
    @productdesc = Product.find(@productId).description
    @productcat = Category.find(Product.find(@productId).category_id).name
  end

  def buy_product
    SellCalification.create!({:target_user => Product.find(params['productId']).user_id,:origin_user => current_user.id, :rating => params['grade']})
  end

  def search_view
    @category_id = params['category']
  end

  def block_people
    if params['type'].to_i == 0
      if params['flag'].to_i == 0
        User.connection.execute("Update users SET status = 1 where id = "+params['id'].to_s+";")
      else
        User.connection.execute("Update users SET status = 0 where id = "+params['id'].to_s+";")
      end
    else
      if params['flag'].to_i == 0
        Product.connection.execute("Update products SET block = 1 where id = "+params['id'].to_s+";")
      else
        Product.connection.execute("Update products SET block = 0 where id = "+params['id'].to_s+";")
      end
    end
  end
end
