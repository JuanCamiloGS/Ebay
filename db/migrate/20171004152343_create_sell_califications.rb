class CreateSellCalifications < ActiveRecord::Migration[5.1]
  def change
    create_table :sell_califications do |t|
      t.integer :target_user
      t.integer :origin_user
      t.integer :rating
      t.integer :flag

      t.timestamps
    end
  end
end
