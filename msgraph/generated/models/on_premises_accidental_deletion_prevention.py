from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .on_premises_directory_synchronization_deletion_prevention_type import OnPremisesDirectorySynchronizationDeletionPreventionType

@dataclass
class OnPremisesAccidentalDeletionPrevention(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Threshold value which triggers accidental deletion prevention. The threshold is either an absolute number of objects or a percentage number of objects.
    alert_threshold: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the accidental deletion prevention feature. The possible values are: disabled, enabledForCount, enabledForPercentage, unknownFutureValue.
    synchronization_prevention_type: Optional[OnPremisesDirectorySynchronizationDeletionPreventionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesAccidentalDeletionPrevention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAccidentalDeletionPrevention
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesAccidentalDeletionPrevention()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .on_premises_directory_synchronization_deletion_prevention_type import OnPremisesDirectorySynchronizationDeletionPreventionType

        from .on_premises_directory_synchronization_deletion_prevention_type import OnPremisesDirectorySynchronizationDeletionPreventionType

        fields: Dict[str, Callable[[Any], None]] = {
            "alertThreshold": lambda n : setattr(self, 'alert_threshold', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "synchronizationPreventionType": lambda n : setattr(self, 'synchronization_prevention_type', n.get_enum_value(OnPremisesDirectorySynchronizationDeletionPreventionType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("alertThreshold", self.alert_threshold)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("synchronizationPreventionType", self.synchronization_prevention_type)
        writer.write_additional_data_value(self.additional_data)
    

