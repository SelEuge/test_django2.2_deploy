from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from snippets.models import Snippet
from django.contrib.auth.models import User
from django.utils import timezone
u=User.objects.get(pk=1)
for i in range (201):        
    s=Snippet(created=timezone.now(),title="Valeria",code="Valeria",linenos="Valeria",language="Java",style="Abap",owner="1",highlighted="1")
    s.save()
    print('Creando snippet: ', i)
    pass
