from django.db import models

class Item(models.Model):
    CATEGORIES = (
        ("beds", "Beds & mattressess"),
        ("furn", "Furniture, wardrobes & shelves"),
        ("sofa", "Sofas & armchairs"),
        ("table", "Tables & chairs"),
        ("texti","Textiles"),
        ("deco","Decoration & mirrors"),
        ("light","Lighting"),
        ("cook","Cookware"),
        ("tablw","Tableware"),
        ("taps","Taps & sinks"),
        ("org", "Organisers & storage accesories"),
        ("toys","Toys"),
        ("leis","Leisure"),
        ("safe","safety"),
        ("diy", "Do-it-yourself"),
        ("floor","Flooring"),
        ("plant","Plants & gardering"),
        ("food","Food & beverages")
    )
    item_number = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_new = models.BooleanField()
    size = models.CharField(max_length=40)
    instructions = models.TextField()
    featured_photo = models.ImageField()
    category = models.CharField(max_length=5, choices=CATEGORIES)
    def __str__(self):
        return  ('[**NEW**]' if self.is_new else '') + "[" + self.category + "] [" + self.item_number + "] " + self.name + " - " + self.description + " (" + self.size + ") : " + str(self.price) + " €"


#Many to many, no se si está bien

class ShoppingCart(models.Model):                         
    cart_id = models.AutoField(primary_key = True)
                                                          
    items = models.ManyToManyField(
        Item,                                             
        through='ItemQuantity',
        #through_fields =('cart_id', 'item_number')
    )

class ItemQuantity(models.Model):
    quantity = models.IntegerField(default = 1)
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)











#Ejemplo manytomany     https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/


#  Otro Ejemplo many to many
#class Person(models.Model): #ITEM
 #   name = models.CharField(max_length=50)

#class Group(models.Model):#qty
 #   name = models.CharField(max_length=128)#ID
  #  members = models.ManyToManyField(
   #     Person,#ITEM
    #    through='Membership',#'ITEMQTY'
     #   through_fields=('group', 'person'),#NO
    #)

#class Membership(models.Model):#cart
 #   group = models.ForeignKey(Group, on_delete=models.CASCADE)
  #  person = models.ForeignKey(Person, on_delete=models.CASCADE)
   # inviter = models.ForeignKey(
    #    Person,
     #   on_delete=models.CASCADE,
      #  related_name="membership_invites",
    #)
    #invite_reason = models.CharField(max_length=64)
    
    
    
