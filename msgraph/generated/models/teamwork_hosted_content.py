from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_hosted_content import ChatMessageHostedContent
    from .entity import Entity

from .entity import Entity

@dataclass
class TeamworkHostedContent(Entity):
    # Write only. Bytes for the hosted content (such as images).
    content_bytes: Optional[bytes] = None
    # Write only. Content type. sicj as image/png, image/jpg.
    content_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHostedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHostedContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageHostedContent".casefold():
            from .chat_message_hosted_content import ChatMessageHostedContent

            return ChatMessageHostedContent()
        return TeamworkHostedContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .entity import Entity

        from .chat_message_hosted_content import ChatMessageHostedContent
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "contentBytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
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
        writer.write_bytes_value("contentBytes", self.content_bytes)
        writer.write_str_value("contentType", self.content_type)
    

