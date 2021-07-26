from models.shippeditem import ShippedItem
from models.retailcenter import RetailCenter
from models.vechile import Vechile
from models.transportenvet import TransportEvent
from models.vechile_transportevent import Vechile_TransportEvent
from models.shipment_transportevent import Shipment_TransportEvent
from models.shippment import Shipment

def create_obj():

    # itemnum, weight, dims, insur_amount, destination, finaldeldate
    item = ShippedItem("123", 200, 2, 300, "Ha Noi", "20/5/2021")
    print(item)

    #vechileID, color, branch
    vec = Vechile("x-123", "red", "Toyota")
    print(vec)

    # uniqueID, typ, address
    retcenter = RetailCenter("b-98", "small", "Ha Noi")
    print(retcenter)

    # schedulenum, typ, deliveryRoute
    tranevent = TransportEvent("bc-900", "truck", "Hanoi-Haiphong")
    print(tranevent)

    # shippmentID, shippeditem, retailcenter
    shi = Shipment("b234", item, retcenter)
    print(shi)

    #many-to-many relationship
    # vechile, transevent
    ve_trans = Vechile_TransportEvent(vec, tranevent)
    print(ve_trans)

    # many-to-many relationship
    # shipment, transevent
    shi_trans = Shipment_TransportEvent(shi, tranevent)
    print(shi_trans)





if __name__ == '__main__':
    create_obj()

