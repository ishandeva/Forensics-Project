from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.contrib import messages
import openpyxl

@login_required
def dashboard(request):
    return render(request,'app/index.html')

@login_required
def upload(request):

    if "GET" == request.method:
        form = UploadFileForm()
        return render(request, 'app/upload.html', {'form': form})
    else:

        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES
        excel_file = file['file']

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        form.save()
        messages.success(request, f'File Uploaded')
        return render(request, 'app/upload.html', {"excel_data":excel_data})
