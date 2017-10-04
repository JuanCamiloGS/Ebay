class CreateProductShippings < ActiveRecord::Migration[5.1]
  def change
    create_table :product_shippings do |t|
      t.integer :product_id
      t.integer :shipping_id

      t.timestamps
    end
  end
end
