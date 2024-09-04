from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rating_canada_movies_type import RatingCanadaMoviesType
    from .rating_canada_television_type import RatingCanadaTelevisionType

@dataclass
class MediaContentRatingCanada(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Movies rating labels in Canada
    movie_rating: Optional[RatingCanadaMoviesType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # TV content rating labels in Canada
    tv_rating: Optional[RatingCanadaTelevisionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MediaContentRatingCanada:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaContentRatingCanada
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MediaContentRatingCanada()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .rating_canada_movies_type import RatingCanadaMoviesType
        from .rating_canada_television_type import RatingCanadaTelevisionType

        from .rating_canada_movies_type import RatingCanadaMoviesType
        from .rating_canada_television_type import RatingCanadaTelevisionType

        fields: Dict[str, Callable[[Any], None]] = {
            "movieRating": lambda n : setattr(self, 'movie_rating', n.get_enum_value(RatingCanadaMoviesType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tvRating": lambda n : setattr(self, 'tv_rating', n.get_enum_value(RatingCanadaTelevisionType)),
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
        writer.write_enum_value("movieRating", self.movie_rating)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tvRating", self.tv_rating)
        writer.write_additional_data_value(self.additional_data)
    

