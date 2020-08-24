from django.db import models

# Create your models here.

class SketchForLife(object):
    def __init__(self,return_val):
        self.return_val = return_val

    def retval(self):
        return self.return_val
        