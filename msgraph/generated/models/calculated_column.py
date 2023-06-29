from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CalculatedColumn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # For dateTime output types, the format of the value. Possible values are: dateOnly or dateTime.
    format: Optional[str] = None
    # The formula used to compute the value for this column.
    formula: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The output type used to format values in this column. Possible values are: boolean, currency, dateTime, number, or text.
    output_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalculatedColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalculatedColumn
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CalculatedColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outputType": lambda n : setattr(self, 'output_type', n.get_str_value()),
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
        writer.write_str_value("format", self.format)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("outputType", self.output_type)
        writer.write_additional_data_value(self.additional_data)
    

