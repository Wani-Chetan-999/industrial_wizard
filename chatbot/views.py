from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from services.rag_service import RagKnowledgeEngine
from services.groq_service import MultiAgentOrchestrator
from dashboard.models import Equipment

def chat_interface(request):
    equipments = Equipment.objects.all()
    return render(request, 'chatbot/chat.html', {'equipments': equipments})

@csrf_exempt
def process_chat_message(request):
    """AJAX/HTMX processing endpoint for conversational maintenance diagnostics"""
    if request.method == "POST":
        user_query = request.POST.get('message', '')
        selected_equipment_id = request.POST.get('equipment_id', '')

        # Gather real-time metric signatures if an asset is pinned
        current_metrics = {}
        if selected_equipment_id:
            try:
                eq = Equipment.objects.get(equipment_id=selected_equipment_id)
                current_metrics = {
                    "machine": eq.name,
                    "health_percentage": eq.health_percentage,
                    "status_flag": eq.health_status
                }
            except Equipment.DoesNotExist:
                pass

        # 1. Retrieve matching semantic data fragments from ChromaDB
        context_chunks = []
        try:
            rag_engine = RagKnowledgeEngine()
            context_chunks = rag_engine.query_knowledge_base(user_query, n_results=3)
        except Exception as e:
            print(f"ChromaDB retrieval skip: {e}")

        # 2. Invoke our Multi-Agent Orchestrator via Groq
        try:
            orchestrator = MultiAgentOrchestrator()
            ai_response = orchestrator.execute_agentic_workflow(
                engineer_query=user_query,
                context_chunks=context_chunks,
                current_metrics=current_metrics
            )
        except Exception as e:
            ai_response = f"Diagnostic loop exception during agent execution: {str(e)}"

        return JsonResponse({
            'response': ai_response,
            'context_used': context_chunks
        })
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)