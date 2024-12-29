from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Get all available lexers from Pygments
LEXERS = [item for item in get_all_lexers() if item[1]]

# Create a sorted list of language choices for the dropdown in forms
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

# Create a sorted list of style choices for the dropdown in forms
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    # Automatically set the created date when a snippet is created
    created = models.DateTimeField(auto_now_add=True)
    
    # Title of the snippet, optional
    title = models.CharField(max_length=100, blank=True, default='')
    
    # The actual code snippet
    code = models.TextField()
    
    # Boolean field to indicate if line numbers should be shown
    linenos = models.BooleanField(default=False)
    
    # Language of the code snippet with choices from LANGUAGE_CHOICES
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    
    # Style of the code snippet with choices from STYLE_CHOICES
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        # Order snippets by creation date
        ordering = ['created']