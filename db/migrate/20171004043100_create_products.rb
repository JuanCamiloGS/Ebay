class CreateProducts < ActiveRecord::Migration[5.1]
  def change
    create_table :products do |t|
      t.integer :user_id
      t.string :name
      t.text :description
      t.integer :category_id
      t.boolean :block
      t.boolean :auction

      t.timestamps
    end
  end
end
