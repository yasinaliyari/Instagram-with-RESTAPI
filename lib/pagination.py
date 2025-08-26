from rest_framework.pagination import PageNumberPagination, CursorPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 7


class StandardCursorPagination(PageNumberPagination):
    ordering = "-created_time"


class LargePageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 40
