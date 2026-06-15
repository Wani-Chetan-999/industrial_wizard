import io
from django.http import HttpResponse
from dashboard.models import Equipment
from alerts.models import Alert

def generate_pdf_report(request):
    """
    Generates an itemized operational shift breakdown report as a text file asset.
    """
    equipments = Equipment.objects.all()
    active_alerts = Alert.objects.filter(is_resolved=False)
    
    # Build text stream report
    report_stream = io.StringIO()
    report_stream.write("=====================================================================\n")
    report_stream.write("    IRONEYE AI OPERATIONAL MAINTENANCE EXPORT REPORT // SHIFT OVERVIEW\n")
    report_stream.write("=====================================================================\n\n")
    
    report_stream.write("--- LINE MACHINERY HEALTH LOGS ---\n")
    for eq in equipments:
        report_stream.write(f"Asset Node: {eq.name} [{eq.equipment_id}]\n")
        report_stream.write(f" > Classification Type: {eq.type}\n")
        report_stream.write(f" > Integrity Index Metrics: {eq.health_percentage}% [{eq.health_status}]\n")
        report_stream.write("---------------------------------------------------------------------\n")
        
    report_stream.write("\n--- ACTIVE SECURITY CRITICAL FAULTS ---\n")
    if not active_alerts.exists():
        report_stream.write("Zero active operational faults listed.\n")
    else:
        for idx, alert in enumerate(active_alerts, 1):
            report_stream.write(f"{idx}. [{alert.severity}] Incident: {alert.alert_type}\n")
            report_stream.write(f"   Target Engine: {alert.equipment.name}\n")
            report_stream.write(f"   Diagnostic Trace: {alert.message}\n\n")
            
    report_stream.write("\n[END OF INDUSTRIAL REPORT - SIGNED AUTOMATICALLY BY IRONEYE CORE ENGINE]\n")
    
    response = HttpResponse(report_stream.getvalue(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="steel_plant_operations_report.txt"'
    return response