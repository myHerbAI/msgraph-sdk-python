from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .service_provisioning_xml_error import ServiceProvisioningXmlError

@dataclass
class ServiceProvisioningError(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The date and time at which the error occurred.
    created_date_time: Optional[datetime.datetime] = None
    # Indicates whether the error has been attended to.
    is_resolved: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Qualified service instance (for example, 'SharePoint/Dublin') that published the service error information.
    service_instance: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningError
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceProvisioningXmlError".casefold():
            from .service_provisioning_xml_error import ServiceProvisioningXmlError

            return ServiceProvisioningXmlError()
        return ServiceProvisioningError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .service_provisioning_xml_error import ServiceProvisioningXmlError

        from .service_provisioning_xml_error import ServiceProvisioningXmlError

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isResolved": lambda n : setattr(self, 'is_resolved', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceInstance": lambda n : setattr(self, 'service_instance', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isResolved", self.is_resolved)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceInstance", self.service_instance)
        writer.write_additional_data_value(self.additional_data)
    

