import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_contact_annotation_request import TextContactAnnotationRequest  # noqa: E501
from openapi_server.models.text_contact_annotation_response import TextContactAnnotationResponse  # noqa: E501
from openapi_server import util


def create_text_contact_annotations(text_contact_annotation_request=None):  # noqa: E501
    """Annotate contact information in a clinical note

    Return the contact annotations found in a clinical note # noqa: E501

    :param text_contact_annotation_request:
    :type text_contact_annotation_request: dict | bytes

    :rtype: TextContactAnnotationResponse
    """
    if connexion.request.is_json:
        annotation_request = TextContactAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
        note = annotation_request._note

        # detect contact info in note._text



    return 'do some magic!'
