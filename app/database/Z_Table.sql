-- Table: Account
CREATE TABLE `Account` (
    `id` INT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `mail` VARCHAR(255),
    `phone` VARCHAR(255),
    `role` VARCHAR(255),
    `create` DATETIME
);

-- Table: History
CREATE TABLE `History` (
    `id` INT PRIMARY KEY,
    `menu_id` INT NOT NULL,
    `quantity` INT NOT NULL,
    `total` INT NOT NULL,
    `time_stamp` DATETIME
);

-- Table: Waste
CREATE TABLE `Waste` (
    `waste_id` INT PRIMARY KEY,
    `item_name` VARCHAR(255) NOT NULL,
    `quantity` FLOAT NOT NULL,
    `unit` VARCHAR(255),
    `price` INT,
    `waste_date` DATETIME,
    `reason` VARCHAR(255),
    `note` VARCHAR(255)
);

-- Table: Menu
CREATE TABLE `Menu` (
    `id` INT PRIMARY KEY,
    `type_id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `image` VARCHAR(255),
    `des` VARCHAR(255),
    `price` INT,
    `tag` VARCHAR(255),
    `Warning` VARCHAR(255)
);

-- Table: Step
CREATE TABLE `Step` (
    `id` INT PRIMARY KEY,
    `step` INT NOT NULL,
    `description` VARCHAR(255),
    `menu_id` INT NOT NULL
);

-- Table: Menu Type
CREATE TABLE `MenuType` (
    `id` INT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `des` VARCHAR(255)
);

-- Table: Payment
CREATE TABLE `Payment` (
    `payment_id` INT PRIMARY KEY,
    `total_price` INT NOT NULL,
    `payment_method` VARCHAR(255),
    `payment_status` VARCHAR(255),
    `payment_date` DATETIME
);

-- Table: Order
CREATE TABLE `Order` (
    `order_id` INT PRIMARY KEY,
    `payment_id` INT,
    `number_table` INT NOT NULL,
    `create_order` DATETIME,
    `number_of_people` INT
);

-- Table: Order Item
CREATE TABLE `OrderItem` (
    `order_item_id` INT PRIMARY KEY,
    `menu_id` INT NOT NULL,
    `menu_qty` INT NOT NULL,
    `menu_note` VARCHAR(255),
    `round_order` INT,
    `create_date` DATETIME,
    `order_id` INT,
    `status_order` VARCHAR(255),
    `status_serve` VARCHAR(255),
    `finish_date` DATETIME
);

-- Table: Ingredients
CREATE TABLE `Ingredients` (
    `Ingredients_id` INT PRIMARY KEY,
    `Ingredients_name` VARCHAR(255) NOT NULL,
    `Ingredients_image` VARCHAR(255),
    `Ingredients_des` VARCHAR(255),
    `main_stock` INT,
    `sub_stock` INT,
    `unit` VARCHAR(255)
);

-- Table: MenuIngredients
CREATE TABLE `MenuIngredients` (
    `MenuIngredients_id` INT PRIMARY KEY,
    `menu_id` INT NOT NULL,
    `ingredient_id` INT NOT NULL,
    `volume` INT,
    `unit` VARCHAR(255)
);
