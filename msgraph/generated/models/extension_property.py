from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class ExtensionProperty(DirectoryObject):
    odata_type = "#microsoft.graph.extensionProperty"
    # Display name of the application object on which this extension property is defined. Read-only.
    app_display_name: Optional[str] = None
    # Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum
    data_type: Optional[str] = None
    # Indicates if this extension property was synced from on-premises active directory using Azure AD Connect. Read-only.
    is_synced_from_on_premises: Optional[bool] = None
    # Name of the extension property. Not nullable. Supports $filter (eq).
    name: Optional[str] = None
    # Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
    target_objects: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExtensionProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExtensionProperty
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExtensionProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: Dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "dataType": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "isSyncedFromOnPremises": lambda n : setattr(self, 'is_synced_from_on_premises', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "targetObjects": lambda n : setattr(self, 'target_objects', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("dataType", self.data_type)
        writer.write_bool_value("isSyncedFromOnPremises", self.is_synced_from_on_premises)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("targetObjects", self.target_objects)
    

