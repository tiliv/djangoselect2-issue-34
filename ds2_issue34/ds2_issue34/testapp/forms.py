import logging

from django import forms

from django_select2.fields import AutoModelSelect2Field
from django_select2.views import NO_ERR_RESP

from .models import Store, Employee

logger = logging.getLogger(__name__)

class StoreFKField_Working(AutoModelSelect2Field):
    """ queryset is all objects; no problems. """
    queryset = Store.objects.all()
    search_fields = ['name__icontains']

    def label_from_instance(self, obj):
        # Sanity proof that the field class is being consulted
        return u"LABEL: {}".format(obj)

class StoreFKField_Broken(AutoModelSelect2Field):
    """
    queryset is empty or otherwise limited for security purposes, but we supply the results
    ourselves in ``get_results()``.  There are various reasons for this.  We expect that our value
    will fail validation (logging message from django_select2/widgets.py:411 should appear), but
    the value should be sent through ``_get_val_txt()`` and then into ``validate_value()`` and
    ``get_val_txt()``.

    Code extract from django_select2/widgets.py lines 413 through 417:

        if hasattr(self.field, '_get_val_txt') and selected_choices:
            for val in selected_choices:
                txt = self.field._get_val_txt(val)
                if txt is not None:
                    txts.append(txt)

    ``self.field`` is None, and therefore has no "_get_val_txt".

    """
    queryset = Store.objects.none()
    search_fields = ['name__icontains']

    def label_from_instance(self, obj):
        # Sanity proof that the field class is being consulted
        return u"LABEL: {}".format(obj)

    def get_results(self, request, term, page, context):
        # Returns the whole queryset for example purposes.
        # In a real app, we would apply the search for ``term`` and otherwise generate the queryset.

        queryset = Store.objects.all()

        results = [(store.pk, self.label_from_instance(store)) for store in queryset]
        return (NO_ERR_RESP, False, results)

    def validate_value(self, value):
        # This is never executed; django_select2/widgets.py:413 says that self.field is None,
        # and therefore has no such attribute "_get_val_txt".
        logger.info("Validating value: %r", value)
        return True

    def get_val_txt(self, value):
        # Also never executed for the same reason as validate_value()
        return "Forced as valid: %r" % (value,)

class EmployeeForm(forms.ModelForm):
    # Change this between StoreFKField_Broken and StoreFKField_Working
    store = StoreFKField_Broken()

    class Meta:
        model = Employee
