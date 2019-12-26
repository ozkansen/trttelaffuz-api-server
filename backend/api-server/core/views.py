from django.http import JsonResponse

from lib.trttelaffuz import TrtTelaffuz


def search(request):
    if request.method == "POST":
        keyword = request.POST.get("q")
        search_keyword = TrtTelaffuz(keyword).return_dict_data()
        return JsonResponse(search_keyword)
    return JsonResponse(
        {
            "q": "",
            "detail": "Aranacak kelimeyi 'q' parametresine "
                      "POST metodu ile gönderiniz."
        }
    )
