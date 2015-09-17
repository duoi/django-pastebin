from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
class Post(models.Model):
#these languages were randomly chosen. the hilightjs library actually supports dozens more.
    LIST_OF_LANGUAGES = (
        ('nohighlight', 'Text'),
        ('code', 'Automatically detect'),
            (_('Select language'), (
            ('python', 'Python'),
            ('javascript', 'Javascript'),
            ('apache', 'Apache'),
            ('css', 'CSS'),
            ('http', 'HTTP'),
            ('ruby', 'Ruby'),
            ('bash', 'Bash'),
            ('coffeescript', 'Coffeescript'),
            ('ini', 'Ini'),
            ('makefile', 'Makefile'),
            ('php', 'PHP'),
            ('sql', 'SQL'),
            ('cs', 'C#'),
            ('diff', 'Diff'),
            ('json', 'JSON'),
            ('markdown', 'Markdown'),
            ('perl', 'Perl'),
            ('cpp', 'C++'),
            ('java', 'Java'),
            ('nginx', 'Nginx'),
            ('python', 'Python'),
            ('django', 'Django'),
            ('html', 'HTML, XML'),
    ))
)
    unique_key = models.CharField(max_length=4, unique=True)
    language = models.CharField(max_length=150, default="nohighlight", choices=LIST_OF_LANGUAGES)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.unique_key
