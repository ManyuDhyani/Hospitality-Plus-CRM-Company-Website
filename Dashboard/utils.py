from .models import Transaction
from django.db.models import Sum
import calendar

def transaction_line_graph():
    labels = []
    dataCredit = []
    dataDebit = []
    context = {}

    querysetCredit = Transaction.objects.values('date_added__month').annotate(Sum('amount')).order_by('-date_added__month').filter(transaction='Credit')[:7]
    
    querysetDebit = Transaction.objects.values('date_added__month').annotate(Sum('amount')).order_by('-date_added__month').filter(transaction='Debit')[:7]
    

    for i, _ in enumerate(querysetCredit):
        x, y = list(querysetCredit[i].values())
        if x is None:
            continue
        labels.append(calendar.month_name[x])
        dataCredit.append(y)
    
    for i, _ in enumerate(querysetDebit):
        x, y = list(querysetDebit[i].values())
        if x is None:
            continue
        dataDebit.append(y)

    context = {
        'labelsTransactionMonths': labels,
        'dataCredit': dataCredit,
        'dataDebit': dataDebit
    }
    
    return context
