from rest_framework import status
from rest_framework.response import Response

from app.models import PageBean


def page_success(page_bean: PageBean, items: list):
    """
    分页请求响应成功
    :param page_bean: 分页数据
    :param items: 需要返回的结果
    :return: HTTP 响应，状态码为 200
    """
    resp_data = {
        'pageBean': page_bean.to_json(),
        'items': items,
    }
    return Response(__success_data(resp_data), status=status.HTTP_200_OK)


def success(result):
    """
    单组数据请求响应成功
    :param result: 需要返回的结果
    :return: HTTP 响应，状态码为 200
    """
    return Response(__success_data(result), status=status.HTTP_200_OK)


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


def parameters_illegal():
    """
    非法的请求参数
    :return: HTTP 响应，状态码为 400
    """
    return Response(__failure_data('Parameters illegal'), status=status.HTTP_400_BAD_REQUEST)


def failure(reason: str):
    """
    单组数据请求响应失败
    :param reason: 失败的原因
    :return: HTTP 响应，状态码为 200
    """
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
