from django.core.paginator import Paginator


def paginations(request, data_list):
    paginator = Paginator(data_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj
