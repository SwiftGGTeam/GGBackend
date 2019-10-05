from rest_framework import status
from rest_framework.response import Response

from app.models import PageBean


def page_success(page_bean: PageBean, items: list):
    resp_data = {
        'pageBean': page_bean.to_json(),
        'items': items,
    }
    return Response(__success_data(resp_data), status=status.HTTP_200_OK)


def success(results):
    return Response(__success_data(results), status=status.HTTP_200_OK)


def __success_data(results):
    """
    返回请求成功通用结构
    :param results: 返回参数
    :return: 请求成功通用结构
    """
    return {
        'success': True,
        'message': '',
        'results': results
    }


def not_found(reason: str):
    return Response(__failure_data(reason), status=status.HTTP_404_NOT_FOUND)


def parameters_illegal():
    return Response(__failure_data('Parameters illegal'), status=status.HTTP_400_BAD_REQUEST)


def method_not_allowed():
    return Response(__failure_data('Method Not Allowed'), status=status.HTTP_405_METHOD_NOT_ALLOWED)


def failure(reason: str):
    return Response(__failure_data(reason), status=status.HTTP_200_OK)


def __failure_data(reason: str):
    """
    返回请求失败通用结构
    :param reason: 请求失败原因
    :return: 请求失败通用结构
    """
    return {
        'success': False,
        'message': reason,
        'results': None
    }
