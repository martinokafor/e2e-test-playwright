class LoginPageLocator:
    username_input_field = "css=[id='user-name']"
    password_input_field = "css=[id='password']"
    login_button = "css=[id='login-button']"
    error_container = "css=[data-test='error']"


class InventoryPageLocator:
    inventory_list = "css=[data-test='inventory-list']"
    inventory_item_name = "css=[data-test='inventory-item-name']"


class InventoryItemPageLocator:
    inventory_details = "css=[class='inventory_details']"
    add_to_cart_button = "css=[data-test='add-to-cart']"
    remove_button = "css=[data-test='remove']"
    shopping_cart_badge = "css=[data-test='shopping-cart-badge']"
