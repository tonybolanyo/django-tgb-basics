class TimeStampedModel(models.Model):
    """
    Clase abstracta que proporciona campos de fecha de cración y modificación
    autogestionadas.
    """

    #: Fecha y hora de creación
    created = models.DateTimeField(
        _("fecha creación"), auto_now_add=True, db_index=True
    )
    #: Fecha y hora de la última actualización
    modified = models.DateTimeField(
        _("fecha actualización"), auto_now=True, db_index=True
    )

    class Meta:
        get_latest_by = "modified"
        ordering = ("-modified", "-created")
        abstract = True
