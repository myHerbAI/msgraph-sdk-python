from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bookings_availability_window import BookingsAvailabilityWindow
    from .bookings_service_availability_type import BookingsServiceAvailabilityType
    from .booking_work_hours import BookingWorkHours

@dataclass
class BookingsAvailability(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The availabilityType property
    availability_type: Optional[BookingsServiceAvailabilityType] = None
    # The hours of operation in a week. The business hours value is set to null if the availability type isn't customWeeklyHours.
    business_hours: Optional[List[BookingWorkHours]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingsAvailability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingsAvailability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingsAvailabilityWindow".casefold():
            from .bookings_availability_window import BookingsAvailabilityWindow

            return BookingsAvailabilityWindow()
        return BookingsAvailability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bookings_availability_window import BookingsAvailabilityWindow
        from .bookings_service_availability_type import BookingsServiceAvailabilityType
        from .booking_work_hours import BookingWorkHours

        from .bookings_availability_window import BookingsAvailabilityWindow
        from .bookings_service_availability_type import BookingsServiceAvailabilityType
        from .booking_work_hours import BookingWorkHours

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityType": lambda n : setattr(self, 'availability_type', n.get_enum_value(BookingsServiceAvailabilityType)),
            "businessHours": lambda n : setattr(self, 'business_hours', n.get_collection_of_object_values(BookingWorkHours)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("availabilityType", self.availability_type)
        writer.write_collection_of_object_values("businessHours", self.business_hours)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
