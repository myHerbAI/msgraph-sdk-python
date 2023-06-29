from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .recording_status import RecordingStatus

@dataclass
class RecordingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The identities of the recording initiator.
    initiator: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordingStatus property
    recording_status: Optional[RecordingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecordingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RecordingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .recording_status import RecordingStatus

        from .identity_set import IdentitySet
        from .recording_status import RecordingStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordingStatus": lambda n : setattr(self, 'recording_status', n.get_enum_value(RecordingStatus)),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recordingStatus", self.recording_status)
        writer.write_additional_data_value(self.additional_data)
    

