from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(unique=True, primary_key-True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    hours = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)
#photos
    photo = models.CharField(max_length=100)
    cuisine_type = models.IntegerField()
    price_point = models.CharField(max_length=30)
    kid_friendly = models.BooleanField

class Menu_Items(models.Model):
    menu_item_id = models.IntegerField(unique=True, primary_key-True)
    restaurant_id = models.ForeignKey(Restaurant, related_name='menuitems')
    menu_cat_id = models.ForeignKey(Menu_Categories, related_name='menuitems')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)
    price = models.DecimalField() #checl syntax for this
    additional_info_1 = models.TextField(max_length=4000)
    additional_info_2 = models.TextField(max_length=4000)
    additional_info_3 = models.TextField(max_length=4000)
    cross_contamination = models.BooleanField(initial_value=false)

class Menu_Sub_Item(models.Model):
    menu_subitem_id = models.IntegerField(unique=True, primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, related_name='menusubitems')
    subitem_name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Menu_Categories(models.Model):
    menu_subitem_id = models.IntegerField(unique=True, primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, related_name='menucategories')
    menu_id = models.ForeignKey(Menu, related_name='menucotegories')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Menu(models.Model):
    menu_id = models.IntegerField(unique=True, primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, related_name='menu')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)
    avalibility = models.BooleanField() #again, check syntax
#nutrition info availible?

class Ingredient(models.Model):
    ingredient_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Diet(models.Model):
    diet_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Ingredient_Category(models.Model):
    ingredient_cat_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Allergy_Group(models.Model):
    allergy_group_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)

class Item_To_SubItem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    subitem_id = models.ForeignKey(Menu_Sub_Item, related_name='itemtosubitem')
    menu_item_id = models.ForeignKey(Menu_Items, related_name='itemtosubitem')

class Menu_To_Item(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    item_id = models.ForeignKey(Menu_Items, related_name='menutoitem')
    menu_id = models.ForeignKey(Menu, related_name='menutoitem')

class Menu_To_SubItem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    subitem_id = models.ForeignKey(Menu_Sub_Item, related_name='menutosubitem')
    menu_id = models.ForeignKey(Menu, related_name='menutosubitem')

class Diet_To_Ingredient(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    diet_id = models.ForeignKey(Diet, related_name='diettoingredient')
    ingredient_id = models.ForeignKey(Ingredient, related_name='diettoingredient')

class Ingredient_Category_To_Ingredient(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    ingredient_cat_id = models.ForeignKey(Ingredient_Category, related_name='ingredientcattoingredient')
    ingredient_id = models.ForeignKey(Ingredient, related_name='ingredientcattoingredient')

class Item_To_Ingredient(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    item_id = models.ForeignKey(Menu_Items, related_name='itemtoingredient')
    ingredient_id = models.ForeignKey(Ingredient, related_name='Itemtoingredient')

class Subitem_To_Ingredient(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    subitem_id = models.ForeignKey=(Menu_Sub_Item, related_name='subitemtoingredient')
    ingredient_id = models.ForeignKey(Ingredient, related_name='subitemtoingredient')

class Allergy_Group_To_Ingredient(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    allergy_group_id = models.ForeignKey(Allergy_Group, related_name='allergygrouptoingredient')
    ingredient_id = models.ForeignKey(Ingredient, related_name='allergygrouptoingredient')

class Menu_Category_To_Menu_Item(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    menu_cat_id = models.ForeignKey(Menu_Categories, related_name='menucattomenuitem')
    menu_item_id = models.ForeignKey(Menu_Items, related_name='menuccattomenuitem')





