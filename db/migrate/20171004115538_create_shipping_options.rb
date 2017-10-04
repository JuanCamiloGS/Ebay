class CreateShippingOptions < ActiveRecord::Migration[5.1]
  def change
    create_table :shipping_options do |t|
      t.string :name

    end
  end
end
