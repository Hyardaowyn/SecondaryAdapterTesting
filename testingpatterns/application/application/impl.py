import service_locator as sl



class GetArticleQuery:
    def __init__(self, event_id):
        self.__event_id = event_id

    def execute(self):
        return self.__event_id


def michel(event, context):
    notifier = sl.get(EventNotifier)

    article_query = sl.get(GetArticleQuery)

    response = article_query.execute()
    notifier.notify(response)
