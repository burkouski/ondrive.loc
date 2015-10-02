import rest_framework_filters as filters
from service.models import AutoService, DiagWork


class AutoserviceFilter(filters.FilterSet):
    #diag_work = django_filters.ModelMultipleChoiceFilter(name='diag_work',queryset=DiagWork.objects.all(), lookup_type="in")
    diag_work = filters.MethodFilter(action='my_custom_filter')
    class Meta:
        model = AutoService
        fields = ['specialization_work','repair_work','diag_work','serv_work','add_work','add_services']

    def my_custom_filter(self, queryset, value):
            print value
            return queryset.filter(
                diag_work=1
            )
