from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .synchronization_schedule import SynchronizationSchedule
    from .synchronization_schema import SynchronizationSchema
    from .synchronization_status import SynchronizationStatus

from .entity import Entity

@dataclass
class SynchronizationJob(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The schedule property
    schedule: Optional[SynchronizationSchedule] = None
    # The schema property
    schema: Optional[SynchronizationSchema] = None
    # The status property
    status: Optional[SynchronizationStatus] = None
    # The synchronizationJobSettings property
    synchronization_job_settings: Optional[List[KeyValuePair]] = None
    # The templateId property
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJob
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .synchronization_schedule import SynchronizationSchedule
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_status import SynchronizationStatus

        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .synchronization_schedule import SynchronizationSchedule
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_status import SynchronizationStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(SynchronizationSchedule)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(SynchronizationSchema)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SynchronizationStatus)),
            "synchronizationJobSettings": lambda n : setattr(self, 'synchronization_job_settings', n.get_collection_of_object_values(KeyValuePair)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("synchronizationJobSettings", self.synchronization_job_settings)
        writer.write_str_value("templateId", self.template_id)
    
