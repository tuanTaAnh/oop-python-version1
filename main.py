from controller.shippeditemDAO import ShippedItemDAO
from controller.vechileDAO import VechileDAO
from controller.retalcenterDAO import RetailCenterDAO
from controller.transporteventDAO import TransportEventDAO
from controller.shipmentDAO import ShipmentDAO
from controller.vechile_transporteventDAO import Vechile_TransportEventDAO
from controller.shipment_transporteventDAO import Shipment_TransportEventDAO



def create_obj():

    # itemnum, weight, dims, insur_amount, destination, finaldeldate
    itemlist = ShippedItemDAO()
    itemlist.add_item("123", 200, 2, 300, "Ha Noi", "20/5/2021")
    itemlist.print_itemlist()

    #vechileID, color, branch
    veclist = VechileDAO()
    veclist.add_vechile("x-123", "2L/100km", "Toyota")
    veclist.print_veclist()

    # uniqueID, typ, address
    retcenterlist = RetailCenterDAO()
    retcenterlist.add_recenter("b-98", "small", "Ha Noi")
    retcenterlist.print_recenterlist()


    # schedulenum, typ, deliveryRoute
    traneventlist = TransportEventDAO()
    traneventlist.add_tran("bc-900", "truck", "Hanoi-Haiphong")
    traneventlist.print_tranlist()


    # shippmentID, shippeditem, retailcenter
    # one-to-one relationship
    shilist = ShipmentDAO()
    shilist.add_shipment("b234", itemlist.get_item_by_id("123"), retcenterlist.get_recenter_by_id("b-98"))
    # shilist.add_shipment("b123", itemlist.get_item_by_id("123"), retcenterlist.get_recenter_by_id("b-98"))
    shilist.print_shilist()


    #many-to-many relationship
    ve_translist = Vechile_TransportEventDAO()
    ve_translist.add_vec_trans(veclist.get_vec_by_id("x-123"), traneventlist.get_tran_by_id("bc-900"))
    ve_translist.print_vec_trans_list()

    # many-to-many relationship
    shi_translist = Shipment_TransportEventDAO()
    shi_translist.add_shi_tran(shilist.get_shi_by_id("b234"), traneventlist.get_tran_by_id("bc-900"))
    shi_translist.print_shi_tranlist()



if __name__ == '__main__':
    create_obj()

