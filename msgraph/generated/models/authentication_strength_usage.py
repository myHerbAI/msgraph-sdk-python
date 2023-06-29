from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy import ConditionalAccessPolicy

@dataclass
class AuthenticationStrengthUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The mfa property
    mfa: Optional[List[ConditionalAccessPolicy]] = None
    # The none property
    none_: Optional[List[ConditionalAccessPolicy]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthUsage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationStrengthUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy import ConditionalAccessPolicy

        from .conditional_access_policy import ConditionalAccessPolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "mfa": lambda n : setattr(self, 'mfa', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "none": lambda n : setattr(self, 'none_', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("mfa", self.mfa)
        writer.write_collection_of_object_values("none", self.none_)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

