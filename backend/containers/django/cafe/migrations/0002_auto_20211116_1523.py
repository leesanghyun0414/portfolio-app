# Generated by Django 3.2.5 on 2021-11-16 06:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            """
        
        ALTER TABLE cafe_drink_item 
  drop constraint cafe_drink_item_menu_type_50dd2df5_fk_cafe_menu_menu_type;
  
        ALTER TABLE cafe_food_item 
  drop constraint cafe_food_item_menu_type_6c87e2b8_fk_cafe_menu_menu_type;
  
        alter table cafe_menu
        drop constraint cafe_menu_menu_type_key;
  
        ALTER TABLE cafe_drink_item 
      add constraint fk_drink_item
        FOREIGN KEY (menu_id, menu_type)
        REFERENCES cafe_menu (menu_id, menu_type)
        DEFERRABLE INITIALLY DEFERRED;
  
        ALTER TABLE cafe_food_item 
      add constraint fk_food_item
        FOREIGN KEY (menu_id, menu_type)
        REFERENCES cafe_menu (menu_id, menu_type)
        DEFERRABLE INITIALLY DEFERRED;
        """
        )
    ]
