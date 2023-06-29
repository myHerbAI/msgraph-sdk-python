from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
    from .pkcs12_certificate_information import Pkcs12CertificateInformation

from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

@dataclass
class ClientCertificateAuthentication(ApiAuthenticationConfigurationBase):
    odata_type = "#microsoft.graph.clientCertificateAuthentication"
    # The list of certificates uploaded for this API connector.
    certificate_list: Optional[List[Pkcs12CertificateInformation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClientCertificateAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClientCertificateAuthentication
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ClientCertificateAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .pkcs12_certificate_information import Pkcs12CertificateInformation

        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .pkcs12_certificate_information import Pkcs12CertificateInformation

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateList": lambda n : setattr(self, 'certificate_list', n.get_collection_of_object_values(Pkcs12CertificateInformation)),
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
        writer.write_collection_of_object_values("certificateList", self.certificate_list)
    

