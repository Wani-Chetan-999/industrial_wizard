import os
from django.shortcuts import render, redirect
from django.conf import settings
from .models import UploadedDocument
from services.rag_service import RagKnowledgeEngine

def upload_document(request):
    if request.method == "POST" and request.FILES.get('doc_file'):
        category = request.POST.get('category', 'SOP')
        uploaded_file = request.FILES['doc_file']
        
        # Save structural model entry
        doc_instance = UploadedDocument.objects.create(
            file=uploaded_file,
            category=category
        )
        
        # Process the PDF file using our RAG service layer
        file_path = os.path.join(settings.MEDIA_ROOT, doc_instance.file.name)
        
        try:
            rag_engine = RagKnowledgeEngine()
            rag_engine.process_and_index_pdf(file_path, str(doc_instance.id))
            doc_instance.processed = True
            doc_instance.save()
        except Exception as e:
            print(f"Error executing vector indexing pipeline: {e}")
            
        return redirect('upload_document')
        
    documents = UploadedDocument.objects.all().order_by('-upload_date')
    return render(request, 'rag_engine/upload.html', {'documents': documents})