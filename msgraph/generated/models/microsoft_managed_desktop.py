from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType

@dataclass
class MicrosoftManagedDesktop(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The managedType property
    managed_type: Optional[MicrosoftManagedDesktopType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The profile property
    profile: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftManagedDesktop:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftManagedDesktop
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftManagedDesktop()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType

        from .microsoft_managed_desktop_type import MicrosoftManagedDesktopType

        fields: Dict[str, Callable[[Any], None]] = {
            "managedType": lambda n : setattr(self, 'managed_type', n.get_enum_value(MicrosoftManagedDesktopType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profile": lambda n : setattr(self, 'profile', n.get_str_value()),
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
        writer.write_enum_value("managedType", self.managed_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profile", self.profile)
        writer.write_additional_data_value(self.additional_data)
    
