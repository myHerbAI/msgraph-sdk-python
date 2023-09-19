from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

@dataclass
class SubjectRightsRequestEnumeratedMailboxLocation(SubjectRightsRequestMailboxLocation):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.subjectRightsRequestEnumeratedMailboxLocation"
    # The userPrincipalNames property
    user_principal_names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestEnumeratedMailboxLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestEnumeratedMailboxLocation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestEnumeratedMailboxLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "userPrincipalNames": lambda n : setattr(self, 'user_principal_names', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("userPrincipalNames", self.user_principal_names)
    
