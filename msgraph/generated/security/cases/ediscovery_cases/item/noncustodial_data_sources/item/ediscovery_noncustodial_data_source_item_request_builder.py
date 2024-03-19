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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
    from .data_source.data_source_request_builder import DataSourceRequestBuilder
    from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder
    from .microsoft_graph_security_apply_hold.microsoft_graph_security_apply_hold_request_builder import MicrosoftGraphSecurityApplyHoldRequestBuilder
    from .microsoft_graph_security_release.microsoft_graph_security_release_request_builder import MicrosoftGraphSecurityReleaseRequestBuilder
    from .microsoft_graph_security_remove_hold.microsoft_graph_security_remove_hold_request_builder import MicrosoftGraphSecurityRemoveHoldRequestBuilder
    from .microsoft_graph_security_update_index.microsoft_graph_security_update_index_request_builder import MicrosoftGraphSecurityUpdateIndexRequestBuilder

class EdiscoveryNoncustodialDataSourceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the noncustodialDataSources property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EdiscoveryNoncustodialDataSourceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/noncustodialDataSources/{ediscoveryNoncustodialDataSource%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property noncustodialDataSources for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EdiscoveryNoncustodialDataSource]:
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryNoncustodialDataSource]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

        return await self.request_adapter.send_async(request_info, EdiscoveryNoncustodialDataSource, error_mapping)
    
    async def patch(self,body: Optional[EdiscoveryNoncustodialDataSource] = None, request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EdiscoveryNoncustodialDataSource]:
        """
        Update the navigation property noncustodialDataSources in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryNoncustodialDataSource]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

        return await self.request_adapter.send_async(request_info, EdiscoveryNoncustodialDataSource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property noncustodialDataSources for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/noncustodialDataSources/{ediscoveryNoncustodialDataSource%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[EdiscoveryNoncustodialDataSource] = None, request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property noncustodialDataSources in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/noncustodialDataSources/{ediscoveryNoncustodialDataSource%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EdiscoveryNoncustodialDataSourceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EdiscoveryNoncustodialDataSourceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EdiscoveryNoncustodialDataSourceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def data_source(self) -> DataSourceRequestBuilder:
        """
        Provides operations to manage the dataSource property of the microsoft.graph.security.ediscoveryNoncustodialDataSource entity.
        """
        from .data_source.data_source_request_builder import DataSourceRequestBuilder

        return DataSourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_index_operation(self) -> LastIndexOperationRequestBuilder:
        """
        Provides operations to manage the lastIndexOperation property of the microsoft.graph.security.ediscoveryNoncustodialDataSource entity.
        """
        from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder

        return LastIndexOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_apply_hold(self) -> MicrosoftGraphSecurityApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        from .microsoft_graph_security_apply_hold.microsoft_graph_security_apply_hold_request_builder import MicrosoftGraphSecurityApplyHoldRequestBuilder

        return MicrosoftGraphSecurityApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_release(self) -> MicrosoftGraphSecurityReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        from .microsoft_graph_security_release.microsoft_graph_security_release_request_builder import MicrosoftGraphSecurityReleaseRequestBuilder

        return MicrosoftGraphSecurityReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_remove_hold(self) -> MicrosoftGraphSecurityRemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        from .microsoft_graph_security_remove_hold.microsoft_graph_security_remove_hold_request_builder import MicrosoftGraphSecurityRemoveHoldRequestBuilder

        return MicrosoftGraphSecurityRemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_update_index(self) -> MicrosoftGraphSecurityUpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        from .microsoft_graph_security_update_index.microsoft_graph_security_update_index_request_builder import MicrosoftGraphSecurityUpdateIndexRequestBuilder

        return MicrosoftGraphSecurityUpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderGetQueryParameters():
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilder.EdiscoveryNoncustodialDataSourceItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

