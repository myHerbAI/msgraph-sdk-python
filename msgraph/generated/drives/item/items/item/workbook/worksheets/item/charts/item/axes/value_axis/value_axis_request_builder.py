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
    from ............models.o_data_errors.o_data_error import ODataError
    from ............models.workbook_chart_axis import WorkbookChartAxis
    from .format.format_request_builder import FormatRequestBuilder
    from .major_gridlines.major_gridlines_request_builder import MajorGridlinesRequestBuilder
    from .minor_gridlines.minor_gridlines_request_builder import MinorGridlinesRequestBuilder
    from .title.title_request_builder import TitleRequestBuilder

class ValueAxisRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the valueAxis property of the microsoft.graph.workbookChartAxes entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ValueAxisRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/valueAxis{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ValueAxisRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property valueAxis for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ValueAxisRequestBuilderGetRequestConfiguration] = None) -> Optional[WorkbookChartAxis]:
        """
        Retrieve the properties and relationships of chartaxis object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChartAxis]
        Find more info here: https://learn.microsoft.com/graph/api/chartaxis-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ............models.workbook_chart_axis import WorkbookChartAxis

        return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)
    
    async def patch(self,body: Optional[WorkbookChartAxis] = None, request_configuration: Optional[ValueAxisRequestBuilderPatchRequestConfiguration] = None) -> Optional[WorkbookChartAxis]:
        """
        Update the properties of chartaxis object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChartAxis]
        Find more info here: https://learn.microsoft.com/graph/api/chartaxis-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ............models.workbook_chart_axis import WorkbookChartAxis

        return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ValueAxisRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property valueAxis for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/valueAxis', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ValueAxisRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of chartaxis object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[WorkbookChartAxis] = None, request_configuration: Optional[ValueAxisRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of chartaxis object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/valueAxis', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ValueAxisRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ValueAxisRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ValueAxisRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def format(self) -> FormatRequestBuilder:
        """
        Provides operations to manage the format property of the microsoft.graph.workbookChartAxis entity.
        """
        from .format.format_request_builder import FormatRequestBuilder

        return FormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def major_gridlines(self) -> MajorGridlinesRequestBuilder:
        """
        Provides operations to manage the majorGridlines property of the microsoft.graph.workbookChartAxis entity.
        """
        from .major_gridlines.major_gridlines_request_builder import MajorGridlinesRequestBuilder

        return MajorGridlinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def minor_gridlines(self) -> MinorGridlinesRequestBuilder:
        """
        Provides operations to manage the minorGridlines property of the microsoft.graph.workbookChartAxis entity.
        """
        from .minor_gridlines.minor_gridlines_request_builder import MinorGridlinesRequestBuilder

        return MinorGridlinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def title(self) -> TitleRequestBuilder:
        """
        Provides operations to manage the title property of the microsoft.graph.workbookChartAxis entity.
        """
        from .title.title_request_builder import TitleRequestBuilder

        return TitleRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ValueAxisRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ValueAxisRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of chartaxis object.
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
    class ValueAxisRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ValueAxisRequestBuilder.ValueAxisRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ValueAxisRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

