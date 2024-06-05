from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...........models.json import Json

@dataclass
class PercentRank_IncPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The array property
    array: Optional[Json] = None
    # The significance property
    significance: Optional[Json] = None
    # The x property
    x: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PercentRank_IncPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PercentRank_IncPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PercentRank_IncPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...........models.json import Json

        from ...........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "array": lambda n : setattr(self, 'array', n.get_object_value(Json)),
            "significance": lambda n : setattr(self, 'significance', n.get_object_value(Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(Json)),
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
        writer.write_object_value("array", self.array)
        writer.write_object_value("significance", self.significance)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    
