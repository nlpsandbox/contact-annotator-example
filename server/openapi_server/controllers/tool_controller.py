from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.models.license import License


def get_tool():  # noqa: E501
    """Get tool information
    Get information about the tool # noqa: E501
    :rtype: Tool
    """
    tool = Tool(
        name="contact-annotator-example",
        version="1.1.2",
        license=License.APACHE_2_0,
        repository="github:nlpsandbox/contact-annotator-example",
        description="Example implementation of the NLP Sandbox Contact Annotator",
        author="NLP Sandbox Team",
        author_email="team@nlpsandbox.io",
        url="https://github.com/nlpsandbox/contact-annotator-example",
        type="nlpsandbox:contact-annotator",
        api_version="1.1.2"
    )
    return tool, 200


def get_tool_dependencies():
    """Get tool dependencies
    Get the dependencies of this tool # noqa: E501
    :rtype: ToolDependencies
    """
    return ToolDependencies(tools=[]), 200
