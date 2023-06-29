from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .setting_source_type import SettingSourceType

@dataclass
class SettingSource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Not yet documented
    display_name: Optional[str] = None
    # Not yet documented
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sourceType property
    source_type: Optional[SettingSourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SettingSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SettingSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .setting_source_type import SettingSourceType

        from .setting_source_type import SettingSourceType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(SettingSourceType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_additional_data_value(self.additional_data)
    

