from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PasswordCredential(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Do not use.
    custom_key_identifier: Optional[bytes] = None
    # Friendly name for the password. Optional.
    display_name: Optional[str] = None
    # The date and time at which the password expires represented using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
    end_date_time: Optional[datetime.datetime] = None
    # Contains the first three characters of the password. Read-only.
    hint: Optional[str] = None
    # The unique identifier for the password.
    key_id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only; Contains the strong passwords generated by Microsoft Entra ID that are 16-64 characters in length. The generated password value is only returned during the initial POST request to addPassword. There is no way to retrieve this password in the future.
    secret_text: Optional[str] = None
    # The date and time at which the password becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordCredential()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "customKeyIdentifier": lambda n : setattr(self, 'custom_key_identifier', n.get_bytes_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "hint": lambda n : setattr(self, 'hint', n.get_str_value()),
            "keyId": lambda n : setattr(self, 'key_id', n.get_uuid_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secretText": lambda n : setattr(self, 'secret_text', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_bytes_value("customKeyIdentifier", self.custom_key_identifier)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("hint", self.hint)
        writer.write_uuid_value("keyId", self.key_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("secretText", self.secret_text)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

