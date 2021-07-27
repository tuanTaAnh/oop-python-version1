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
    itemlist.add_item("144", 224, 3, 500, "TP HCM", "20/3/2021")
    itemlist.print_itemlist()

    #vechileID, color, branch
    veclist = VechileDAO()
    veclist.add_vechile("x-123", "2L/100km", "Toyota")
    veclist.add_vechile("a-2021", "1.8L/100km", "Vinfast")
    veclist.add_vechile("cx-135", "2.2L/100km", "Ford")
    veclist.print_veclist()

    # uniqueID, typ, address
    retcenterlist = RetailCenterDAO()
    retcenterlist.add_recenter("b-98", "small", "Ha Noi")
    retcenterlist.print_recenterlist()


    # schedulenum, typ, deliveryRoute
    traneventlist = TransportEventDAO()
    traneventlist.add_tran("bc-900", "truck", "Hanoi-Haiphong")
    traneventlist.add_tran("za-808", "bus", "Xa lo ha noi")
    traneventlist.print_tranlist()


    # shippmentID, shippeditem, retailcenter
    # one-to-one relationship
    item_id = "123"
    item = itemlist.get_item_by_id(item_id)
    assert item != None, "Not found item ID"

    recenterID = "b-98"
    recenter = retcenterlist.get_recenter_by_id(recenterID)
    assert item != None, "Not found reteil center ID"

    shilist = ShipmentDAO()
    shilist.add_shipment("b234", item, recenter)
    # shilist.add_shipment("b123", item, recenter)
    shilist.print_shilist()


    #many-to-many relationship illucidate by 2 one-to-many relationship
    vecID1 = "x-123"
    vec1 = veclist.get_vec_by_id(vecID1)
    assert vec1 != None, "Not found vechile ID"

    vecID2 = "a-2021"
    vec2 = veclist.get_vec_by_id(vecID2)
    assert vec2 != None, "Not found vechile ID"

    vecID3 = "a-2021"
    vec3 = veclist.get_vec_by_id(vecID3)
    assert vec3 != None, "Not found vechile ID"

    transID1 = "bc-900"
    trans1 = traneventlist.get_tran_by_id(transID1)
    assert trans1 != None, "Not found transport event ID"

    transID2 = "za-808"
    trans2 = traneventlist.get_tran_by_id(transID2)
    assert trans2 != None, "Not found transport event ID"

    ve_translist = Vechile_TransportEventDAO()
    ve_translist.add_vec_trans(vec1, trans1)
    ve_translist.add_vec_trans(vec2, trans1)
    ve_translist.add_vec_trans(vec3, trans1)
    ve_translist.add_vec_trans(vec1, trans2)
    ve_translist.print_vec_trans_list()

    #many-to-many relationship illucidate by 2 one-to-many relationship
    shiID = "b234"
    shi = shilist.get_shi_by_id(shiID)
    assert shi != None, "Not found shipment ID"

    transID = "bc-900"
    trans = traneventlist.get_tran_by_id(transID)
    assert transID != None, "Not found transport event ID"

    shi_translist = Shipment_TransportEventDAO()
    shi_translist.add_shi_tran(shi, trans)
    shi_translist.print_shi_tranlist()



if __name__ == '__main__':
    create_obj()

