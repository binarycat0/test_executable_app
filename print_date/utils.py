import datetime
import dateutils


def date_with_offset(offset=0):
    return (datetime.datetime.now().date() + dateutils.relativedelta(days=offset)).isoformat()
