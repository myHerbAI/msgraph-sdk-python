from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_answer_string import AccessPackageAnswerString
    from .access_package_question import AccessPackageQuestion

@dataclass
class AccessPackageAnswer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The answeredQuestion property
    answered_question: Optional[AccessPackageQuestion] = None
    # The localized display value shown to the requestor and approvers.
    display_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAnswerString".casefold():
            from .access_package_answer_string import AccessPackageAnswerString

            return AccessPackageAnswerString()
        return AccessPackageAnswer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_answer_string import AccessPackageAnswerString
        from .access_package_question import AccessPackageQuestion

        from .access_package_answer_string import AccessPackageAnswerString
        from .access_package_question import AccessPackageQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "answeredQuestion": lambda n : setattr(self, 'answered_question', n.get_object_value(AccessPackageQuestion)),
            "displayValue": lambda n : setattr(self, 'display_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("answeredQuestion", self.answered_question)
        writer.write_str_value("displayValue", self.display_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

