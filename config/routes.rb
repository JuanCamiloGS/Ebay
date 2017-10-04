Rails.application.routes.draw do
  get 'user_panel', to: 'user_view#main_page'
  get 'create_product', to: 'user_view#create_product'

  devise_for :users
  get 'home/index'
  root 'home#index'
  as :user do
    get 'new_password', to: 'devise/passwords#new'
  end
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
