from django.db import models


class GenericActiveManager(models.Manager):
    """
    Generic custom manager to fetch only the objects marked with
    an active flag.
    """
    def get_query_set(self):
        return (super(GenericActiveManager, self).get_query_set()
                .filter(active=True))
