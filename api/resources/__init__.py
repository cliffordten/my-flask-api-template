

def setDocumentaiondb(request):
    rule = request.url_rule
    if 'hello' in rule.rule:
        return True
        # __bind_key__ = 'documenationDB'

    return False

