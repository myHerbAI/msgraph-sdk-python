from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact import Artifact
    from .host import Host

from .artifact import Artifact

@dataclass
class HostComponent(Artifact):
    odata_type = "#microsoft.graph.security.hostComponent"
    # The type of component that was detected (for example, Operating System, Framework, Remote Access, or Server).
    category: Optional[str] = None
    # The first date and time when Microsoft Defender Threat Intelligence observed this web component. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host property
    host: Optional[Host] = None
    # The most recent date and time when Microsoft Defender Threat Intelligence observed this web component. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # A name running on the artifact, for example, Microsoft IIS.
    name: Optional[str] = None
    # The component version running on the artifact, for example, v8.5. This should not be assumed to be strictly numerical.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostComponent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostComponent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HostComponent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .artifact import Artifact
        from .host import Host

        from .artifact import Artifact
        from .host import Host

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("version", self.version)
    

