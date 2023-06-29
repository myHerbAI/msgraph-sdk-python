from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

@dataclass
class AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource(AccessReviewInstanceDecisionItemResource):
    odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource"
    # Display name of the access package to which access has been granted.
    access_package_display_name: Optional[str] = None
    # Identifier of the access package to which access has been granted.
    access_package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageDisplayName": lambda n : setattr(self, 'access_package_display_name', n.get_str_value()),
            "accessPackageId": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
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
        writer.write_str_value("accessPackageDisplayName", self.access_package_display_name)
        writer.write_str_value("accessPackageId", self.access_package_id)
    

