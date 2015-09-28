import items as i
AmericanEagle_Array = []
BestBuy_Array = []
Kmart_Array = []
WholeFoods_Array = []

Jacket = i.items()
Jacket.setAll('Jacket', 30, 'American Eagle')
Pants = i.items()
Pants.setAll('Pants', 45, 'American Eagle')
Boxers = i.items()
Boxers.setAll('Boxers', 15, 'American Eagle')
Socks = i.items()
Socks.setAll('Socks', 3, 'American Eagle')
Bra = i.items()
Bra.setAll('Bra', 12, 'American Eagle')
Shirts = i.items()
Shirts.setAll('Thongs', 10, 'American Eagle')

AmericanEagle_Array.extend([Jacket, Pants, Boxers, Socks, Bra, Shirts])

USB = i.items()
USB.setAll('USB', 5, 'Best Buy')
Xbox = i.items()
Xbox.setAll('Xbox', 250, 'Best Buy')
Mouse = i.items()
Mouse.setAll('Mouse', 14, 'Best Buy')
HDTV = i.items()
HDTV.setAll('HDTV', 799.99, 'Best Buy')
VideoGames = i.items()
VideoGames.setAll('Video Games', 40, 'Best Buy')
Laptop = i.items()
Laptop.setAll('Laptop', 1000, 'Best Buy')

BestBuy_Array.extend([USB, Xbox, Mouse, HDTV, VideoGames, Laptop])

Cake = i.items()
Cake.setAll('Cake', 25, 'Whole Foods')
Salad = i.items()
Salad.setAll('Salad', 9, 'Whole Foods')
Broccoli = i.items()
Broccoli.setAll('Broccoli', 4, 'Whole Foods')
Sausage = i.items()
Sausage.setAll('Sausage', 3, 'Whole Foods')
Banana = i.items()
Banana.setAll('Banana', 1.50, 'Whole Foods')
Oreos = i.items()
Oreos.setAll('Oreos', 3.50, 'Whole Foods')

WholeFoods_Array.extend([Cake, Salad, Broccoli, Sausage, Banana, Oreos])

TrashBags = i.items()
TrashBags.setAll('TrashBags', 7, 'Kmart')
Table = i.items()
Table.setAll('Table', 24, 'Kmart')
Chair = i.items()
Chair.setAll('Chair', 15, 'Kmart')
Blanket = i.items()
Blanket.setAll('Blanket', 10, 'Kmart')
ChocolateBar = i.items()
ChocolateBar.setAll('Chocolate Bar', 3, 'Kmart')
WaterBottle = i.items()
WaterBottle.setAll('Water Bottle', 5.00, 'Kmart')


Kmart_Array.extend([TrashBags, Table, Chair, Blanket, ChocolateBar, WaterBottle])

