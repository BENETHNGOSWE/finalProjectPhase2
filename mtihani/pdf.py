from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
from django.conf import settings
import uuid

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None



# def html_to_pdf(params:dict):
#     template = get_template("mtihani/generate_exam.html")
#     html = template.render(params)     
#     response = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
#     file_name = uuid.uuid4()
    
#     try:
#         with open(str(settings.BASE_DIR)+ f'/public/static/{file_name}.pdf', 'wb+') as output:
#             pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)

#     except Exception as e:
#         print(e)      

#     if pdf.err:
#         return '', False 

#     return file_name, True         