from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .unfavorite_post_request_body import UnfavoritePostRequestBody
    from .unfavorite_post_response import UnfavoritePostResponse

class UnfavoriteRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the unfavorite method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UnfavoriteRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/serviceAnnouncement/messages/unfavorite", path_parameters)
    
    async def post(self,body: Optional[UnfavoritePostRequestBody] = None, request_configuration: Optional[UnfavoriteRequestBuilderPostRequestConfiguration] = None) -> Optional[UnfavoritePostResponse]:
        """
        Remove the favorite status of serviceUpdateMessages for the signed in user.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnfavoritePostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/serviceupdatemessage-unfavorite?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .unfavorite_post_response import UnfavoritePostResponse

        return await self.request_adapter.send_async(request_info, UnfavoritePostResponse, error_mapping)
    
    def to_post_request_information(self,body: Optional[UnfavoritePostRequestBody] = None, request_configuration: Optional[UnfavoriteRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Remove the favorite status of serviceUpdateMessages for the signed in user.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> UnfavoriteRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UnfavoriteRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UnfavoriteRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnfavoriteRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

