from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import MarloProduct
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class MarloProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'brand', 'description', 'price', 'available')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = MarloProduct.objects.update_or_create(
                    name = fields[0],
                    barcode = fields[1],
                    brand = fields[2],
                    description = fields[3],
                    price = fields[4],
                    available = fields[5]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(MarloProduct, MarloProductAdmin)
