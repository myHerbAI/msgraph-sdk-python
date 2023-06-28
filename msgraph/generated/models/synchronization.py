from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .synchronization_job import SynchronizationJob
    from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
    from .synchronization_template import SynchronizationTemplate

from .entity import Entity

@dataclass
class Synchronization(Entity):
    # The jobs property
    jobs: Optional[List[SynchronizationJob]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The secrets property
    secrets: Optional[List[SynchronizationSecretKeyStringValuePair]] = None
    # The templates property
    templates: Optional[List[SynchronizationTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Synchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Synchronization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Synchronization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .synchronization_job import SynchronizationJob
        from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
        from .synchronization_template import SynchronizationTemplate

        from .entity import Entity
        from .synchronization_job import SynchronizationJob
        from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
        from .synchronization_template import SynchronizationTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(SynchronizationJob)),
            "secrets": lambda n : setattr(self, 'secrets', n.get_collection_of_object_values(SynchronizationSecretKeyStringValuePair)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(SynchronizationTemplate)),
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
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("secrets", self.secrets)
        writer.write_collection_of_object_values("templates", self.templates)
    
